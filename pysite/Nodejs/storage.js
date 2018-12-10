var fs = require('fs');
var _ = require('underscore');
var express = require("express");
var myParser = require("body-parser");
var app = express();
var pp= 5;
console.log(pp);

app.use(myParser.urlencoded({extended : true}));

          app.use(function(req, res, next) {
          res.setHeader('Access-Control-Allow-Origin', '*');
          res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
          res.setHeader('Access-Control-Allow-Headers', "Origin, X-Requested-With, Content-Type, Accept");
          res.setHeader('Access-Control-Allow-Credentials', true);
          next();
          });
   

          app.post('/endpoint', function(request, response) {
          var location= './storage/'   
          var text=JSON.stringify(request.body)
          var start_pos = text.indexOf('m') + 5 ;
          var end_pos = text.indexOf('"',start_pos) ;
          var title = text.substring(start_pos,end_pos)
          var start_pos2 = text.indexOf(':',end_pos) + 2;
          var end_pos2 = text.lastIndexOf('"');
          var contenido = text.substring(start_pos2,end_pos2);
          var tmpo = contenido.split('\\n');

          var x = tmpo.length
          var final="";
          var almost="";
                for (i = 0; i < x; i++) {

                   almost = final +tmpo[i] + "\r\n";
                   final = almost.replace('\\',"");
                   }
               fs.writeFile( location + title + ".py", final, function(err) {
                   if(err) {
                      return console.log(err);
                           }

           }); 
        

});

app.listen(5080);
