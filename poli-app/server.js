//Think of these require statements as #include statements. They're just pre-built libraries.
var express = require('express');
var handles = require('express-handlebars');
var sentiment = require('sentiment');
var bodyParser = require('body-parser');
var app = express();

// Body Parser
app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({ extended: true })); // for parsing application/x-www-form-urlencoded

// Static Files
app.use(express.static(__dirname + '/public'));
// Start the server
var server = app.listen(8888);
console.log('Server magic happens at port 8888');

// Routes
var io = require('socket.io')(server);
require('./app/routes')(app, io, sentiment);

//This allows us to use handlebars as our template engine
app.set('views', __dirname + '/public/views');
app.engine('.hbs', handles({
	defaultLayout: 'base',
	layoutsDir: 'public/views/layouts',
        extname: '.hbs'
}));
app.set('view engine', '.hbs');

