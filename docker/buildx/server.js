var http = require("http");

const hostname='0.0.0.0'
const port='8000'

const server = http.createServer(function (req,res){
    res.statusCode=200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello from NodeJS in ${process.arch}!\n');
});

server.listen(port, hostnmae, () => {
	console.log('Sever runing at http://${hostnmae}:${port}/');
});




