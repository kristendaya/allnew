//mongoose: MongoDB 객체 모델링 도구입니다.
//sync-mysql: Node.js용 동기식 MySQL 클라이언트입니다
//async: 여러 가지 비동기 제어 흐름 함수를 제공하는 유틸리티 모듈입니다.
const express = require("express")
const app = express()
const mongoose = require("mongoose")
const mysql = require("sync-mysql");
const bodyParser = require("body-parser");
const env = require("dotenv").config({ path: "../../.env" });
const query = require("async");

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    password: process.env.password,
    database: process.env.database
});

// define schema
var new_clothes_Schema = mongoose.Schema({
    cloth_name: String,
    category: String
}, {
    versionKey: false
})

var new_places_Schema = mongoose.Schema({
    place_name: String,
    type: String,
    location: String
}, {
    versionKey: false
})

var rec_places_Schema = mongoose.Schema({
    location: String,
    date: String,
    place_name: String
}, {
    versionKey: false
})

// create model with mongodb collection and schema
var New_clohtes = mongoose.model('musinsas', new_clothes_Schema);
var New_places = mongoose.model('agodas', new_places_Schema);
var Rec_places = mongoose.model('rec_places', rec_places_Schema);

// mysql에서 뽑아온 추천 관광지를 mongodb에 바로 저장
///rec_place_insert: 사용자로부터 위치와 날짜를 POST 요청으로 받습니다.
// 이 엔드포인트는 날씨 조건에 따라 추천 여행지를 MySQL 데이터베이스에서 조회한 후, 결과를 MongoDB 데이터베이스에 저장합니다.
app.post('/rec_place_insert', function (req, res, next) {
    const { loc, user_date } = req.body;
    const result = connection.query(
        "SELECT w.location, w.date, p.name AS place_name FROM weather w JOIN places p ON w.location = p.location AND w.temp_min <= p.temp_min WHERE w.location=? AND w.date=?;", [loc, user_date]);
    var location = [];
    var date = [];
    var place_name = [];

    for (let i = 0; i < result.length; i++) {
        location[i] = result[i]['location'];
        date[i] = result[i]['date'];
        place_name[i] = result[i]['place_name'];

        var rec_places = new Rec_places({ 'location': location[i], 'date': date[i], 'place_name': place_name[i] })

        rec_places.save(function (err, silence) {
            if (err) {
                res.status(500).send('insert error')
                res.send('{ "ok": false }');
                console.log('{ "ok": false }');
                return;
            }
        })
    }
    res.status(200)
    res.send('{"ok": true,' + JSON.stringify(result) + ' }');
    console.log('{"ok":true,' + JSON.stringify(result) + ' }');
});


// list
///list: GET 요청을 받고, MongoDB 데이터베이스의 "musinsas" 컬렉션에 있는 모든 문서를 반환합니다.
app.get('/list', function (req, res, next) {
    New_clohtes.find({}, function (err, docs) {
        if (err) console.log('err')
        res.send(docs)
    })
});

// get
///get: "input"이라는 쿼리 파라미터로 사용자 ID를 받는 GET 요청을 받습니다.
// 이 엔드포인트는 MongoDB 데이터베이스의 "users" 컬렉션에서 해당 문서를 조회하여 반환합니다.
app.get('/get', function (req, res, next) {
    var userid = req.query.input
    User.findOne({ 'userid': userid }, function (err, doc) {
        if (err) console.log('err')
        res.send(doc)
    })
});

// new clothes insert from users
///cloth_insert: 사용자로부터 옷 이름과 카테고리를 POST 요청으로 받습니다. 
//이 엔드포인트는 해당 문서를 MongoDB 데이터베이스의 "musinsas" 컬렉션에 저장합니다.
app.post('/cloth_insert', function (req, res, next) {
    var cloth_name = req.body.cloth_name;
    var category = req.body.category;
    var new_clothes = new New_clohtes({ 'cloth_name': cloth_name, 'category': category })

    new_clothes.save(function (err, silence) {
        if (err) {
            console.log('err')
            res.status(500).send('insert error')
            return;
        }
        res.status(200)
        res.redirect('/list')
    })
});

// new places insert from users
///place_insert: 사용자로부터 장소 이름, 유형, 위치를 POST 요청으로 받습니다. 
//이 엔드포인트는 해당 문서를 MongoDB 데이터베이스의 "agodas" 컬렉션에 저장합니다.
app.post('/place_insert', function (req, res, next) {
    var place_name = req.body.place_name;
    var type = req.body.type;
    var location = req.body.location;
    var new_places = new New_places({ 'place_name': place_name, 'type': type, 'location': location })

    new_places.save(function (err, silence) {
        if (err) {
            console.log('err')
            res.status(500).send('insert error')
            return;
        }
        res.status(200)
        res.redirect('/list')
    })
    //res.redirect('/list')
});


// new clothes update from users
///cloth_update: 사용자로부터 옷 이름과 카테고리를 POST 요청으로 받습니다.
// 이 엔드포인트는 MongoDB 데이터베이스의 "musinsas" 컬렉션에서 해당 문서를 업데이트합니다.
app.post('/cloth_update', function (req, res, next) {
    var cloth_name = req.body.cloth_name;
    var category = req.body.category;

    New_clohtes.findOne({ 'cloth_name': cloth_name }, function (err, new_clohtes) {
        if (err) {
            console.log('err')
            res.status(500).send('update error')
            return;
        }
        new_clohtes.cloth_name = cloth_name;
        new_clohtes.category = category;

        new_clohtes.save(function (err, silence) {
            if (err) {
                console.log('err')
                res.status(500).send('update error')
                return;
            }
            res.status(200)
            res.redirect('/list')
        })
    })
});

// new places update
///place_update: 사용자로부터 장소 이름, 유형, 위치를 POST 요청으로 받습니다. 
//이 엔드포인트는 MongoDB 데이터베이스의 "agodas" 컬렉션에서 해당 문서를 업데이트합니다.
app.post('/place_update', function (req, res, next) {
    var place_name = req.body.place_name;
    var type = req.body.type;
    var location = req.body.location;

    New_places.findOne({ 'place_name': place_name }, function (err, new_places) {
        if (err) {
            console.log('err')
            res.status(500).send('update error')
            return;
        }
        new_places.place_name = cloth_name;
        new_places.type = type;
        new_places.location = location;

        new_places.save(function (err, silence) {
            if (err) {
                console.log('err')
                res.status(500).send('update error')
                return;
            }
            res.status(200)
            res.redirect('/list')
        })
    })
});


// clothes delete
app.post('/cloth_delete', function (req, res, next) {
    var cloth_name = req.body.cloth_name;
    var new_clohtes = New_clohtes.find({ 'cloth_name': cloth_name })
    new_clohtes.remove(function (err) {
        if (err) {
            console.log('err')
            res.status(500).send('delete error')
            return;
        }
        res.status(200)
        res.redirect('/list')
    })
});

// delete place
app.post('/places_delete', function (req, res, next) {
    var place_name = req.body.place_name;
    var new_places = New_places.find({ 'place_name': place_name })
    new_places.remove(function (err) {
        if (err) {
            console.log('err')
            res.status(500).send('delete error')
            return;
        }
        res.status(200)
        res.redirect('/list')
    })
});


function show_table(result, res) {
    res.writeHead(200);
    var template = `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="table.css">
        </head>
        <body>
            <table style="margin:auto; text-align:center;">
                <thead>
                    <tr><th>지역</th><th>최저 기온</th><th>최고 기온</th><th>미세 먼지</th><th>강수량</th></tr>
                </thead>
                <tbody>
                `;
    for (var i = 0; i < result.length; i++) {
        template += `
        <tr>
            <td>${result[i]['location']}</td>
            <td>${result[i]['temp_min']}</td>
            <td>${result[i]['temp_max']}</td>
            <td>${result[i]['fine_dust']}</td>
            <td>${result[i]['prec']}</td>
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


/// functions for project

app.get("/select", (req, res) => {
    const result = connection.query("SELECT * FROM places;");
    res.send(result);
});


app.get("/show_wt", (req, res) => {
    //const result = connection.query("SELECT * FROM weather WHERE location = '서울' AND date = '20230313';");
    const result = connection.query("SELECT * FROM weather WHERE date = '20230314';");

    if (result.length == 0) {
        res.send('{ "ok": false }');
        console.log('{ "ok": false }');
    } else {
        show_table(result, res);
        res.send('{"ok": true,' + JSON.stringify(result) + ' }');
        console.log('{"ok":true,' + JSON.stringify(result) + ' }');
    }
});

app.post("/show_wt", (req, res) => {
    const { loc, date } = req.body;
    const result = connection.query("select * from weather WHERE location=? AND date=?;", [loc, date]);

    if (result.length == 0) {
        res.send('{ "ok": false }');
        console.log('{ "ok": false }');
    } else {
        res.send('{"ok": true,' + JSON.stringify(result) + ' }');
        console.log('{"ok":true,' + JSON.stringify(result) + ' }');
    }
});


app.get("/rec_place", (req, res) => {
    const result = connection.query(
        "SELECT w.location, w.date, p.name AS place_name FROM weather w JOIN places p ON w.location = p.location AND w.temp_min <= p.temp_min WHERE w.location = '대전' AND w.date = '20230328'; ");
    console.log(result);
    res.send(result);
});

app.post("/rec_place", (req, res) => {
    const { loc, date } = req.body;
    const result = connection.query(
        "SELECT w.location, w.date, p.name AS place_name FROM weather w JOIN places p ON w.location = p.location AND w.temp_min <= p.temp_min WHERE w.location=? AND w.date=?;", [loc, date]);
    console.log('{"ok":true,' + JSON.stringify(result) + ' }');

    if (result.length == 0) {
        res.send('{ "ok": false }');
    } else {
        res.send('{"ok": true,' + JSON.stringify(result) + ' }');
    }
});


app.get("/rec_cloth", (req, res) => {
    const result = connection.query(
        "SELECT w.location, w.date, c.name AS cloth_name FROM clothes c JOIN weather w ON w.temp_max >= c.temp_max AND w.temp_min >= c.temp_min WHERE w.location = '대구' AND w.date = '20230329'; ");
    console.log(result);
    res.send(result);
});

app.post("/rec_cloth", (req, res) => {
    const { loc, date } = req.body;
    const result = connection.query(
        "SELECT w.location, w.date, c.name AS cloth_name FROM clothes c JOIN weather w ON w.temp_max >= c.temp_max AND w.temp_min >= c.temp_min WHERE w.location = ? AND w.date = ?;", [loc, date]);
    console.log(result);
    res.send(result);
});


app.post("/find_my_cloth", (req, res) => {
    const { now_temp, cloth_category } = req.body;
    const clothes = connection.query("select name, temp_min, temp_max from clothes where category=?", [cloth_category]);
    const mintemp = [];
    const maxtemp = [];
    const result = [];

    console.log(clothes)

    Array.from(clothes).forEach((clothing) => {
        mintemp.push(clothing.temp_min);
        maxtemp.push(clothing.temp_max);
    });

    if (now_temp.length == 0 || cloth_category.length == 0) {
        res.send(
            `<script>
                alert('현재 온도와 원하시는 옷 카테고리를 모두 입력해주세요!');
            </script>`
        );
    } else {
        for (var i = 0; i < clothes.length; i++) {
            if ((maxtemp[i] >= now_temp) && (mintemp[i] <= now_temp)) {
                result.push(clothes[i].name);
            }
        }
        console.log(result);
        res.send(result);
    }
});


module.exports = app;