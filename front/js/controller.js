var timerInterval = 0;

function hideInfo() {
    $("#p1-info").hide();
    $("#p2-info").hide();
}

function setPlayerInfo(distance, score) {
    var p1Info = $("#p1-info");
    p1Info.show();
    p1Info.text("You were off by " + distance + "km and scored " + score + " points");
}

function setOpponentInfo(distance, score) {
    var p2Info = $("#p2-info");
    p2Info.show();
    p2Info.text("Your opponent was off by " + distance + "km and scored " + score + " points");
}

function setPlayerScore(value) {
    var playerScore = $("#player-score");
    playerScore.show();
    playerScore.text("Your score: " + value);
}

function setOpponentScore(value) {
    var opponentScore = $("#opponent-score");
    opponentScore.show();
    opponentScore.text("Opponent's score: " + value);
}

function getTimerValue() {
    var timeString = $("#timer-value").text();
    return parseInt(timeString);
}

function startTimer(value, text) {
    clearInterval(timerInterval);
    timerInterval = setInterval(decrementTimer, 1000);
    $("#timer").show();
    $("#timer-value").text(value);
    $("#timer-text").text(text);
}

function ask_question(country_code, city) {
    var countryStr = countries[country_code.toUpperCase()];
    $("#question").show();
    $("#country").text(countryStr);
    $("#flag").attr("src", "img/flags/" + country_code.toLowerCase() + ".png");
    $("#city").text(city);
}

function setGameScene() {
    $("#welcome").hide();
    $("#game-wrapper").show();
}