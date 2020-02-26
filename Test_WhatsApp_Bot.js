
// var msg = "Try Again"
// async function pr(q, callback){
//     // msg = "Try Again"
//     const spawn = require('child_process').spawn;
//     const process = await spawn('python', ['Test_PytoJS.py', q]);

//     process.stdout.on('data', data => {
//       msg = data.toString();  
//       // console.log(msg);
//   });
//   callback();
// }

// function prr(q){
//     const spawn = require('child_process').spawn;
//     const process = spawn('python', ['Test_PytoJS.py', q]);

//     process.stdout.on('data', data => {
//       msg = data.toString();  
//       console.log(msg);
//       return 1;
//   });
// }
var msg = "TO";

function getMsg(q){
      const spawn = require('child_process').spawn;
      const process = spawn('python', ['Test_PytoJS.py', q]);
      
       process.stdout.on('data', data => {
        msg = data.toString();  
        console.log("1");
        console.log(msg);
    });
    // setTimeout(function() {console.log("ST");},100);
    // return 1;
  }



const sulla = require('sulla');

sulla.create().then(client => start(client));

function start(client) {
  client.onMessage( message => {
  var q = message.body

    // client.sendText(message.from, mes => {
    //   const spawn = require('child_process').spawn;
    //   const process = spawn('python', ['Test_PytoJS.py', q]);
    //   process.stdout.on('data', data => {
    //   msg = data.toString();  
    //   console.log(msg);
    //   return msg;
    //   });
    // return msg;
    // });
    // pr(q, async function sendmsg(){
    //   client.sendText(message.from,msg);
    // });
    getMsg(q);
    
    console.log("s" + msg.toString());
    setTimeout(function() {client.sendText(message.from, msg);},1000);
    // prr(q).then(function() {
    //   client.sendText(message.from,msg);
    // });
    // if (message.body === 'Helloxx') {
    //   client.sendText(message.from, 'Hello from sulla!');
    // }
  }); 
}


// let myPromise = new Promise((resolve, reject) => {
// 	setTimeout(() => {
// 		resolve("")
//     }, 100)
//     process.stdout.on('data', data => {
//         msg = data.toString();
//     })
// })
// myPromise.then((resolve) => {
//     console.log(msg);
// 	// do whatever you want to do
// })