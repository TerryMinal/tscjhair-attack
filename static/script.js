var display_pics = function(e){
    //alert('test');
    console.log('test');
    var input=document.getElementsByTagName('input');
    var i =0;
    while(i < 5) {
        if(input[i].checked) {
            console.log('img ' + i + ' is checked!');
        }
        else{
            console.log('img ' + i + ' isn\'t checked!');
            runAjax(input[i]);
        }
        i++;
    }
};
$(document).ready(function() {
    document.getElementById("display_submit").addEventListener('click', display_pics);
    console.log('test');
});

var runAjax = function(inp) {
    $.ajax({
        type: 'GET',
        url: '/update_display',
        data: {"replace_pics": inp},
        async: true,
        beforeSend: function() {
            console.log('b');
        },
        success: function(d){
            console.log('a');
            console.log(d);
            console.log(JSON.parse(d));
            d=JSON.parse(d);
            console.log(d['new_pics']);
        }

    });
    return true;
}
