function categoryDrop() {
  document.getElementById("categoryDropdown").classList.toggle("show");
}
function profileDrop(){
document.getElementById("profileDropdown").classList.toggle("show")
}
function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("categoryDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}


$(document).ready(function(){
  $('ul .measure').click(function(){
    var measure = {'measure': this.getAttribute("data-id"),
                  'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                };
    $.ajax({
        type: "POST",
        url: "prueba/",
        data: measure
      });
  });
})
