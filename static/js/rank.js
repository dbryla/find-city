function populateRankTable(rank) {
    var table = $("#rank-table");
    table.empty();
    var row, name, score;
    for (var i = 0; i < rank.length; i++) {
        row = rank[i];
        name = row[0];
        score = row[1];
        table.append("<tr><td>" + (i + 1) + ".</td><td>" + name + "</td><td>" + score + "</td></tr>")
        table.append("<tr><td>" + (i + 1) + ".</td><td>" + name + "</td><td>" + score + "</td></tr>")
    }
}

var id;
var send;

function getRank() {
    $.get( "/get", function( data ) {
        populateRankTable(data["rank"]);
    });
}
