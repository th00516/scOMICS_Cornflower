/*jQuery*/

$(document).ready(function() {

  $("#year").html(function() {
                    var thisYear = new Date();
                    return thisYear.getFullYear();
                  });

});