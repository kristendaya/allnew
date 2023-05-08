//MY SQL > MONGO Insert 위한 Select
function resselect_result(req) {
    const result = connection.query('SELECT * FROM taxitbl');
    return result;
}

// define schema
var taxiSchema = mongoose.Schema({
    id: Number,
    pw: String,
    usr: String,
    cartype: String,
    area: String,
    avl: Number
})

// create model with mongodb collection and schema
var Restbls = mongoose.model('restbls', restblSchema);


// mongo insert
app.post('/mongoinsert', function (req, res) {
    let result = resselect_result(req)
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
        res.send({ "ok": true, "result": [result], "service": "mongoinsert" });
    } else {
        // res.status(200).send("Inserted")
        res.send({ "ok": true, "result": [result], "service": "mongoinsert" });
    }

})