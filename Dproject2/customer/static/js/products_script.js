$('document').ready(function(){

$('select').on('change', function() {

  var id = this.value;
  var item_upc = $(this).children(":selected").attr("id");

  $.ajax({
    async: true,
      type: "POST",
      url: "price/",
      data: {
        'item_upc':item_upc // from form
      },
      success: function (data) {
        var object = JSON.parse(data)
        var market_price = object.market_price.toFixed(2)
        var price = object.price.toFixed(2)
        var unit = object.unit

        if (market_price >= price || market_price == 0){
          $("#"+id).html("Rs.&nbsp;"price + "/" + unit)
        }else{
          $("#"+id).html("Rs." + price + "/" + unit)
        }

            }
    });
    return false;


});


});
