function decrementTimer() {
    var curTime = getTimerValue();
    if (curTime > 0) {
        $("#timer-value").text(curTime - 1);
    } else {
        clearInterval(timerInterval);
    }
}
var id;
var send;

function initSocket(){
        var host = location.origin.replace(/^http/, 'ws')+"/socket"
        //var host = "ws://localhost:"+port+"/socket";
        var socket = new WebSocket(host);
        //var id;
        /*
        $( "#target2" ).click(function() {
             var wiad = '{"action": "friend", "msg": 2, "id": '+id+'}';
            socket.send(wiad);
        });
        */

        if(socket){
              socket.onopen = function(){
                showServerResponse("connection opened....");
              }

              socket.onmessage = function(msg){
                console.log(msg.data);
                var obj = JSON.parse(msg.data);
                /*  action:  start - miasto
                           | end   
                */

                switch(obj["action"]){
                    case "init":
                        id = obj["msg"];
                        showServerResponse("Your id:"+id);
                        break;
                    case "start":
                        ask_question(obj["msg"]["country"], obj["msg"]["name"]);
                        break;
                    case "end":
                        if(obj["msg"][0]["id"] == id){
                            player = obj["msg"][0];
                            oponent = obj["msg"][1];
                        } else {
                            player = obj["msg"][1];
                            oponent = obj["msg"][0];
                        }
                        setPlayerInfo(parseInt(player["dist"]), parseInt(player["point"]));
                        setOpponentInfo(parseInt(oponent["dist"]), parseInt(oponent["point"]));

                        if(player["win"]){
                            alert("Wygalem!");
                        } else {
                            alert("Przegralem");
                        }

                    default:
                        showServerResponse(obj["msg"]);
                }
              }

              socket.onclose = function(){
                showServerResponse("connection closed....");
              }

            }else{
              console.log("invalid socket");
            }

            function showServerResponse(txt){
                console.log(txt);
            }

            send = function(msg){
                console.log(msg);
                var wiad = '{"action": "play", "x": '+msg.lat +', "y": '+msg.lon+', "time": 100, "id": '+id+'}';
                socket.send(wiad);
            }
    }

function init() {
    $("#play-btn").click(function () {
        setGameScene();
        ask_question("de", "Berlin");
        startTimer(5, "Next country in: ");
        setPlayerScore(12120);
        setOpponentScore(424);
        setPlayerInfo(1238, 123);
        setOpponentInfo(8567, 41);
        setRound(1, 10);
        incRound();
        initSocket();
        //hideInfo();
    });
}

$(document).ready(function () {
    init();
    //$("#play-btn").click();  //for debugging purpose only
});