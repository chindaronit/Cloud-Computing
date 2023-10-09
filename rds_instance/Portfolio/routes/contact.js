const express = require('express')
const router = express.Router()


const {
    getval,
    postval
} = require('../controllers/contact.js')


router.route("/contacts").get(getval)
router.route("/").post(postval)


module.exports = router