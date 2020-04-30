var express 	=require('express')
var app 	= express();
var bodyParser 	= require("body-parser");





app.use(bodyParser.urlencoded({extended:true}));




app.get('/', function(req,res){
	
	res.render('index.ejs')
	});

app.get('/create', function(req,res){
	res.render('createform.ejs');
	});


app.post("/create",function(req,res){
	
	
	var spawn = require("child_process").spawn;
	var process = spawn('python3',["./out.py", 
                            req.body.cont, 
                            req.body.image] ); 
	process.stdout.on('data', function(data) { 
        res.send('Container is created with ID: '+ data.toString()+'\nGo back now'); 
    } );
  
	
	});

app.get("/delete", (req,res)=> {
	res.render('del.ejs');	
	})

app.post('/delete', (req,res)=>{
	console.log('running post route')
	var spawn = require("child_process").spawn;
	var process = spawn('python3',["./del.py", 
                            req.body.cont] ); 
	process.stdout.on('data', function(data) { 
	console.log('script should be complete by now')
        res.send('Container is deleted: '+ data.toString()+'\nGo back now'); 
    } );
	});


app.get("/pullimage", (req,res)=> {
	res.render('pull.ejs');	
	})

app.post('/pullimage', function(req,res){
	console.log('running post route')
	var spawn = require("child_process").spawn;
	console.log(req.body.image)
	var process = spawn('python3',["./pull.py", 
                            req.body.image] ); 
	process.stdout.on('data', function(data) { 
	console.log('script should be complete by now')
        res.send('Image pulled: '+ data.toString()+'\nGo back now'); 
	console.log(data.toString())
    } );
	});








app.get('/names', callName); 
  
function callName(req, res) { 
      
    // Use child_process.spawn method from  
    // child_process module and assign it 
    // to variable spawn 
    var spawn = require("child_process").spawn; 
      
    // Parameters passed in spawn - 
    // 1. type_of_script 
    // 2. list containing Path of the script 
    //    and arguments for the script  
      
    // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will 
    // so, first name = Mike and last name = Will 
    var process = spawn('python3',["./hello.py", 
                            req.body.cont, 
                            req.body.image] ); 
  
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object 
    process.stdout.on('data', function(data) { 
        res.send(data.toString()); 
    } ) 
} 

app.get('/name', callName); 
  
function callName(req, res) { 
      
    // Use child_process.spawn method from  
    // child_process module and assign it 
    // to variable spawn 
    var spawn = require("child_process").spawn; 
      
    // Parameters passed in spawn - 
    // 1. type_of_script 
    // 2. list containing Path of the script 
    //    and arguments for the script  
      
    // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will 
    // so, first name = Mike and last name = Will 
    var process = spawn('python3',["./hello.py", 
                            req.query.firstname, 
                            req.query.lastname] ); 
  
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object 
    process.stdout.on('data', function(data) { 
        res.send(data.toString()); 
    } ) 
} 


app.get('*',function(){
	res.send('try another route')
	
	});



app.listen(3000, function(){
	console.log('server running')
	});
