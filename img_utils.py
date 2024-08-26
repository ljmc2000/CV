import base64, subprocess

def asset(filename):
	return 'assets/'+filename

def aspect_ratio(filename: str) -> float:
	check=subprocess.run(["magick", "identify", "-format", "%w:%h", asset(filename)], stdout=subprocess.PIPE)
	w,h=check.stdout.decode().split(':')
	return float(w)/float(h)

def image(filename: str, height: int, width: int=None, *, scale: int=1, class_names='', style='') -> str:
	if not width:
		width=int(height*aspect_ratio(filename))

	dimensions=f'{width}x{height}'
	class_names=f'class="{class_names}" ' if class_names else ""
	style=f'style="{style}" ' if style else ""

	imgmck=subprocess.run(['magick', asset(filename), '-resize', f'{scale*width}x{scale*height}', 'JPG:-'], stdout=subprocess.PIPE)
	return f'''<img {class_names}{style} width="{width}" height="{height}" src="data: image/jpeg; base64, {base64.b64encode(imgmck.stdout).decode()}">'''

def svg(filename: str):
	with open(asset(filename)) as ext_file:
		return ext_file.read()
