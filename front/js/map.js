function send(msg){
    console.log(msg);
}

Raphael("game", 1000, 400, function () {
    var r = this;

    //Draw water
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

    var dot = r.circle().attr({fill: "r#FE7727:50-#F57124:100", stroke: "#fff", "stroke-width": 2, r: 0});
    function clickMap(oLatLon){
        attr = getXY(oLatLon.lat, oLatLon.lon);
        attr.r = 0;
        dot.stop().attr(attr).animate({r: 5}, 1000, "elastic");
        send(oLatLon);
    }

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
});