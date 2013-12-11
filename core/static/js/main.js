var offset = $(".well.comprar").offset();
var topPadding = 0;


$(window).scroll(function() {
    var heightColuna = $(".detalhes-pacote").height();
    var heightWell = $(".sidebar .comprar").height() + 70;
    var max_height = offset.top + heightColuna - heightWell;

    if ($(window).scrollTop() > offset.top && $(window).scrollTop() < max_height) {
        $(".well.comprar").stop().animate({
            marginTop: $(window).scrollTop() - offset.top + 10,
        });
    }

    else if ($(window).scrollTop() < max_height) {
        $(".well.comprar").stop().animate({
            marginTop: 0
        });
    }
});
