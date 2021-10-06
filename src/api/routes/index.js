const express = require("express");
const router = express.Router();

router.post("/CreateAccount", require("./CreateAccount"));

module.exports = router;
