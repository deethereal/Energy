const app = require("express")();
const express = require("express")
const http = require("http");
const fs = require("fs");
const multer = require("multer")
const upload = multer({ dest: 'uploads/' });
const path = require("path")
const exec = require("child_process");


app.use(express.static(__dirname + '/WebApp'));

app.listen(3000, () => {
    console.log("Listening on port 3000!");
} );

app.get('/file', (req,res) => {
    // console.log(req)
    console.log('im here')
    res.sendFile(__dirname + '/test.json')
})

app.get('/', function (req, res){
    res.sendFile('index.html');
})

app.post('/', upload.single('file'), (req, res) => {
    console.log("got data!")
    console.log(req.file);
    let file = fs.readFileSync(__dirname + '/' + req.file.path)
    fs.writeFileSync("tmp.csv", file);
    exec.execFileSync("process.py", ['tmp.csv'])
    res.status(200).sendFile(__dirname + '/WebApp/success.html');
})



function deleteFiles_in_dir (dir){
    let files = fs.readdirSync(dir);
    for (const file of files) {
        fs.unlink(path.join(dir, file), err => {
            if (err) throw err;
        });
    }
}