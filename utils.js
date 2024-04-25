#ifndef CV_UTILS_H
#define CV_UTILS_H
#include "configuration.h"

function set_image(image, src, height)
{
	var img=new Image()
	img.src=src

	img.addEventListener("load",(e) => {
		var canvas = document.createElement("canvas")
		var ctx=canvas.getContext("2d")
		canvas.height = height*IMAGE_SCALE
		canvas.width = height/img.naturalHeight*img.naturalWidth*IMAGE_SCALE
		if(canvas.height>image.naturalHeight || canvas.width>canvas.naturalWidth)
			return
		ctx.drawImage(img, 0, 0, canvas.width, canvas.height)
		image.crossOrigin = ""
		image.src=canvas.toDataURL()
	})
}

function href(i,src)
{
	var a=document.createElement("a")
	a.href=src
	a.appendChild(i)
	return a
}

#endif
