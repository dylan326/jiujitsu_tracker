$(document).ready(function() {
  $("#half_guard_offence").on("click", function() {
      var url = $("#half_guard_offence").attr("data-url");
      document.location.href = url;
  });
  $("#half_guard_defense").on("click", function() {
    var url = $("#half_guard_defense").attr("data-url");
    document.location.href = url;
  });
});