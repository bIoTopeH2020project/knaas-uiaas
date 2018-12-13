var fs = require('fs');
var _ = require('underscore');
var express = require("express");
var myParser = require("body-parser");
var app = express();
var pp= 3;
console.log(pp);

app.use(myParser.urlencoded({extended : true}));

       app.use(function(req, res, next) {
            res.setHeader('Access-Control-Allow-Origin', '*');
            res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
            res.setHeader('Access-Control-Allow-Headers', "Origin, X-Requested-With, Content-Type, Accept");
            res.setHeader('Access-Control-Allow-Credentials', true);
            next();
         });
       app.post('/', function(request, response) {
       
       var location= './storage/'
       var text=JSON.stringify(request.body)
       var start_pos = text.indexOf('m') + 5 ;
       var end_pos = text.indexOf('"',start_pos) ;
       var title = text.substring(start_pos,end_pos);
       var contents
          fs.readFile(location + title + ".py", 'utf8', function(err, contents) {        
          response.send(contents); 
          });
       

       });


   
app.listen(8090);
