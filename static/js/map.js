function getXY(lat, lon) {
    return {
        cx: lon * 2.6938 + 465.4,
        cy: lat * -2.6938 + 227.066
    };
};
function getLatLon(x, y) {
    return {
        lat: (y - 227.066) / -2.6938,
        lon: (x - 465.4) / 2.6938
    };
};

var enableClick = false;
var dots;

function showCorrectLocation(realPos, opponentPos){
    attr = getXY(realPos.x, realPos.y);
    attr.r = 0;
    dots[0].stop().attr(attr).animate({r: 8}, 1000, "elastic");
    
    if(opponentPos && ((opponentPos.x && opponentPos.y) || opponentPos.x === 0 || opponentPos.y)){
        attr = getXY(opponentPos.x, opponentPos.y);
        attr.r = 0;
        dots[1].stop().attr(attr).animate({r: 5}, 1000, "elastic");
    }
}

function toggleClick(){
    enableClick = true;
    dots[0].attr({r: 0});
    dots[1].attr({r: 0});
    dots[2].attr({r: 0});
}

function loadMap(){
    var r = Raphael("game", 1000, 400);
    var water = r.rect(0, 0, 1000, 400, 10);
    water.attr({
        stroke: "none",
        fill: "0-#9bb7cb-#adc8da"
    });
    water.click(function(event){
        clickMap(getLatLon(event.layerX, event.layerY));
    });

    //Draw world
    r.setStart();
    var hue = Math.random();
    for (var country in worldmap.shapes) {
        // var c = Raphael.hsb(Math.random(), .5, .75);
        // var c = Raphael.hsb(.11, .5, Math.random() * .25 - .25 + .75);
        r.path(worldmap.shapes[country]).attr({stroke: "#ccc6ae", fill: "#f0efeb", "stroke-opacity": 0.25});
    }
    var world = r.setFinish();
    world.click(function(event){
        clickMap(getLatLon(event.layerX, event.layerY));
    });

    var dotLocation = r.circle(0, 0, 0).attr({fill: "r#91E547:50-#51AC00:100", stroke: "#000e", "stroke-width": 2, r: 0});
    var dotOpponent  = r.circle(0,0,0).attr({fill: "r#4263AF:50-#082D81:100", stroke: "#fff", "stroke-width": 2, r: 0});
    var dot = r.circle(0,0,0).attr({fill: "r#FE7727:50-#F57124:100", stroke: "#fff", "stroke-width": 2, r: 0});

    dots = [dotLocation, dotOpponent, dot];

    function clickMap(oLatLon){
        if(enableClick){
            attr = getXY(oLatLon.lat, oLatLon.lon);
            attr.r = 0;
            dot.stop().attr(attr).animate({r: 5}, 1000, "elastic");
            send(oLatLon);
            enableClick = false;
        }
    }
}