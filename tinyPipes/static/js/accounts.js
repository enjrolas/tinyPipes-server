$(document).ready(function(e) {
    adjustHeader();
});

function adjustHeader(){
    //get width of the NOT fixed header spans
    var a = $("span#fName").width();
    b = $("span#fCountry").width();
    c = $("span#fStatus").width();
    d = $("span#fCommands").width();

    //Change the width of the fixed header spans
    //with the other headers spans
    $("span#tName").width(a);
    $("span#tCountry").width(b);
    $("span#tStatus").width(c);
    $("span#tCommands").width(d);
}

$('html').ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});