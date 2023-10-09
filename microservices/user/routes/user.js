const express = require("express");
const router = express.Router();
const path = require("path");
const { postval } = require("../controllers/user.js");


router.route("/post").post(postval);

router.route("/").get((req, res) => {
  res.sendFile(path.resolve(__dirname + "/../public/user.html"));
});

module.exports = router;
