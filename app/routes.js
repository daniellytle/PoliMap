var data = require('./data');

module.exports = function(app, io, sentiment) {

	io.on('connection', function(socket){
		console.log('a user connected');
		socket.on('disconnect', function(){
			console.log('user disconnected');
		});
	});

	app.get('/', function(req, res) {
		res.render('map');
	});

	app.post('/api/tweet', function(req, res) {
		console.log('Got Tweet');
		console.log(req.body);

		io.emit('tweet', { 
			state: req.body.state,
			pol : req.body.pol 
		});
		res.status(200).end();
	})
}