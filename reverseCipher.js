// Reverse encryption program
// BSD Licensed

var message = "Hello, World!";
var translated = "";

for (var i = message.length - 1; i >= 0; i--) {
  translated += message.charAt(i);
}

console.log(translated);