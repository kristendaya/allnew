const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const mongoose = require("mongoose")
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

// define schema
var taxi_Schema = mongoose.Schema({
    id: Number,
    // pw: String,
    usr: String,
    cartype: String,
    area: String,
    avl: Number
}, {
    versionKey: false
})

//MY SQL > MONGO Insert 위한 Select
function resselect_result(req) {
    const result = connection.query('SELECT * FROM taxitbl where avl = 1 ');
    return result;
}

// create model with mongodb collection and schema
var Taxi = mongoose.model('taxi', taxi_Schema);



// mongo insert
app.get('/mongoinsert', function (req, res) {
    let result = resselect_result(req)
    let flag = 0

    for (var i = 0; i < result.length; i++) {
        var id = result[i].id;
        var usr = result[i].usr;
        var cartype = result[i].cartype;
        var area = result[i].area;
        var avl = result[i].avl;

        // var taxi = new Taxi({ 'id': id, 'usr': usr, 'cartype': cartype, 'area': area, 'avl': avl })

        console.log(Taxi)

        Taxi.save(function (err, silence) {
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
        res.send({ "ok": false, "result": [Taxi], "service": "mongoinsert" });
    } else {
        // res.status(200).send("Inserted")
        res.send({ "ok": true, "result": [Taxi], "service": "mongoinsert" });
    }

});

// list
app.get('/list', function (req, res, next) {
    Taxi.find({}, function (err, docs) {
        if (err) console.log('err')
        // res.send(docs)
        let template = `
        <html>
          <head>
            <title>Taxi Availability</title>
            <meta charset="utf-8">
            <style>
              table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
              }
              th, td {
                padding: 10px;
                text-align: left;
              }
              th {
                background-color: #4CAF50;
                color: white;
              }
            </style>
          </head>
          <body>
            <h1>Taxi Availability</h1>
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Driver Name</th>
                  <th>Car Type</th>
                  <th>Area</th>
                  <th>Availability</th>
                </tr>
              </thead>
              <tbody>
                ${docs.map((taxi) => `
                  <tr>
                    <td>${taxi.id}</td>
                    <td>${taxi.usr}</td>
                    <td>${taxi.cartype}</td>
                    <td>${taxi.area}</td>
                    <td>${taxi.avl}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </body>
        </html>
      `;

        res.send(template);


    })
})

// app.get('/avltaxiids', function (req, res) {
//     Taxi.find({ avl: 1 }, { _id: 0, id: 1, usr: 1, cartype: 1, area: 1, avl: 1 }, function (err, docs) {
//         if (err) {
//             console.error(err);
//             res.status(404).send({ error: '에러입니다!' });
//         } else {
//             let taxis = [];
//             for (let i = 0; i < docs.length; i++) {
//                 taxis.push(docs[i]);
//             }
//         let template = `
//     <html>
//       <head>
//         <title>Taxi Availability</title>
//         <meta charset="utf-8">
//         <style>
//           table, th, td {
//             border: 1px solid black;
//             border-collapse: collapse;
//           }
//           th, td {
//             padding: 10px;
//             text-align: left;
//           }
//           th {
//             background-color: #4CAF50;
//             color: white;
//           }
//         </style>
//       </head>
//       <body>
//         <h1>Taxi Availability</h1>
//         <table>
//           <thead>
//             <tr>
//               <th>ID</th>
//               <th>Driver Name</th>
//               <th>Car Type</th>
//               <th>Area</th>
//               <th>Availability</th>
//             </tr>
//           </thead>
//           <tbody>
//             ${taxis.map((taxi) => `
//               <tr>
//                 <td>${taxi.id}</td>
//                 <td>${taxi.usr}</td>
//                 <td>${taxi.cartype}</td>
//                 <td>${taxi.area}</td>
//                 <td>${taxi.avl}</td>
//               </tr>
//             `).join('')}
//           </tbody>
//         </table>
//       </body>
//     </html>
//   `;

//         res.send(template);
//         }
//     });
// });
// res.render('table.html', { taxis: taxis });
// res.send({ "ok": true, "job": "availability 확인! 1일경우 사용가능", taxis: taxis });



//nodata 
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



//로그인
app.post('/taxi_login', (req, res) => {
    const { id, pw } = req.body;
    const result = connection.query("select * from taxitbl where id=? and pw=?", [id, pw]);
    // res.send(result.User_ID);
    if (result.length == 0) {
        res.redirect('error.html');
    }
    if (id == '01031145933' || id == '01010041004') {
        res.redirect('check.html?id=' + id);
    } else {
        console.log(id + " => User Logined")
        res.redirect('afterlogin.html?id=' + id)
        // res.send({ 'ok': true, 'id': id, 'pw': pw, 'job': 'login' })
    }
});



//register
app.post('/taxi_register', (req, res) => {
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
            <div>c
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
            // res.send({ 'ok': true, 'id': id, 'pw': pw, 'usr': usr, 'cartype': cartype, 'area': area, 'availability': avl, 'job': '가입이완료되었습니다.' });
            res.redirect('index.html');
        }
    }
})


// 관리자 페이지 


// request O, query X
app.get('/select', (req, res) => {
    const result = connection.query('select * from taxitbl');
    console.log(result);
    // res.send({ 'ok': true, 'job': 'select' })
    res.send(result);
})

// request O, query O
app.get('/selectQuery', (req, res) => {
    const id = req.query.id;
    const result = connection.query("select * from taxitbl where id=?", [id]);
    console.log(result);
    res.send(result)
    // res.send({ 'ok': true, 'user': id, 'job': 'select' })
    // res.send(result);
})

// request O, query O
// app.post('/selectQuery', (req, res) => {
//     const id = req.body.id;
//     // console.log(req.body);
//     const result = connection.query("select * from taxitbl where id=?", [id]);
//     console.log(result);
//     res.send(result);
// })

// request O, query O
app.post('/insert', (req, res) => {
    const { id, pw, usr, cartype, area, avl } = req.body;
    const result = connection.query("insert into taxitbl values (?,?,?,?,?,?)", [id, pw, usr, cartype, area, avl]);
    console.log(result);
    res.send({ 'ok': true, 'user': id, 'job': 'insert' })
    res.redirect('/selectQuery?id=' + req.body.id);
})

app.post('/update', (req, res) => {
    const { id, pw, usr, cartype, area, avl } = req.body;
    if (id == "") {
        res.send('User-id를 입력하세요.')
    } else {
        const result = connection.query("select * from taxitbl where id=?", [id]);
        console.log(result);
        // res.send(result);
        if (result.length == 0) {
            template_nodata(res)
        } else {
            const result = connection.query("update taxitbl set pw=?, usr=?, cartype=?, area=?,avl=? where id=?", [pw, usr, cartype, area, avl, id]);
            console.log(result);
            res.send({ 'ok': true, 'mobile': id, 'pw': pw, 'usr': usr, 'cartype': cartype, 'area': area, 'job': 'update' })
            // res.redirect('/select');
        }
    }
})


// // request O, query O
// app.post('/update', (req, res) => {
//     const { id, pw, usr, cartype, area, avl } = req.body;
//     const result = connection.query("update taxitbl set pw=?, usr=?, cartype=?, area=?,avl=? where id=?", [pw, usr, cartype, area, avl, id]);
//     console.log(result);
//     res.send({ 'ok': true, 'mobile': id, 'pw': pw, 'usr': usr, 'cartype': cartype, 'area': area, 'job': 'update' })
//     res.redirect('/selectQuery?id=' + req.body.id);
// })

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




module.exports = app;