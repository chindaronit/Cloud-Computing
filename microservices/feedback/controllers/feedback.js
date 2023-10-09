const conn = require("../database");

const getval = (req, res) => {
  conn.query("SELECT * FROM feedback", function (err, result) {
    if (err) {
      console.error(err);
      return res.status(500).json({ status: false, error: "Database error" });
    }
    res.status(200).json(result);
  });
};

const postval = (req, res) => {
  const formdata = req.body;
  console.log(req.body);

  const sql = "INSERT INTO feedback SET ?";
  conn.query(sql, formdata, function (err, data) {
    if (err) throw err;
    console.log("data inserted ...");
  });

  return res.status(302).redirect("/dev/feedback/"); // Redirect to the form page after inserting data
};

module.exports = { getval, postval };
