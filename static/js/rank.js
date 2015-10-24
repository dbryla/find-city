function populateRankTable(rank) {
    var table = $("#rank-table");
    table.empty();
    var row, name, score;
    for (var i = 0; i < rank.length; i++) {
        row = rank[i];
        name = row[0];
        score = row[1];
        table.append("<tr><td>" + (i + 1) + ".</td><td>" + name + "</td><td>" + score + "</td></tr>")
    }
}

var id;
var send;

function recordSocket() {
    var host = location.origin.replace(/^http/, 'ws') + "/socket";
    var socket = new WebSocket(host);

    if (socket) {
        socket.onopen = function () {
            console.log("connection opened....");
        };

        socket.onmessage = function (msg) {
            var obj = JSON.parse(msg.data);
            switch (obj["action"]) {
                case "init":
                    id = obj["msg"];
                    var wiad = '{"action": "list", "id": ' + id + '}';
                    socket.send(wiad);
                    break;
                case "rank":
                    var rank = obj["msg"];
                    populateRankTable(rank);
                    break;

                default:
                    console.log(obj["msg"]);
            }
        };

        socket.onclose = function () {
            console.log("connection closed....");
        }
    } else {
        console.log("invalid socket");
    }
}
