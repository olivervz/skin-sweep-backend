# This uses the metadata CSV to move the top-level, unsorted HAM10000 images into their respective class directories.
import pandas as pd
import numpy as np
import os
from shutil import copy2

ham_path = '../../data/ham10000/'
image_path = ham_path + 'images/'
validation_path = ham_path + 'validation/'
metadata = ham_path + 'HAM10000_metadata.csv'
ground_truth = ham_path + 'ISIC2018_Task3_Validation_GroundTruth.csv'


def make_class_dirs(dir_name, classes):
    for c in classes:
        class_dir_name = dir_name + c
        print('Creating training directory', class_dir_name, '...')
        try:
            os.mkdir(class_dir_name)
        except FileExistsError:
            print('  (Directory', class_dir_name, 'already exists)')


def copy_to_classdir(row):
    jpg = row.image_id + '.jpg'
    class_dir = 'class_' + row.dx + '/'
    src = image_path + jpg
    dest = image_path + class_dir + jpg
    # print('copying', src, 'to', dest)
    copy2(src, dest)


def copy_to_validationdir(row):
    jpg = row.image + '.jpg'
    index = np.where(row)[0][1]
    label = ground_truth_headers[index].lower()
    validation_dir = 'class_' + label + '/'
    src = validation_path + jpg
    dest = validation_path + validation_dir + jpg
    # print('copying', src, 'to', dest)
    copy2(src, dest)


# Separate training data into class folders
df_training = pd.read_csv(metadata)
classes = pd.unique(df_training['dx'])
classes_counts = [df_training.dx.value_counts()[lesion_class] for lesion_class in classes]

training_class_dirs = ham_path + '/images/class_'
make_class_dirs(training_class_dirs, classes)

print('Copying', len(df_training), 'training images...')
df_training.apply(copy_to_classdir, axis=1)
print('Training data copied into class directories.')

# Separate validation into class foldiers
df_validation = pd.read_csv(ground_truth)
ground_truth_headers = list(df_validation)

# Create validation directories
validation_class_dirs = ham_path + '/validation/class_'
make_class_dirs(validation_class_dirs, classes)

print('Copying', len(df_validation), 'validation images...')
df_validation.apply(copy_to_validationdir, axis=1)
print('Validation data copied into class directories.')
