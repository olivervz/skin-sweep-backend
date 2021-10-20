const express = require("express");
const router = express.Router();

router.post("/CreateAccount", require("./CreateAccount"));
router.get("/GetUserID", require("./GetUserID"));

module.exports = router;
