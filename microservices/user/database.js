var mysql = require("mysql");
var conn = mysql.createConnection({
  // host: "skywalker-db.cxq4xccdowko.ap-south-1.rds.amazonaws.com",
  port: "3306",
  host: "localhost",
  user: "victus",
  password: "Chinda@7988",
  database: "user",
});

conn.connect(function (err) {
  if (err) throw err;

  conn.query(
    "create table if not exists users (firstname varchar(255), lastname varchar(255), email varchar(255), phoneno varchar(15), PRIMARY KEY (email));",
    function (err, result) {
      if (err) {
        console.error(err);
      } else {
        console.log("user table created!");
      }
    }
  );
});

module.exports = conn;
