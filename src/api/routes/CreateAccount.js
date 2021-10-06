const express = require("express"),
    router = express.Router(),
    CreateAccount = require("../controllers/CreateAccount");

router.post("/CreateAccount", CreateAccount.CreateAccount);

module.exports = router;
