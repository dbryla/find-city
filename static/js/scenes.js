function setGameScene() {
    $("#welcome").hide();
    $("#header").hide();
    $("#rank").hide();
    $("#about").hide();
    $("#game-wrapper").show();
}

function setWelcomeScene() {
    $("#welcome").show();
    $("#header").show();
    $("#rank").hide();
    $("#about").hide();
    $("#home-li").addClass("active");
    $("#rank-li").removeClass("active");
    $("#about-li").removeClass("active");
    $("#game-wrapper").hide();
}

function setRankScene() {
    $("#welcome").hide();
    $("#header").show();
    $("#rank").show();
    $("#about").hide();
    $("#home-li").removeClass("active");
    $("#rank-li").addClass("active");
    $("#about-li").removeClass("active");
    $("#game-wrapper").hide();
    getRank();
}

function setAboutScene() {
    $("#welcome").hide();
    $("#header").show();
    $("#rank").hide();
    $("#about").show();
    $("#home-li").removeClass("active");
    $("#rank-li").removeClass("active");
    $("#about-li").addClass("active");
    $("#game-wrapper").hide();
}