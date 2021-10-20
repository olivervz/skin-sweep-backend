const jssha = require("jssha");
const mysql = require("mysql");

exports.CreateAccount = (req, res) => {
    const username = req.body.username;
    const email = req.body.email;
    const password = req.body.password;

    const jsshaObj = new jssha("SHA-512", "TEXT", {
        encoding: "UTF8",
    });

    jsshaObj.update(password);
    const hashedPassword = jsshaObj.getHash("HEX");

    const db = mysql.createPool(process.env.CLEARDB_DATABASE_URL);

    const sqlInsert =
        "INSERT INTO users (username, email, password) VALUES (?,?,?);";

    db.query(sqlInsert, [username, email, hashedPassword], (err, result) => {
        const sqlSelect = "SELECT id FROM users WHERE username = ?";
        db.query(sqlSelect, [username], (err, result) => {
            res.send({ id: result[0].id });
        });
    });
};
