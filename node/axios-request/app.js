const axios = require('axios');

axios
    .post('http://192.168.1.18:8000/todos', {
        todo: "Buy a bottle of water"
    })
    .then(res => {
        console.log('statusCode : ${res.status}')
        console.log(res)
    })
    .catch(error => {
        console.log(eroor)
    })