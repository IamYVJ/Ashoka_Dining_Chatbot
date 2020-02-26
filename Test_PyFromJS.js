
// const { spawn } = require('child_process');
// const temperatures = []; // Store readings

// const sensor = spawn('python', ['sensor.py']);
// console.log(sensor);
// sensor.stdout.on('data', function(data) {

//     // convert Buffer object to Float
//     temperatures.push(parseFloat(data));
//     console.log(temperatures);
// });

    const spawn = require('child_process').spawn;
    const process = spawn('python', ['Test_PytoJS.py', "Hzzz"]);
    // const msg = [];
    var msg;


function abc(callback) {
    process.stdout.on('data', data => {
        // msg.push(data);
        // script.onload(process.stdout)
        // return data.toString();
        msg = data.toString();
        // console.log(msg);
        // console.log(data.toString());
        var t = callback();
        console.log(t);
    });
}

// let myPromise = new Promise((resolve, reject) => {
// 	// setTimeout(() => {
// 	// 	resolve("")
//     // }, 100)
//     process.stdout.on('data', data => {
//         msg = data.toString();
//     })
// })
// myPromise.then((resolve) => {
//     console.log(msg);
// 	// do whatever you want to do
// })

// .catch((err)=>{
//     console.log("error");
// })
function pr(){
    return msg;
}
abc(pr);


