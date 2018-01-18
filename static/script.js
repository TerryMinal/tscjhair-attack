var display_pics = function(e){
    var input=document.getElementsByTagName('input')
    var i =0;
    while(i < 5){
	if(input[i].checked){	 
	    console.log('img ' + i + ' is checked!');
	}
	else{

	    

	    console.log('img ' + i + ' isn\'t checked!');
	}
	i++;
    }
};

document.getElementById("display_submit").addEventListener('click', display_pics);
