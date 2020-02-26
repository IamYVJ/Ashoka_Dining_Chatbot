
var msg = "Sorry, Try Again!";

function getMsg(q){
      const spawn = require('child_process').spawn;
      const process = spawn('python', ['Bot_Message.py', q]);
      
       process.stdout.on('data', data => {
        msg = data.toString();  

    });

  }

const sulla = require('sulla');

sulla.create().then(client => start(client));

function start(client) {
  client.onMessage( message => {
    msg = "Sorry, Try Again!";

    var q = message.body;
    
    getMsg(q);
    
    setTimeout(function() {
        client.sendText(message.from, msg);
        console.log("Sent: " + msg);
    },1000);
  }); 
}
