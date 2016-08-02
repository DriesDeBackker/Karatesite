/**
 * Created by Dries on 1/08/2016.
 */
$(document).ready(function() {
  $(window).scroll(function () {
      console.log($(window).scrollTop())
    if ($(window).scrollTop() > 172) {
      $('#third-bar').addClass('third-bar-fixed');
    }
    if ($(window).scrollTop() < 172) {
      $('#third-bar').removeClass('third-bar-fixed');
    }
  });
});