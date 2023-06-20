'use strict'

var express =require("express");
const app = express()

const HOST='0.0.0.0'
const PORT='8000'

app.get('/',(req,res) => {
	res.send('Hello World\n');
});

app.listen(PORT, HOST) ;
console.log('Sever runing at http://${HOST}:${PORT}/');




