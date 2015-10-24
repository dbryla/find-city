var timerInterval = 0;

function hideRestartButton() {
    $("#restart").hide();
    $("#round").show();
}

function showRestartButton() {
    $("#restart").show();
    $("#round").hide();
}

function showRecordModal() {
    var modal = $('#record-modal');
    modal.modal({
        backdrop: 'static',
        keyboard: false
    });
    modal.modal('show');
}

function showFriendModal(id) {
    var modal = $('#friend-modal');
    modal.modal({
        backdrop: 'static',
        keyboard: false
    });
    modal.find("#id").text(id);
    modal.modal('show');
}

function closeWaitingModal() {
    $('#waiting-modal').modal('hide');
    $('#friend-modal').modal('hide');
}
function showWaitingModal() {
    var modal = $('#waiting-modal');
    modal.modal({
        backdrop: 'static',
        keyboard: false
    });
    modal.modal('show');
}

function showModal(text) {
    $('#end-game-modal-title').text(text);
    $('#end-game-modal').modal('show');
}

function incRound() {
    var round = $("#round");
    round.show();
    var value = parseInt(round.find(".value").text()) + 1;
    round.find(".value").text(value);
}

function setRound(value, totalRounds) {
    totalRounds = totalRounds || 10;
    var round = $("#round");
    round.show();
    round.find(".value").text(value);
    round.find(".total").text(totalRounds);
}

function hideInfo() {
    $("#p1-info").hide();
    $("#p2-info").hide();
}

function setPlayerInfo(distance, score) {
    var p1Info = $("#p1-info");
    p1Info.show();
    p1Info.find(".distance").text(distance);
    p1Info.find(".score").text(score);
}

function setOpponentInfo(distance, score) {
    var p2Info = $("#p2-info");
    p2Info.show();
    $("#opp-timeout").hide();
    p2Info.find(".distance").text(distance);
    p2Info.find(".score").text(score);
}

function setOpponentTimeoutInfo() {
    $("#p2-info").hide();
    $("#opp-timeout").show();
}

function setPlayerScore(value) {
    var playerScore = $("#player-score");
    playerScore.parent().show();
    playerScore.text(value);
}

function setOpponentScore(value) {
    var opponentScore = $("#opponent-score");
    opponentScore.parent().show();
    opponentScore.text(value);
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

function hideTimer() {
    $("#timer").hide();
}

function askQuestion(country_code, city) {
    var countryStr = worldmap.names[country_code.toUpperCase()];
    $("#question").show();
    $("#country").text(countryStr);
    $("#flag").attr("src", "static/img/flags/" + country_code.toLowerCase() + ".png");
    $("#city").text(city);
}

function hideQuestion() {
    $("#question").hide();
}

function setGameScene() {
    $("#welcome").hide();
    $("#header").hide();
    $("#game-wrapper").show();
}

function setWelcomeScene() {
    $("#welcome").show();
    $("#header").show();
    $("#game-wrapper").hide();
}