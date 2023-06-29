const axios = require('axios');

axios 
    .post('https://example.com/todos',{
        todo : "Buy the milk"
        })
        .then(res => {
            console.log(`statusCoide : ${res.statusCode}`)
            console.log(res)
        })
        .caatch(error => {
            console.error(error)

        })