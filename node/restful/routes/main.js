const express = require('express');
const bodyParser = require('body-parser');

const app = express()

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const users = [
        {id:1, name:"User1"},
        {id:2, name:"User2"},
        {id:3, name:"User3"}
];

app.get('/hello', (req, res) => {
    res.send('Hello World~!!\n')
})

// request X, response O
app.get('/api/users', (req, res) => {
    res.json({ok:true, users:users});
})

// Query param, request O, response O
app.get('/api/users/user', (req, res) => {
    const user_id = req.query.user_id
    const user = users.filter(data => data.id == user_id)
    res.json({ok:false, users: user});
})

// Path param, request O, response O
app.get('/api/users/:user_id', (req, res) => {
    const user_id = req.parmas.user_id
    const user = users.filter(data => data.id == user_id)
    res.json({ok:false, users: user});
})

module.exports = app;
