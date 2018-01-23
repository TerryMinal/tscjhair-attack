var returnPics = []
var data = []

var display_pics = function(e){
    //alert('test');
    // console.log('test');
    var input=document.getElementsByTagName('input');
    var img=document.getElementsByClassName('rounded');
    var i =0;
    inp = [];
    while(i < 5) {
        if(input[i].checked) {
            console.log('img ' + i + ' is checked!');
        }
        else{
            console.log('img ' + i + ' isn\'t checked!');
            console.log(input[i]);
        }
        inp.push(img[i].src);
        i++;
    }
    returnPics = [];
    runAjax(inp);
    
};
$(document).ready(function() {
    document.getElementById("display_submit").addEventListener('click', display_pics);
    console.log('test document ready');
});

var runAjax = function(inp) {
    // console.log(inp);
    send = JSON.stringify(inp);
    // console.log(send);
    $.ajax({
        type: 'GET',
        url: '/update_display',
        data: {"replace_pics": send},
        async: true,
        beforeSend: function() {
           //  console.log('data: '+send);
        },
        success: function(d){
            //console.log('a');
	    console.log('printing d')
            console.log(d);
            d=JSON.parse(d);
            console.log(d);
            //console.log(d.new_pics);
            returnPics = d;
            shuffle(returnPics);
            console.log(returnPics);
            overwriteWithNew();
            
        }

    });
    return true;
}

function shuffle(array) {//Stolen, but just using this for testing
  var i = 0, j = 0, temp = null

  for (i = array.length - 1; i > 0; i -= 1) {
    j = Math.floor(Math.random() * (i + 1))
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
  }
}
var overwriteWithNew = function() {
    var input=document.getElementsByTagName('input');
    var img = document.getElementsByClassName('rounded');
    var i = 0;
    while (i < 5) {
        input[i].checked=false;
        console.log(returnPics[i])
        img[i].src = returnPics[i];
        i++
    }
}
