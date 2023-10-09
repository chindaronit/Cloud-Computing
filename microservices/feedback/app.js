const express = require("express");
const app = express();
const feedback = require("./routes/feedback");

// Setup static middleware to serve static files from the "public" directory
app.use(express.static("public"));
app.use(express.urlencoded({ extended: false }));
app.use(express.json()); // Use express.json() middleware to parse JSON data
app.use("/", feedback);

app.listen(8003, () => {
  console.log("Server is listening on port 8003...");
});
