$('#light_switch').click(function () {
    var toggle_state = document.getElementById('light_switch').innerText;
    $.getJSON($SCRIPT_ROOT + '/hue/_toggle_lights/' + toggle_state, {}, function (data) {

        $("#light_switch").text(function (i, text) {
            var button = document.getElementById('light_switch')

            if (data === 'Off') {
                button.classList.remove('btn-success');
                button.classList.add('btn-danger');
            } else {
                button.classList.add('btn-success');
                button.classList.remove('btn-danger');
            }

              return text = data

        })
    });
    return false;
});

$('#soundcapture').click(function () {
    var toggle_state = document.getElementById('soundcapture').innerText;
    $.getJSON($SCRIPT_ROOT + '/hue/_toggle_soundcapture/' + toggle_state, {}, function (data) {

        $("#soundcapture").text(function (i, text) {
            var button = document.getElementById('soundcapture')

            if (data === 'Off') {
                button.classList.remove('btn-success');
                button.classList.add('btn-danger');
            } else {
                button.classList.add('btn-success');
                button.classList.remove('btn-danger');
            }

              return text = data

        })
    });
    return false;
});

$(document).ready(function () {
    $("#{{request.endpoint}}").parent().addClass("active");
})