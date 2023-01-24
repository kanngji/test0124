// client.js

const net = require("net");
const readline = require("readline-sync");

const options = {
  port: 4000,
  host: "127.0.0.1",
};

const client = net.createConnection(options);

client.on("connect", () => {
  console.log("Client Connected");
  sendLine();
});

client.on("data", (data) => {
  console.log("Received: " + data);
  sendLine();
});

client.on("error", (err) => {
  console.log(err.message);
});

function sendLine() {
  let line = readline.question("\n Send:\t");
  client.write(line);
}
