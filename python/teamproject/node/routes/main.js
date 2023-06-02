const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });
const axios = require('axios')
const app = express();


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// app.get('/hello', (req, res) => {
//     res.send('Hello World~!!');
// });

// app.get('/dropmongo', (req, res) => {
//     axios
//         .get('http://192.168.1.10:3000/dropdata')
//         .then(response => {
//             console.log('statusCode:', response.status);
//             console.log(response.data);
//             res.send(response.data);
//         })
//         .catch(error => {
//             console.log(error);
//         });
// });


// app.get('/insertmongo', (req, res) => {
//     axios
//         .get('http://192.168.1.10:3000/insert_data')
//         .then(response => {
//             console.log('statusCode:', response.status);
//             console.log(response.data);
//             res.send(response.data);
//         })
//         .catch(error => {
//             console.log(error);
//         });
// });

app.get('/getdata', (req, res) => {
    const start = req.query.start;
    const end = req.query.end;
    axios
        .get(`http://192.168.1.10:3000/getdata?start=${start}&end=${end}`)
        .then(response => {
            console.log('statusCode:', response.status);
            console.log(response.data);
            res.send(response.data);
        })
        .catch(error => {
            console.log(error);
        });
});


app.get('/graph_by_date', (req, res) => {
    const start = req.query.start;
    const end = req.query.end;
    console.log(start, end)
    axios
        .get(`http://192.168.1.10:3000/graph_data_by_date?start=${start}&end=${end}`)
        .then(response => {
            console.log('statusCode:', response.status);
            console.log(response.data);
            res.send(response.data);
        })
        .catch(error => {
            // console.log(error);
        });
});

app.get('/get_gra_by_nationality', (req, res) => {
    const nationality = req.query.nationality;

    axios
        .get(`http://192.168.1.10:3000/get_gra_by_nationality?nationality=${nationality}`)
        .then(response => {
            console.log('statusCode:', response.status);
            console.log(response.data);
            res.send(response.data);
        })
        .catch(error => {
            console.log(error);
        });
});

app.get('/get_top', (req, res) => {
    const start = req.query.start;
    const end = req.query.end;

    axios
        .get(`http://192.168.1.10:3000/get_top?start=${start}&end=${end}`)
        .then(response => {
            console.log('statusCode:', response.status);
            console.log(response.data);
            res.send(response.data);
        })
        .catch(error => {
            console.log(error);
        });
});




// app.listen(5000, () => {
//     console.log('Server is running on port 5000');
// });


module.exports = app;