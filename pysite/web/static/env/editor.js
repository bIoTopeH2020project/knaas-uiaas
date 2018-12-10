
$(document).ready(function () {
    var output = $('#edoutput');
    var outf = function (text) {
        output.text(output.text() + text);
    
    };
    
    var jsoutf = function (text) {
        window.js_output=text;
    }
    
    var keymap = {
        "Ctrl-Enter" : function (editor) {
           
            Sk.configure({output: outf, read: builtinRead});
            Sk.canvas = "mycanvas";
            if (editor.getValue().indexOf('turtle') > -1 ) {
                $('#mycanvas').show()
            }
            Sk.pre = "edoutput";
            (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
            try {
                var myPromise = Sk.misceval.asyncToPromise(function() {
                    console.log('entered')
                    return Sk.importMainWithBody("<stdin>",false,editor.getValue(),true);
                });

                   myPromise.then(function(mod) {
		       console.log('success');
		   },
		       function(err) {
                       var pos=err.toString()
		       outf(pos);
		   });
            } catch(e) {
                outf(e.toString() + "\n")
            }
        },
        "Shift-Enter": function (editor) {
            Sk.configure({output: outf, read: builtinRead});
            Sk.canvas = "mycanvas";
            Sk.pre = "edoutput";
            if (editor.getValue().indexOf('turtle') > -1 ) {
                $('#mycanvas').show()
            }
            try {
                Sk.misceval.asyncToPromise(function() {
                    return Sk.importMainWithBody("<stdin>",false,editor.getValue(),true);
                });
            } catch(e) {
                outf(e.toString() + "\n")
            }
        },
        "load": function Load(editor)
	{ 
 
	    var fileNameToLoad = document.getElementById("inputnameload").value;

                       var header = {
                       "Content-Type": "application/json; charset=utf-8",
                       "Accept" : "application/json"
                        };                                           

	               var datas = {};
                       datas.body = {};
                       datas.body.fileName =fileNameToLoad
                                       
					
                       jQuery.ajax({
		       type: 'POST',
		       data: datas,
                       crossDomain:true,
                       url: 'http://localhost:8090/',						
                            success: function(result) {
                            console.log('Data'+result);    
                      var contents= result;
                      editor.setValue(contents);
                            }
                            
                       });
                                    

    
},	
  
        "save": function saveTextAsFile(editor)
	{ 
            
	    var textToSave = editor.getValue();
	    var textToSaveAsBlob = new Blob([textToSave], {type:"text/plain"});
	    var textToSaveAsURL = window.URL.createObjectURL(textToSaveAsBlob);
	    var fileNameToSaveAs = document.getElementById("inputFileNameToSaveAs").value;

                      var headers = {
                      "Content-Type": "application/json; charset=utf-8",
                      "Accept" : "application/json"
                       };                                           

		      var data = {};
                      data.body = {};
                      data.body.fileName =fileNameToSaveAs
                      data.body.content  =textToSave
        
		      jQuery.ajax({
		      type: 'POST',
		      data: data, 
                      crossDomain:true,
                      url: 'http://localhost:5080/endpoint',						
                            success: function(data) {
                            console.log('success');
                            console.log(JSON.stringify(data));
                            }
                           
                      });
            
	   var downloadLink = document.createElement("a");
	    downloadLink.download = fileNameToSaveAs;
	    downloadLink.innerHTML = "Download File";
	    downloadLink.href = textToSaveAsURL;
	    downloadLink.style.display = "none";
	    document.body.appendChild(downloadLink);	 
	    downloadLink.click();
	},


   }


    var editor = CodeMirror.fromTextArea(document.getElementById('code'), {
        parserfile: ["parsepython.js"],
        autofocus: true,
        theme: "solarized dark",
        styleActiveLine: true,
        lineNumbers: true,
        textWrapping: false,
        indentUnit: 4,
        height: "160px",
        fontSize: "9pt",
        autoMatchParens: true,
        extraKeys: keymap,
        parserConfig: {'pythonVersion': 2, 'strictErrors': true}
    });

   
    window.code_editor = editor;
    window.jsoutf = jsoutf;
    window.outf = outf;
    window.builtinRead = builtinRead;

    $("#skulpt_run").click(function (e) {
        $('#edoutput').text('');
        $('#mycanvas').hide();
    });

    $("#skulpt_run").click(function (e) { keymap["Ctrl-Enter"](editor)} );

    $("#skulpt_save").click(function (e) { keymap["save"](editor)} );
    $("#skulpt_load").click(function (e) {
        $(editor.setValue(''));
        $('#mycanvas').hide();
    });
    $("#skulpt_load").click(function (e) { keymap["load"](editor)} );
    $("#toggledocs").click(function (e) {
        $("#quickdocs").toggle();
    });

    var exampleCode = function (id, text) {
        $(id).click(function (e) {
            editor.setValue(text);
            editor.focus(); 
        });
    };

    exampleCode('#codeexample1', "print 'Hello, World!'     # natch");
    exampleCode('#codeexample2', "for i in range(5):\n    print i\n");
    exampleCode('#codeexample3', "print [x*x for x in range(20) if x % 2 == 0]");
    exampleCode('#codeexample4', "print 45**123");
    exampleCode('#codeexample5', "print \"%s:%r:%d:%x%#-+37.34o\" % (\n        \"dog\",\n        \"cat\",\n        23456,\n        999999999999L,\n        0123456702345670123456701234567L)");
    exampleCode('#codeexample6', "def genr(n):\n    i = 0\n    while i < n:\n        yield i\n        i += 1\n\nprint list(genr(12))\n");
    exampleCode('#codeexample7', "# obscure C3 MRO example from Python docs\nclass O(object): pass\nclass A(O): pass\nclass B(O): pass\nclass C(O): pass\nclass D(O): pass\nclass E(O): pass\nclass K1(A,B,C): pass\nclass K2(D,B,E): pass\nclass K3(D,A): pass\nclass Z(K1,K2,K3): pass\nprint Z.__mro__\n");
    exampleCode('#codeexample8', "import document\n\npre = document.getElementById('edoutput')\npre.innerHTML = '''\n<h1> Skulpt can also access DOM! </h1>\n''' \n");

    $('#clearoutput').click(function (e) {
        $('#edoutput').text('');
        $('#mycanvas').hide();
    });


    function builtinRead(x) {
        if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
        return Sk.builtinFiles["files"][x];
    }

    editor.focus();
});


