$(document).ready(function(){
    var $btnTop = $(".btn-top")
    $(window).on("scroll", function(){
        if ($(window).scrollTop() >= 500){
            $btnTop.fadeIn();
        }else{
            $btnTop.fadeOut();
        }
    });

    $btnTop.on("click", function(){
        $("html").animate({scrollTop:0}, 1000)
    });
})