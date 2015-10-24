function decrementTimer() {
    var curTime = getTimerValue();
    if (curTime > 0) {
        $("#timer-value").text(curTime - 1);
    } else {
        clearInterval(timerInterval);
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
        //hideInfo();
    });
}

$(document).ready(function () {
    init();
    $("#play-btn").click();  //for debugging purpose only
});