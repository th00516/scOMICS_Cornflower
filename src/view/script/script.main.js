/*eslint-env jquery*/

$(document).ready(function(){

  $("#year").html(function(){
    var thisYear = new Date();
    return thisYear.getFullYear();
  });
  
  $("#about").click(function(){
    alert(
"这是一个关于单细胞组学的数据分析平台，\n\
我们立志于打造一个功能丰富且易用的scOmics分析工具"
    );
  });

});