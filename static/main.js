$(document).ready(function(){
    $('.product-link').click(function(){
        $('#product-name').html($(this).data('name'));

        var imgset = $(this).data('img');
        $("#product-img").attr('src' , imgset);
        $("#indicator-img").attr('src' , imgset);

        var imgseta = $(this).data('imga');
        $("#product-imga").attr('src' , imgseta);
        $("#indicator-imga").attr('src' , imgseta);

        var imgsetb = $(this).data('imgb');
        $("#product-imgb").attr('src' , imgsetb);
        $("#indicator-imgb").attr('src' , imgsetb);

        $('#product-description').html($(this).data('description'));

        var sizeimg = $(this).data('size');
        $("#size-guidee").attr('src' , sizeimg);

        $('#product-price-list').html($(this).data('listprice'));
        $('#product-price-sale').html($(this).data('saleprice'));
        $('#product-category').html($(this).data('productcategory'));
        
        var id = $(this).data('id');
        $("#add-button").attr('value', id);

        var pro_id = $(this).data('id');
        $('#input').attr('data-id', pro_id)
        $('.qty_up').attr('data-id', pro_id)
        $('.qty_down').attr('data-id', pro_id)       


    });
});
