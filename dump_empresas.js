const fs = require('fs');
const http = require('http');

const empresas_url = "http://www.madrid.org/filmmadrid/data/empresas.min.js";

const js_file = fs.createWriteStream("empresas.js");

const req = http.get(empresas_url, async (res) => {
    let stream = res.pipe(js_file);

    await new Promise(fulfill => stream.on("finish", fulfill));

    fs.appendFileSync('empresas.js', 'exports.empresas = empresas'); // append exports to downloaded file

    const empresas = require('./empresas.js'); // everything inside this callback because I fucking suck at JS :(
    
    const json_empresas = JSON.stringify(empresas.empresas);
    
    fs.writeFileSync("empresas.json", json_empresas);

});
