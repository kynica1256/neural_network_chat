const axios = require('axios');

const { base64encode, base64decode } = require('nodejs-base64');
const childProcess = require('child_process');




const express = require('express')
const bodyParser = require('body-parser')
const app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))




let id_col = {};


app.post('/', (req, res) => {
    let data = req.body;
    let id_ = data.id;
    let text_ = data.str;
    let result_ = childProcess.execSync(`cd ../distributor/out && java -classpath .:../lib/* com.Distributorstart ${id_} "${text_}" predict`).toString();
    if ( typeof id_col[id_] === 'undefined' ) {
    	id_col[id_] = 1;
    } else {
        id_col[id_]++;
        console.log(id_col);
        if ( id_col[id_] === 5  ) {
            childProcess.execSync(`cd ../distributor/out && java -classpath .:../lib/* com.Distributorstart ${id_} " " train > /dev/null 2>&1 &`)
	}
    }
    console.log(id_col);
    res.send(result_);
})





var server = app.listen(8000,"127.0.0.1",function (){
  var host = server.address().address;
  var port = server.address().port;
  console.log("listening on http://%s:%s",host,port);
})

