var id;
var send;

function initSocket() {
    var host = location.origin.replace(/^http/, 'ws') + "/socket";
    //var host = "ws://localhost:"+port+"/socket";
    var socket = new WebSocket(host);
    //var id;
    /*
     $( "#target2" ).click(function() {
     var wiad = '{"action": "friend", "msg": 2, "id": '+id+'}';
     socket.send(wiad);
     });
     */

    if (socket) {
        socket.onopen = function () {
            showServerResponse("connection opened....");
        };

        socket.onmessage = function (msg) {
            var obj = JSON.parse(msg.data);
            /*  action:  start - miasto
             | end
             */
            console.log(msg);

            switch (obj["action"]) {
                case "init":
                    id = obj["msg"];
                    break;
                case "start":
                    ask_question(obj["msg"]["country"], obj["msg"]["name"]);
                    break;
                case "end":
                    if (obj["msg"]["players"][0]["id"] == id) {
                        player = obj["msg"]["players"][0];
                        oponent = obj["msg"]["players"][1];
                    } else {
                        player = obj["msg"]["players"][1];
                        oponent = obj["msg"]["players"][0];
                    }
                    setPlayerInfo(parseInt(player["dist"]), parseInt(player["point"]));
                    setOpponentInfo(parseInt(oponent["dist"]), parseInt(oponent["point"]));

                    showCorrectLocation(obj["msg"]["location"], oponent["click"]);

                    if (player["win"]) {
                        showModal("Wygalem!");
                    } else {
                        showModal("Przegralem");
                    }
                    break;
                case "wait":
                    closeWaitingModal();
                    startTimer(5, "Game starts in: ");
                    break;

                default:
                    showServerResponse(obj["msg"]);
            }
        };

        socket.onclose = function () {
            showServerResponse("connection closed....");
        }

    } else {
        console.log("invalid socket");
    }

    function showServerResponse(txt) {
        console.log(txt);
    }

    send = function (msg) {
        var wiad = '{"action": "play", "x": ' + msg.lat + ', "y": ' + msg.lon + ', "time": 100, "id": ' + id + '}';
        socket.send(wiad);
    }
}
