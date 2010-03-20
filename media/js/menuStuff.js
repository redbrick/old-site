var timeout	= 500;
var closetimer	= 0;
var ddmenuitem	= 0;

// open hidden layer
function mopen(id)
{
	// change arrow to white
	if(ddmenuitem) {
		arrow_img = document.getElementById('downarrow_' + ddmenuitem.id);
		arrow_img.src = '/media/images/arrow_white.png';
	}
	
	// change arrow to red
	arrow_img = document.getElementById('downarrow_' + id);
	arrow_img.src = '/media/images/arrow_red.png';
	
	// cancel close timer
	mcancelclosetime();

	// close old layer
	if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';

	// get new layer and show it
	ddmenuitem = document.getElementById(id);
	ddmenuitem.style.visibility = 'visible';

}
// close showed layer
function mclose()
{
	// change arrow to white
	if(ddmenuitem) {
		arrow_img = document.getElementById('downarrow_' + ddmenuitem.id);
		arrow_img.src = '/media/images/arrow_white.png';
	}
	
	if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';
}

// go close timer
function mclosetime()
{
	closetimer = window.setTimeout(mclose, timeout);
}

// cancel close timer
function mcancelclosetime()
{
	if(closetimer)
	{
		window.clearTimeout(closetimer);
		closetimer = null;
	}
}

// close layer when click-out
document.onclick = mclose; 
