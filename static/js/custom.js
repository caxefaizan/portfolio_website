(function ($) {

  "use strict";

    // COLOR MODE
    $('.color-mode').click(function(){
        $('.color-mode-icon').toggleClass('active')
        $('body').toggleClass('dark-mode')
    })

    // HEADER
    $(".navbar").headroom();

    // PROJECT CAROUSEL
    $('.owl-carousel').owlCarousel({
    	items: 1,
	    loop:true,
	    margin:10,
	    nav:true
	});

    // SMOOTHSCROLL
    $(function() {
      $('.nav-link, .custom-btn-link').on('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - 49
        }, 1000);
        event.preventDefault();
      });
    });  

    // TOOLTIP
    $('.social-links a').tooltip();

    // CONTACT FORM — AJAX SUBMIT
    $('form[action="submit_form"]').on('submit', function (e) {
      e.preventDefault();
      var form = this;
      if (!form.checkValidity()) { form.reportValidity(); return; }
      fetch('submit_form', { method: 'POST', body: new FormData(form) })
        .then(function () {
          form.reset();
          $('html, body').animate({ scrollTop: $('#contact').offset().top - 49 }, 600, function () {
            $('#contact-success-banner').fadeIn(300);
          });
        })
        .catch(function () {
          alert('Something went wrong. Please try again.');
        });
    });

})(jQuery);
