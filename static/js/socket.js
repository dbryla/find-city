var id;
var send;

function initSocket(friend) {
    var initQuery = "/socket";
    if (friend) {
        initQuery = "/friend";
    }
    var host = location.origin.replace(/^http/, 'ws') + initQuery;
    var socket = new WebSocket(host);

    $("#connect-btn").click(function () {
        var friendId = $("#friend-id");
        var friendIdText = friendId.val();
        if (parseInt(friendIdText) > 0) {
            var wiad = '{"action": "friend", "msg": ' + friendIdText + ', "id": ' + id + '}';
            socket.send(wiad);
        }
    });

    if (socket) {
        socket.onopen = function () {
            showServerResponse("connection opened....");
        };

        socket.onmessage = function (msg) {
            var obj = JSON.parse(msg.data);
            /*  action:  start - miasto
             | end
             */

            switch (obj["action"]) {
                case "init":
                    id = obj["msg"];
                    if (friend) {
                        showFriendModal(id);
                    } else {
                        showWaitingModal();
                    }
                    break;
                case "start":
                    ask_question(obj["msg"]["country"], obj["msg"]["name"]);
                    incRound();
                    toggleClick();
                    break;
                case "end":
                    if (obj["msg"]["players"][0]["id"] == id) {
                        player = obj["msg"]["players"][0];
                        opponent = obj["msg"]["players"][1];
                    } else {
                        player = obj["msg"]["players"][1];
                        opponent = obj["msg"]["players"][0];
                    }
                    setPlayerInfo(parseInt(player["dist"]), parseInt(player["point"]));
                    setOpponentInfo(parseInt(opponent["dist"]), parseInt(opponent["point"]));
                    setPlayerScore(parseInt(player["result"]));
                    setOpponentScore(parseInt(opponent["result"]));

                    showCorrectLocation(obj["msg"]["location"], opponent["click"]);

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
