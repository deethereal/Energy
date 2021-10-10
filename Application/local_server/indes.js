const app = require("express")();
const express = require("express")
const http = require("http");
const fs = require("fs");
const multer = require("multer")
const upload = multer({ dest: 'uploads/' });
const path = require("path")
const exec = require("child_process");
const {json} = require("express");
const stringify = require('csv-stringify');
const { parse } = require('json2csv');


app.use(express.static(__dirname + '/WebApp'));

app.use(express.urlencoded());

app.listen(3000, () => {
    console.log("Listening on port 3000!");
} );

app.get('/WebApp', (req,res) => {
    // console.log(req)
    console.log('im here');
    res.status(200);
    res.sendFile(__dirname + '/WebApp/result.json')
})

app.post('/WebApp', (req,res) => {
    let str = ['QGRS_1','QGRS_2','QPlant_1','QPlant_2','QPlant_3','QPlant_4','PGRS_1','PGRS_2','P_1','P_2','P_3','P_4','P_5','P_6','P_7','P_8','P_9','Q_1','Q_2','Q_3','Q_4','Q_5','Q_6','Q_7','Q_8'];
    let opts = {str};
    console.log("got data!")
    console.log(JSON.stringify(req.body));
    let Json = req.body;
    let resJ = {}
    console.log(Json)
    str.forEach(item => {
        resJ[item] = parseFloat(Json[item])
    })
    let csvData = parse(resJ,opts)
    console.log(csvData)
    // console.log(resJ)
    fs.writeFileSync("tmp.json", JSON.stringify(resJ));
    exec.execSync("python3 process.py tmp.json 1");

    res.status(200).sendFile(__dirname + '/WebApp/success.html');
})

app.get('/', function (req, res){
    res.sendFile('index.html');
})

app.post('/', upload.single('file'), (req, res) => {
    console.log("got data!")
    console.log(req.file);
    let file = fs.readFileSync(__dirname + '/' + req.file.path)
    fs.writeFileSync("tmp.csv", file);
    exec.execSync("python3 process.py tmp.csv 0");
    res.status(200).sendFile(__dirname + '/WebApp/success_file.html');
})

app.get('/file', (req, res) => {
    console.log('im here');
    res.sendFile(__dirname + '/WebApp/result.json')
})



function deleteFiles_in_dir (dir){
    let files = fs.readdirSync(dir);
    for (const file of files) {
        fs.unlink(path.join(dir, file), err => {
            if (err) throw err;
        });
    }
}