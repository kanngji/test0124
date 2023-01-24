// server.js

const net = require("net");
const readline = require("readline-sync");

const server = net.createServer();

server.on("connection", (socket) => {
  socket.on("data", (data) => {
    console.log("Received: " + data);
    // // console.log(data);
    let change_data = data.toString();
    // // console.log(change_data);
    if (change_data === "ping") {
      change_data = "pong";
      sendLine(change_data);
    }
    // } else {
    //   //   console.log("ping이 아닐때");
    //   sendLine(change_data);
    // }
    else {
      //   console.log("else");
      sendLine();
    }
  });

  socket.on("error", () => {
    console.log(err.message);
  });

  function sendLine(data) {
    // console.log(data, "일로");
    // changed_data = data.toString();
    // console.log(changed_data);
    if (changed_data === "pong") {
      let line = readline.question("\n Send:\t" + changed_data);
      socket.write(line);
    } else {
      let line = readline.question("\n Send:\t" + data);
      console.log("여기");
      socket.write(line);
    }
  }
});

server.listen(4000, () => {
  console.log("server is connect", server.address().port);
});
