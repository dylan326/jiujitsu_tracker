$(document).ready(function() {
  $("#half_guard").on("click", function() {
      var url = $("#half_guard").attr("data-url");
      document.location.href = url;
  });
});