const conn = require("../database");

const getval = (req, res) => {
  conn.query("SELECT * FROM message", function (err, result) {
    if (err) {
      console.error(err);
      return res.status(500).json({ status: false, error: "Database error" });
    }
    res.status(200).json(result);
  });
};

const postval = (req, res) => {
  const formdata = req.body;

  const sql = "INSERT INTO message SET ?";
  conn.query(sql, formdata, function (err, data) {
    if (err) {
      console.error(err);
      return res.status(500).json({ status: false, error: "Database error" });
    }
    console.log("Data inserted ...");

    // Redirect to the form page after inserting data
    return res.status(302).redirect("/dev/message/");
  });
};

module.exports = { getval, postval };
