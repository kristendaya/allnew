const fs = require('fs')
const env = require('dotenv').config({ path: "../../.env"});

const AWS = require('aws-sdk');
const ID = process.env.ID;
const SECRET = process.env.SECRET;
const BUCKET_NAME = 'lee-5933';
const MYREGION = 'ap-northeast-2'
const s3 = new AWS.S3({accessKeyID : ID, secretAccessKey: SECRET, region: MYREGION});

const uploadFile = (fileName) => {
    const fileContent = fs.readFileSync(fileName);
    const params ={
        Bucket : BUCKET_NAME,
        Key : 'axios.png',
        Body : fileContent
    };
    s3.upload(params, function(err, data) {
        if(err) {throw err;}
        console.log('File uploaded sucessfully. ${data.Location}')
    });
};
uploadFile('axios.png');