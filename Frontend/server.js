const express = require("express");
const app = express();
const port = process.env.PORT || 5000;
const bodyParser = require("body-parser");
const path = require("path");

// use body parser middleware
app.use(bodyParser.json());

// get routes
app.get("/express_backend", (req, res) => {
  res.send({express: "express backend is connected to react"});
})

app.listen(port, () => console.log("listening to port " + port))