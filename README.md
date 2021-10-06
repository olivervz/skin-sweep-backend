# Backend for SkinSweep

## To run development server:

### `npm run dev`

### Will default to `localhost:3001`

## Necessary API endpoints

### CreateAccount: [username, email, password] -> userID

#### Create an account with a username, email, and password

#### Returned userID is used to access records

<br />

### ResetPassword: [userID, password] -> \_

#### Reset password using valid userID

<br />

### UpdateInformation: [userID, username, email, password] -> \_

#### Update username and or email and or password, must be logged in

<br />

### Login: [username, password] -> userID

#### log into account using correct username and password

<br />
