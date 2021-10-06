const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const routes = require("./api/routes/index.js");
const mysql = require("mysql");
require("dotenv").config();

// const db = mysql.createPool(process.env.CLEARDB_DATABASE_URL);
const db = mysql.createPool("localhost");

// Express Middleware
app = express();
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors());

// Provide Routes
app.use("/", routes);

// Start Server
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
    console.log(`listening on port ${PORT}`);
});
