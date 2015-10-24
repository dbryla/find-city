var timerInterval = 0;

function setScore(value) {
    $("#score").text("Score: " + value);
}

function decrementTimer() {
    var curTime = getTimerValue();
    if (curTime > 0) {
        $("#timer-value").text(curTime - 1);
    } else {
        clearInterval(timerInterval);
    }
}

function getTimerValue() {
    var timerText = $("#timer").text();
    var timeString = timerText.split(":")[1];
    return parseInt(timeString);
}

function startTimer(value, text) {
    clearInterval(timerInterval);
    timerInterval = setInterval(decrementTimer, 1000);
    $("#timer-value").text(value);
    $("#timer-text").text(text);
}

function ask_question(country_code, city) {
    var countryStr = countries[country_code.toUpperCase()];
    $("#country").text(countryStr);
    $("#flag").attr("src", "img/flags/" + country_code.toLowerCase() + ".png");
    $("#city").text(city);
}

function setGameScene() {
    $("#welcome").hide();
    $("#game-wrapper").show();
}

function init() {
    $("#play-btn").click(function () {
        setGameScene();
        ask_question("de", "Berlin");
        startTimer(5, "Next country in: ");
        setScore(12120);
    });
}

$(document).ready(function () {
    init();
    //for debugging purpose only
    //$("#play-btn").click();
});