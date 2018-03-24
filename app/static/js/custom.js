$('#soundcapture').click(function () {
    var toggle_state = document.getElementById('soundcapture').innerText;
    $.getJSON($SCRIPT_ROOT + '/hue/_toggle_soundcapture/' + toggle_state, {}, function (data) {
        console.log(data);
        $("#soundcapture").text(function (i, text) {
            console.log('text: ' + text);
            var button = document.getElementById('soundcapture')

            if (text === 'On') {
                button.classList.remove('btn-success');
                button.classList.add('btn-danger');
            } else {
                button.classList.add('btn-success');
                button.classList.remove('btn-danger');
            }

            return text === "On" ? "Off" : "On";
        })
    });
    return false;
});

$(document).ready(function () {
    $('.nav a').click(function () {
        //removing the previous selected menu state
        $('.nav').find('li.active').removeClass('active');
        //adding the state for this parent menu
        $(this).parents("li").addClass('active');

    });
});