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
    setRound(0, 10);
    hideInfo();
}

function init() {
    loadMap();
    $("#play-btn").click(function () {
        initGame();
        initSocket(false);
    });
    $("#play-friend-btn").click(function () {
        initGame();
        initSocket(true);
    });
    $("#restart-btn").click(function () {
        hideInfo();
        hideTimer();
        hideQuestion();
        hideRestartButton();
        setWelcomeScene();
    });
}

$(document).ready(function () {
    init();
});