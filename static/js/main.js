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

function loadFlags(countryList){
    if(countryList.length == 0){
        init();
    } else {
        var country = countryList[0];
        var img = new Image();
        img.onload = function(){loadFlags(countryList.slice(1))};
        img.src = "static/img/flags/" + country.toLowerCase() + ".png";
    }
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

    $("#home-li").click(function () {
        setWelcomeScene();
    });
    $("#rank-li").click(function () {
        setRankScene();
    });
    $("#about-li").click(function () {
        setAboutScene();
    });
}

$(document).ready(function () {
    loadFlags(Object.keys(worldmap.names));
});