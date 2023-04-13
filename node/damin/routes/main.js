const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    password: process.env.password,
    database: process.env.database
});

const app = express()

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.get('/select', (req, res) => {
    const result = connection.query('select * from UserTbl');
    console.log(result);
    res.send(result);
})

// request O, query O
app.get('/selectQuery', (req, res) => {
    const id = req.query.userid;
    // console.log("이건 id 값이에요: " + id);
    // console.log("select * from UserTbl where userid="+id);
    console.log(id);
    const result = connection.query("select * from UserTbl where userid=?", [id]);
    console.log(result);
    res.send(result);
})

// request O, query O
app.post('/selectQuery', (req, res) => {
    const id = req.body.userid;
    
    const result = connection.query("select * from UserTbl where userid=?", [id]);
    console.log(result);
    res.send(result);
})

// request O, query O
app.post('/insert', (req, res) => {
    const { id, name,addr,favor } = req.body;
    // console.log(id+name+addr+favor)
    const result = connection.query("insert into UserTbl values (?,?,?,?)", [id,name,addr,favor]);
    console.log(result);
    res.redirect('/selectQuery?userid=' + req.body.id);
})

// request O, query O
app.post('/update', (req, res) => {
    const { id,name,addr,favor} = req.body;
    const result = connection.query("update UserTbl set name=?,addr=?,favor=? where Userid=?", [name,addr,favor,id]);
    console.log(result);
    res.redirect('/selectQuery?userid=' + req.body.id);
})

// request O, query O
app.post('/delete', (req, res) => {
    const id= req.body.id;
    const result = connection.query("delete from UserTbl where userid=?", [id]);
    console.log(result);
    res.redirect('/select');
})

module.exports = app;