

$('#soundcapture').click(function() {
  console.log('#soundcapture was clicked');
    $.getJSON($SCRIPT_ROOT + '/_toggle_soundcapture', {
  }, function(data) {
    $("#soundcapture").text(function(i, text){
        return text === "On" ? "Off" : "On";
    })
  });
  return false;
});

