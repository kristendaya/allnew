const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const mongoose = require("mongoose");
const env = require('dotenv').config({ path: "../../.env" });

//MySQL 연결 정보
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

//MY SQL > MONGO Insert 위한 Select
function resselect_result(req) {
    const result = connection.query('SELECT * FROM restbl');
    return result;
}

function template_nodata(res) {
    res.writeHead(200);
    var template = `
    <!doctype html>
    <html>
    <head>
        <title>Result</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h3>데이터가 존재하지 않습니다.</h3>
    </body>
    </html>
    `;
    res.end(template);
}

function template_result2(result, res) {
    res.writeHead(200);
    var template = `
    <!doctype html>
    <html>
    <head>
        <title>Result</title>
        <meta charset="utf-8">
        <link type="text/css" rel="stylesheet" href="mystyle.css" />
    </head>
    <body>
    <table border="1" style="margin:auto;">
    <thead>
        <tr><th>shopId</th><th>shopService</th><th>shopName</th><th>shopArea</th><th>shopAddr</th></tr>
    </thead>
    <tbody>
    `;
    for (var i = 0; i < result.length; i++) {
        template += `
    <tr>
        <td>${result[i]['shopId']}</td>
        <td>${result[i]['shopService']}</td>
        <td>${result[i]['shopName']}</td>
        <td>${result[i]['shopArea']}</td>
        <td>${result[i]['shopAddr']}</td>
    </tr>
    `;
    }
    template += `
    </tbody>
    </table>
    </body>
    </html>
    `;
    res.end(template);
}

function template_result3(result, res) {
    res.writeHead(200);
    var template = `
    <!doctype html>
    <html>
    <head>
        <title>Result</title>
        <meta charset="utf-8">
        <link type="text/css" rel="stylesheet" href="mystyle.css" />
    </head>
    <body>
    <table border="1" style="margin:auto;">
    <thead>
        <tr><th>resNumber</th><th>userId</th><th>shopName</th><th>resDate</th><th>shopService</th><th>shopArea</th></tr>
    </thead>
    <tbody>
    `;
    for (var i = 0; i < result.length; i++) {
        template += `
    <tr>
        <td>${result[i]['resNumber']}</td>
        <td>${result[i]['userId']}</td>
        <td>${result[i]['shopName']}</td>
        <td>${result[i]['resDate']}</td>
        <td>${result[i]['shopService']}</td>
        <td>${result[i]['shopArea']}</td>
    </tr>
    `;
    }
    template += `
    </tbody>
    </table>
    </body>
    </html>
    `;
    res.end(template);
}

// 로그인
app.post('/login', (req, res) => {
    const { id, pw } = req.body;
    const usertbl = connection.query("select * from usertbl where userid=? and passwd=?", [id, pw]);
    // console.log(usertbl);
    if (usertbl.length == 0) {
        res.redirect('error.html')
    }
    if (id == 'admin' || id == 'root') {
        console.log(id + " => Administrator Logined")
        // res.redirect('member.html?id=' + id)
        res.send({ "ok": true, "userid": [id], "service": "Admin login" });
    } else {
        console.log(id + " => User Logined")
        // res.redirect('main.html?id=' + id)
        res.send({ "ok": true, "userid": [id], "service": "User login" });
    }
})

// 회원가입 
app.post('/register', (req, res) => {
    const { id, pw, name, addr, num } = req.body;
    if (id == "") {
        res.redirect('register.html')
    } else {
        let usertbl = connection.query("select * from usertbl where userid=? and passwd=? and userName=? and userAddr=? and userNumber=?", [id, pw, name, addr, num]);
        if (usertbl.length > 0) {
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
            usertbl = connection.query("insert into usertbl values (?, ?, ?, ?, ?)", [id, pw, name, addr, num]);
            console.log(usertbl);
            res.send({ "ok": true, "usertbl": [{ "id": id, "pw": pw, "name": name, "addr": addr, "num": num }], "service": "register" });
            // res.redirect('/');
        }
    }
})


//SelectDong ' 동 (Area) ' 에 따른 Shop 조회
app.get('/selectDong', (req, res) => {
    const shopArea = req.query.shopArea;
    if (shopArea == "") {
        // res.send('원하는 동을 입력하세요.')
        res.write("<script>alert('원하는 동을 입력하세요')</script>");
    } else {
        const shoptbl = connection.query("SELECT * FROM shoptbl where shopArea=?", [shopArea]);
        console.log(shoptbl);
        // res.send(shoptbl);
        if (shoptbl.length == 0) {
            // template_nodata(res);
            res.send({ "ok": false, "shopArea": [shopArea], "service": "SelectDong" });
        } else {
            // template_result2(result, res);
            res.send({ "ok": true, "shopArea": [shopArea], "service": "SelectDong" });
        }
    }
})

// 전체 업체 검색
app.get('/select', (req, res) => {
    const shoptbl = connection.query('SELECT * FROM shoptbl');
    console.log(shoptbl);
    //res.send('{"ok":true, "affectedRows":' + shoptbl.affectedRows + ', "service":"insert"}');
    // res.send(shoptbl);
    if (shoptbl.length == 0) {
        // template_nodata(res);
        res.send({ "ok": false, "shoptbl": [shoptbl], "service": "select" });
    } else {
        // template_result2(result, res);
        res.send({ "ok": true, "shoptbl": [shoptbl], "service": "select" });
    }

})

// 예약 등록 
app.post('/insert', (req, res) => {
    const { resNumber, userId, shopName, resDate, shopService, shopArea } = req.body;
    if (resNumber == "" || userId == "" || shopName == "" || resDate == "" || shopService == "" || shopArea == "") {
        // res.send('정보를 빠짐없이 입력하세요.')
        res.write({ "ok": false, "restbl": [restbl], "service": "Reservation" });
    } else {
        let restbl = connection.query("select * from restbl where resNumber=?", [resNumber]);
        if (restbl.length > 0) {
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
            </div>
        </body>
        </html>
        `;
            res.end(template);
        } else {
            restbl = connection.query("insert into restbl values (?, ?, ?, ?, ?, ?)", [resNumber, userId, shopName, resDate, shopService, shopArea]);
            console.log(restbl);
            // res.redirect('/selectQuery?resNumber=' + req.body.resNumber);
            res.send({ "ok": true, "restbl": [{ "resNumber": resNumber, "userID": userId, "shopName": shopName, "resDate": resDate, "shopService": shopService, "shopArea": shopArea }], "service": "Reservation" });
        }
    }
})

// ReservationSelect (예약 정보 출력)
app.get('/select2', (req, res) => {
    const restbl = connection.query('SELECT * FROM restbl');
    console.log(restbl);
    // res.send(restbl);
    if (restbl.length == 0) {
        // template_nodata(res);
        res.send({ "ok": false, "restbl": [restbl], "service": "ReservationSelect" });
    } else {
        // template_result3(restbl, res);
        res.send({ "ok": true, "restbl": [restbl], "service": "ReservationSelect" });
    }
})

// define schema
var restblSchema = mongoose.Schema({
    resNumber: Number,
    userId: String,
    shopName: String,
    resDate: String,
    shopService: String,
    shopArea: String
})

// create model with mongodb collection and schema
var Restbls = mongoose.model('restbls', restblSchema);


// mongo insert
app.post('/mongoinsert', function (req, res) {
    let result = resselect_result(req)
    //상위에 지정한 My SQL > Mongo로 이동하는 Function 이므로 result로 변수 선언
    let flag = 0

    for (var i = 0; i < result.length; i++) {
        var resNumber = result[i].resNumber;
        var userId = result[i].userId;
        var shopName = result[i].shopName;
        var resDate = result[i].resDate;
        var shopService = result[i].shopService;
        var shopArea = result[i].shopArea;

        var restbls = new Restbls({ 'resNumber': resNumber, 'userId': userId, 'shopName': shopName, 'resDate': resDate, 'shopService': shopService, 'shopArea': shopArea })

        restbls.save(function (err, silence) {
            if (err) {
                flag = 1;
                return;
            }
        })
        if (flag) break;
    }
    if (flag) {
        console.log('err')
        // res.status(500).send('insert error')
        res.send({ "ok": false, "mongoinsert": [restbls], "service": "mongoinsert" });
    } else {
        // res.status(200).send("Inserted")
        res.send({ "ok": true, "mongoinsert": [restbls], "service": "mongoinsert" });
    }

})

// list
app.get('/mongolist', function (req, res, next) {
    Restbls.find({}, function (err, mongolist) {
        if (err) console.log('err')
        res.send({ "ok": true, "mongolist": [_id = 0, mongolist], "service": "mongoinsert" })

    })
})

// update
app.post('/mongoupdate', function (req, res, next) {
    var resNumber = req.body.resNumber;
    var userId = req.body.userId;
    var shopName = req.body.shopName;
    var resDate = req.body.resDate;
    var shopService = req.body.shopService;
    var shopArea = req.body.shopArea;

    Restbls.findOne({ 'resNumber': resNumber }, function (err, restbl) {
        if (err) {
            console.log('err')
            // res.status(500).send('update error')
            res.status(500).send({ "ok": false, "rstbl": [_id = 0, restbl], "service": "mongoupdate" })
            return;
        }
        restbl.userId = userId;
        restbl.shopName = shopName;
        restbl.resDate = resDate;
        restbl.shopService = shopService;
        restbl.shopArea = shopArea;

        restbl.save(function (err, silence) {
            if (err) {
                console.log('err')
                res.status(500).send({ "ok": false, "rstbl": [_id = 0, restbl], "service": "mongoupdate" })
                return;
            }
            // res.status(200).send("Updated")
            res.status(200).send({ "ok": true, "rstbl": [_id = 0, restbl], "service": "mongoupdate" })

        })
    })
})

// delete
app.post('/mongodelete', function (req, res, next) {
    var resNumber = req.body.resNumber;

    var restbls = Restbls.find({ 'resNumber': resNumber })
    restbls.remove(function (err) {
        if (err) {
            console.log('err')
            res.status(500).send({ "ok": false, "service": "mongodelete" })
            return;
        }
        // res.status(200).send("Removed")
        res.status(200).send({ "ok": true, "service": "mongodelete" })
    })
})

module.exports = app;