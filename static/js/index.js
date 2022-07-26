$(document).ready(function(){
    //banner owl carousel
    $("#banner-area .owl-carousel").owlCarousel({
        dots: true,
        items: 1,
        loop: true,
        autoplay:true,
        autoplayTimeout: 2000,
        autoplayHoverPause:true
    });

    //top sale carousel
    $("#top-sale .owl-carousel").owlCarousel({
        loop: true,
        nav: false,
        dots: false,
        responsive: {
            0:{
                items: 2
            },
            420:{
                items: 3
            },
            980:{
                items: 4
            },
            1244:{
                items: 5
            }
        }
    });
   

    //shop carousel
    $("#shop .owl-carousel").owlCarousel({
        loop: true,
        nav: false,
        dots: false,
        responsive: {
            0:{
                items: 2
            },
            420:{
                items: 3
            },
            980:{
                items: 4
            },
            1244:{
                items: 5
            }
        }
    });

    //isotope filter
    var $grid = $(".grid").isotope({
        itemSelector: '.grid-item',
        layoutMode: 'fitRows'
    });

    //filter items on buttton click
    $(".button-group").on("click", "button", function(){
        var filterValue = $(this).attr('data-filter');
        $grid.isotope({filter:filterValue});
    });

    //New Clothes carousel
    $("#new-clothes .owl-carousel").owlCarousel({
        loop: true,
        nav: false,
        dots: false,
        responsive: {
            0:{
                items: 2
            },
            420:{
                items: 3
            },
            980:{
                items: 4
            },
            1244:{
                items: 5
            }
        }
    });
    //product Qty section
    let $qty_up = $(".qty .qty_up");
    let $qty_down = $(".qty .qty_down");
    //let $input = $(".qty .qty_input");

    //click on qty
    $qty_up.click(function(e){
        let $input = $(`.qty_input[data-id='${$(this).data("id")}']`);
        if($input.val() >= 1 && $input.val() <= 19){
            $input.val(function(i, oldval){
                return++oldval;
            })
        }
    });

    //click on qty
    $qty_down.click(function(e){
        let $input = $(`.qty_input[data-id='${$(this).data("id")}']`);
        if($input.val() > 1 && $input.val() <= 20){
            $input.val(function(i, oldval){
                return--oldval;
            })
        }
    });
});

$(function(){
    $("[data-trigger]").on("click", function(){
        var target_id = $(this).attr("data-trigger");
        $(target_id).toggleClass("show")
        $('body').toggleClass("offcanvas-active")  
    });

    $(".btn-close").click(function(){
        $(".navbar-collapse").removeClass("show");
        $('body').removeClass("offcanvas-active");
    })
})

function myFunction(x) {
    x.classList.toggle("show_color");
  }

setTimeout(function(){
    $('#message').fadeOut('slow')
  }, 8000)


  // Data Picker Initialization

/*Size is  set in pixels... supports being written as: '250px' */
var magnifierSize = 500;

/*How many times magnification of image on page.*/
var magnification = 3;

function magnifier() {

  this.magnifyImg = function(ptr, magnification, magnifierSize) {
    var $pointer;
    if (typeof ptr == "string") {
      $pointer = $(ptr);
    } else if (typeof ptr == "object") {
      $pointer = ptr;
    }
    
    if(!($pointer.is('.magnifiedImg'))){
      // alert('Object must be image.');
      return false;
    }

    magnification = +(magnification);

    $pointer.hover(function() {
      //$(this).css('cursor', 'none');
      $('.magnify').show();

      //Setting some variables for later use
      var width = $(this).width();
      var height = $(this).height();
      var src = $(this).attr('src');
      var imagePos = $(this).offset();
      var image = $(this);

      if (magnifierSize == undefined) {
        magnifierSize = '300px';
      }

      $('.magnify').css({
        'background-size': width * magnification + 'px ' + height * magnification + "px",
        'background-image': 'url("' + src + '")',
        'width': magnifierSize,
        'height': magnifierSize
      });

      //Setting a few more...
      var magnifyOffset = +($('.magnify').width()/2);
      var rightSide = +(imagePos.left + $(this).width());
      var bottomSide = +(imagePos.top + $(this).height());

      $(document).mousemove(function(e) {
        if (e.pageX < +(imagePos.left - magnifyOffset / 6) || e.pageX > +(rightSide + magnifyOffset / 6) || e.pageY < +(imagePos.top - magnifyOffset / 6) || e.pageY > +(bottomSide + magnifyOffset / 6)) {
          $('.magnify').hide();
          //$(document).unbind('mousemove');
        }
        var backgroundPos = "" - ((e.pageX - imagePos.left) * magnification - magnifyOffset) + "px " + -((e.pageY - imagePos.top) * magnification - magnifyOffset) + "px";
        $('.magnify').css({
          'right': 120,
          'top': 220,
          'background-position': backgroundPos
        });
      });
    }, function() {

    });
  };

  this.init = function() {
    $('body').prepend('<div class="magnify"></div>');
  }

  return this.init();
}

var magnify = new magnifier();
magnify.magnifyImg('.magnifiedImg', magnification, magnifierSize);


