var display_pics = function(e){
    var input=document.getElementsByTagName('input')
    var i =0;
    while(i < 5){
	if(input[i].checked){	 
	    console.log('img ' + i + ' is checked!');
	}
	else{
	    console.log('img ' + i + ' isn\'t checked!');
	    
	    $.ajax({
		url: '/update_display',
		type: 'GET', 
		data:{"replace_pics": input[i]},

		success: function(d){
		    console.log(d);
		    console.log(JSON.parse(d));
		    d=JSON.parse(d);
		    console.log(d['new_pics']);
		}

	    });
	}
	i++;
    }
};

document.getElementById("display_submit").addEventListener('click', display_pics);
