$(function(){
    $('#html').on('click',function(){
        $('#html_text').fadeIn()
    });
    $('#css').on('click',function(){
        $('#css_text').fadeIn()
    });
    $('#js').on('click',function(){
        $('#js_text').fadeIn()
    });
    $('#jq').on('click',function(){
        $('#jq_text').fadeIn()
    });

    $("#theTarget").skipper();
}