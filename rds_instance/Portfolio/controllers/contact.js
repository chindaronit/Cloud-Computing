const conn = require('../database');


const getval = (req, res) => { // Corrected order of parameters
    
    conn.query("SELECT * FROM contact", function (err, result) {
        if (err) {
            console.error(err);
            return res.status(500).json({ status: false, error: "Database error" });
        }

        res.status(200).json(result);
    });
}

const postval = (req, res) => {
    const formdata = req.body;
    const sql = 'INSERT INTO contact SET ?';
    conn.query(sql, formdata, function (err, data) {
        if (err) throw err;
        console.log("data inserted ..."); 
    });

    res.status(200).redirect('/'); // Redirect to the form page after inserting data
}


module.exports = {
    getval,
    postval
}

