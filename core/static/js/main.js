var offset = $(".well.comprar").offset();
var topPadding = 0;

var heightColuna = $(".detalhes-pacote .col-md-9").height();

function heightSidebar(){
    $('.col-md-3.sidebar').css('height',heightColuna)
}

$(window).scroll(function() {

    heightSidebar();

    if ($(window).scrollTop() > offset.top) {
        $(".well.comprar").stop().animate({
            marginTop: $(window).scrollTop() - offset.top + 10,
        });

        if($(window).scrollTop() > heightColuna + 250 ){
            $(".well.comprar").stop().animate({
                marginTop: $(window).scrollTop() - offset.top - 120 ,
            });
        }
    } 
  
    else {
        $(".well.comprar").stop().animate({
            marginTop: 0
        });
    };

    


});