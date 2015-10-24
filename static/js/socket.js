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

    $("#record-btn").click(function () {
        var username = $("#record-name").val();
        if (username.length > 0) {
            var wiad = '{"action": "record", "msg": "' + username + '", "id": ' + id + '}';
            console.log(wiad);
            socket.send(wiad);
        }
    });

    var firstTime = true;
    var round = 0;

    if (socket) {
        socket.onopen = function () {
            showServerResponse("connection opened....");
        };

        socket.onmessage = function (msg) {
            var obj = JSON.parse(msg.data);

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
                    askQuestion(obj["msg"]["country"], obj["msg"]["name"]);
                    startTimer(10, "Round ends in: ");
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
                    if (opponent.hasOwnProperty("dist")) {
                        setOpponentInfo(parseInt(opponent["dist"]), parseInt(opponent["point"]));
                    } else {
                        setOpponentTimeoutInfo();
                    }
                    setPlayerScore(parseInt(player["result"]));
                    setOpponentScore(parseInt(opponent["result"]));

                    showCorrectLocation(obj["msg"]["location"], opponent["click"]);
                    if (++round == 10) {
                        playerScore = parseInt(player["result"]);
                        opponentScore = parseInt(opponent["result"]);
                        if (player["record"]) {
                            showRecordModal();
                        }
                        if (playerScore > opponentScore) {
                            showModal("You win");
                        } else if (playerScore == opponentScore) {
                            showModal("Tie");
                        } else {
                            showModal("You lose");
                        }
                        showRestartButton();
                    }

                    break;
                case "wait":
                    if (firstTime) {
                        closeWaitingModal();
                        startTimer(5, "Game starts in: ");
                    } else {
                        startTimer(5, "Next round in:");
                    }
                    break;
                case "error":
                    break;
                case "quit":
                    showModal("You win! Your opponent has quit.");
                    showRestartButton();
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
