

function myfunc(){
  $("#replace_me").load("helper/");
};


$(document).ready(function(){


  $(".subcategories").click(function(){
    var category = this.getAttribute("data-id")
                $.ajax({
                  async: true,
                    type: "POST",
                    url: "subcategories/",
                    data: {
                      'category':category // from form
                    },
                    success: function (data) {
                      myfunc()
                    }
                  });
                  return false; //<---- move it here
                });

              });
