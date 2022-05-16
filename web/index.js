const http = require("http");
const fs = require('fs')

// PORT
const PORT = 3000;

// server create
const server = http.createServer((req, res) => {
    let page;
    if (req.url === "/") {
        page = "home/index.html"
    } else if (req.url === "/about" && req.method === "GET") {
        page = "home/index.html"
    } else {
        res.write("Not Found!");
        res.end();
        return;
    }

    res.writeHead(200, {'Content-Type': 'text/html'});
    fs.createReadStream('index.html').pipe(res)
    res.end();
});

// server listen port
server.listen(PORT);

console.log(`Server is running on PORT: ${PORT}`);