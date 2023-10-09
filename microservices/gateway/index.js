const express = require("express");
const app = express();
const cors = require("cors");
const bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: false }));
const proxy = require("express-http-proxy");

app.use(bodyParser.json());

app.use(cors());
app.use(express.json()); // Use express.json() middleware to parse JSON data

app.use(
  "/feedback",
  proxy("http://ec2-3-110-224-61.ap-south-1.compute.amazonaws.com/")
);

app.use(
  "/message",
  proxy("http://ec2-52-66-241-218.ap-south-1.compute.amazonaws.com/")
);

app.use(
  "/",
  proxy("http://ec2-43-204-107-116.ap-south-1.compute.amazonaws.com/")
);

app.listen(8000, () => {
  console.log("Gateway is listening on port 8000...");
});
