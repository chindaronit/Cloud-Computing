const express = require("express");
const app = express();
const message = require("./routes/message");

// Setup static middleware to serve static files from the "public" directory
app.use(express.static("public"));
app.use(express.urlencoded({ extended: false }));
app.use(express.json()); // Use express.json() middleware to parse JSON data
app.use("/", message);

app.listen(8002, () => {
  console.log("Server is listening on port 8002...");
});
