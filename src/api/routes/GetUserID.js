const express = require("express"),
    router = express.Router(),
    GetUserID = require("../controllers/GetUserID");

router.get("/GetUserID", GetUserID.GetUserID);

module.exports = router;
