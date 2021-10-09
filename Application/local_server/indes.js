const app = require("express")();
const express = require("express")
const http = require("http");
const fs = require("fs");

app.use(express.static('WebApp'));

app.listen(3000, () => {
    console.log("Listening on port 3000!");
} );

app.get('/', function (req, res){
    res.sendFile('index.html');
})