var m = require('mraa');

var analogPin0 = new m.Aio(0); //setup access analog inpuput pin 0
var analogValue = analogPin0.read();//read the value of the analog pin
console.log(analogValue); //write the value of the analog pin to the console
periodicActivity(); //call the periodicActivity function

function periodicActivity()
{
  analogValue = analogPin0.read();
  console.log(analogValue)
  setTimeout(periodicActivity,1000); //call the indicated function after 1 second (1000 milliseconds)
}