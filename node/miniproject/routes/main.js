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


//로그인
app.post('/login', (req, res) => {
    const { id, pw } = req.body;
    const result = connection.query("select * from taxitbl where id=? and pw=?", [id, pw]);
    // res.send(result.User_ID);
    if (result.length == 0) {
        res.send({ 'ok': false })
    }
    if (id == 'admin' || id == 'root') {
        res.send({ 'ok': false })
    } else {
        res.send({ 'ok': true })
    }
});



//register
app.post('/register', (req, res) => {
    const { id, pw, usr, cartype, area, avl } = req.body;
    if (id == "") {
        res.redirect('register.html')
    } else {
        let result = connection.query("select * from taxitbl where id=?", [id]);
        if (result.length > 0) {
            res.writeHead(200);
            var template = `
        <!doctype html>
        <html>
        <head>
            <title>Error</title>
            <meta charset="utf-8">
        </head>
        <body>
            <div>
                <h3 style="margin-left: 30px">Registrer Failed</h3>
                <h4 style="margin-left: 30px">이미 존재하는 아이디입니다.</h4>
                <a href="register.html" style="margin-left: 30px">다시 시도하기</a>
            </div>
        </body>
        </html>
        `;
            res.end(template);
        } else {
            result = connection.query("insert into taxitbl values (?,?,?,?,?,?)", [id, pw, usr, cartype, area, avl]);
            console.log(result);
            res.send(result);
        }
    }
})



// request O, query X
app.get('/select', (req, res) => {
    const result = connection.query('select * from taxitbl');
    console.log(result);
    res.send({ 'ok': true, 'job': 'select' })
    // res.send(result);
})

// request O, query O
app.get('/selectQuery', (req, res) => {
    const id = req.query.id;
    const result = connection.query("select * from taxitbl where id=?", [id]);
    console.log(result);
    res.send({ 'ok': true, 'user': id, 'job': 'select' })
    // res.send(result);
})

// request O, query O
app.post('/selectQuery', (req, res) => {
    const id = req.body.id;
    // console.log(req.body);
    const result = connection.query("select * from taxitbl where id=?", [id]);
    console.log(result);
    res.send(result);
})

// request O, query O
app.post('/insert', (req, res) => {
    const { id, pw, usr, cartype, area, avl } = req.body;
    const result = connection.query("insert into taxitbl values (?,?,?,?,?,?)", [id, pw, usr, cartype, area, avl]);
    console.log(result);
    res.send({ 'ok': true, 'user': id, 'job': 'insert' })
    res.redirect('/selectQuery?id=' + req.body.id);
})

// request O, query O
app.post('/update', (req, res) => {
    const { id, pw, cartype, area } = req.body;
    const result = connection.query("update taxitbl set pw=?, cartype=?, area=? where id=?", [id, pw, cartype, area]);
    console.log(result);
    res.send({ 'ok': true, 'user': id, 'job': 'update' })
    res.redirect('/selectQuery?id=' + req.body.id);
})

// request O, query O
app.post('/delete', (req, res) => {
    const id = req.body.id;
    if (id == "") {
        res.send('User-id를 입력하세요.')
    } else {
        const result = connection.query("select * from taxitbl where id=?", [id]);
        console.log(result);
        // res.send(result);
        if (result.length == 0) {
            template_nodata(res)
        } else {
            const result = connection.query("delete from taxitbl where id=?", [id]);
            console.log(result);
            res.send({ 'ok': true, 'user': id, 'job': 'delete' })
            // res.redirect('/select');

        }
    }
})

// request O, query O
app.put('/toggle/:id', (req, res) => {
    const id = req.params.id;
    let result = connection.query("select * from taxitbl where id=?", [id]);
    console.log(result);
    if (result.length == 0) {
        // template_nodata(res)
    } else {
        const avl = result[0].avl === 1 ? 0 : 1; // availability 값을 토글
        result = connection.query("update taxitbl set avl=? where id=?", [avl, id]); // 첫 번째 result와 동일한 변수에 할당
        console.log(result);
        res.send({ 'ok': true, 'user': id, 'job': 'toggle availability' })
    }
})


module.exports = app;