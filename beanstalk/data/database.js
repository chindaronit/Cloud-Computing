var mysql = require('mysql');
var conn = mysql.createConnection({
    host: 'skywalker-db.cxq4xccdowko.ap-south-1.rds.amazonaws.com',
    port: '3306',
    user: 'victus',
    password: "victus123",
    database: 'portfolio'
});


conn.connect(function (err) {
    if (err) throw err;
    
    conn.query("create table if not exists contact (firstname varchar(255),lastname varchar(255), email varchar(255),phoneno varchar(15), message varchar(500));", function (err, result) {
        if (err) {
            console.error(err);
            return res.status(500).json({ status: false, error: "Database error" });
        }
        console.log("table created!")
    });

});

module.exports = conn;