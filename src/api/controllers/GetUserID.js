const mysql = require("mysql");

exports.GetUserID = (req, res) => {
    const db = mysql.createPool(process.env.CLEARDB_DATABASE_URL);

    const sqlSelect = "SELECT * FROM users WHERE username=?";
    db.query(sqlSelect, (err, result) => {
        console.log(result);
        console.log(err);
        res.send(result);
    });
};
