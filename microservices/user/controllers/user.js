const conn = require("../database");

const postval = (req, res) => {
  const formdata = req.body;

  try {
    // Check if a user with the same email already exists
    const sql = "SELECT * FROM users WHERE email = ?";
    conn.query(sql, formdata.email, (err, result) => {
      if (err) {
        console.error(err);
        return res.status(500).json({ status: false, error: "exist error" });
      }

      if (result && result.length > 0) {
        return res.status(302).redirect("/dev/message/");
      }

      // If the email is unique, proceed to insert the new user
      const insertSql = "INSERT INTO users SET ?";
      conn.query(insertSql, formdata, (err, data) => {
        if (err) {
          console.error(err);
          return res
            .status(500)
            .json({ status: false, error: "Database error" });
        }

        console.log("Data inserted ...");

        return res.status(302).redirect("/dev/message/");
      });
    });
  } catch (error) {
    console.error(error);
    return res.status(500).json(error);
  }
};

module.exports = { postval };
