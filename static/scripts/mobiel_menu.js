$(document).ready(function() {
	//Verberg standaard de donkere overlay;
    $('#fade').hide();
	//Als op het menu-icoontje wordt geklikt, komt de menubalk in beeld en wordt de achtergrond donker.
    $('#navicon').click(function() {
            $('body').animate({left: "-260px"}, 400).css({"overflow":"hidden"});
            $('#mobile-menu-wrap').animate({right: "0"}, 400);
            $('#fade').fadeIn(); 
	});
	//Als ergens anders wordt geklikt (zwarte achtergrond), gaat de menubalk terug en wordt de achtergrond terug helder.
	$('#fade').click(function() {
            $('body').animate({left: "0"}, 400).css({"overflow":"scroll"});
            $('#mobile-menu-wrap').animate({right: "-260px"}, 400);
            $('#fade').fadeOut();
    });
	//Verberg standaard de submenu's
	$('#mobile-menu').find('ul').hide();
	//Functionaliteit voor het openen en sluiten van de submenu's.
	$('#submenubutton1,#submenubutton2,#submenubutton3').click(function(){
		$('#mobile-menu > li').not(this).find('ul').slideUp();
    	$(this).find('ul').stop(true, true).slideToggle(400);   
	});

	$('#submenubutton1 ul,#submenubutton2 ul,#submenubutton3 ul').click(function (e) {
	    e.stopPropagation()
	});
});