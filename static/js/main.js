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
        setPlayerScore(0);
        setOpponentScore(0);
        setRound(1, 10);
        initSocket();
        hideInfo();
        showModal("Waiting for the opponent...");
    });
}

$(document).ready(function () {
    init();
});