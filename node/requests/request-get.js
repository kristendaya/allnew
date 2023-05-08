const express = require("express");
const https = require("https");
const request = require('request');
const app = express();


app.get('/hello', (req, res) => {
    res.send("Hello World - Lee");
})

option = "http://192.168.1.18:8000/hello"
app.get("/rhello", function (req, res) {
    request(option, { json: true }, (err, result, body) => {
        if (err) { return console.log(err) }
        res.send(CircularJSON.strionify(body))
    })
})


const data = JSON.stringify({ todo: 'Buy the milk -Lee' })
app.get("/data", function (req, res) {
    res.send(data)
})

option = "http://192.168.1.18:8000/data"
app.get("/rdat", function (req, res) {
    request(option, { json: true }, (err, result, body) => {
        if (err) { return console.log(err) }
        res.send(CircularJSON.strionify(body))
    })
})


app.listen(8000, function () {
    console.log("8000 Port : Server Started…");
});