var timerInterval = 0;

function incRound() {
    var round = $("#round");
    var roundString = round.text();
    var roundNumbersString = roundString.split(" ")[1];
    var roundNumbers = roundNumbersString.split("/");
    var value = parseInt(roundNumbers[0]) + 1;
    var totalRounds = roundNumbers[1];
    round.text("Round " + value + "/" + totalRounds);
}

function setRound(value, totalRounds) {
    totalRounds = totalRounds || 10;
    var round = $("#round");
    round.show();
    round.text("Round " + value + "/" + totalRounds);
}

function hideInfo() {
    $("#p1-info").hide();
    $("#p2-info").hide();
}

function setPlayerInfo(distance, score) {
    var p1Info = $("#p1-info");
    p1Info.show();
    p1Info.text("You were off by " + distance + "km and scored " + score + "p");
}

function setOpponentInfo(distance, score) {
    var p2Info = $("#p2-info");
    p2Info.show();
    p2Info.text("Your opponent was off by " + distance + "km and scored " + score + "p");
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
    $("#flag").attr("src", "static/img/flags/" + country_code.toLowerCase() + ".png");
    $("#city").text(city);
}

function setGameScene() {
    $("#welcome").hide();
    $("#game-wrapper").show();
}