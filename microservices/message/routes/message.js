const express = require("express");
const router = express.Router();
const path = require('path');
const { getval, postval } = require("../controllers/message.js");

router.route("/api").get(getval);
router.route("/post").post(postval);

router.route("/").get((req, res) => {
  res.sendFile(path.resolve(__dirname + "/../public/message.html"));
});

module.exports = router;
