const https = require("https");

const data = JSON.stringify({
    todo: 'Buy the milk'
})

const options = {
    hostname: '192.168.1.18',
    port: '8000',
    path: '/todos',
    method: 'POST',
    header: {
        'Content-Type': 'application/'josn' , 
        'Content-Length' : data.Length

    }
}

const req = https.request(options, res => {
    console.log('statusCode : ${res.statusCode}');
    res.on

}