function decrementTimer() {
    var curTime = getTimerValue();
    if (curTime > 0) {
        $("#timer-value").text(curTime - 1);
    } else {
        clearInterval(timerInterval);
    }
}

function initGame() {
    setGameScene();
    setPlayerScore(0);
    setOpponentScore(0);
    setRound(1, 10);
    hideInfo();
}

function init() {
    $("#play-btn").click(function () {
        initGame();
        initSocket(false);
    });
    $("#play-friend-btn").click(function () {
        initGame();
        initSocket(true);
    });
}

$(document).ready(function () {
    init();
});