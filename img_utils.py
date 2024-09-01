import base64, subprocess

BASE_SCALE=1.75

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

	imgmck=subprocess.run(['magick', asset(filename), '-resize', f'{scale*BASE_SCALE*width}x{scale*BASE_SCALE*height}', 'JPG:-'], stdout=subprocess.PIPE)
	return f'''<img {class_names}{style} width="{width}" height="{height}" src="data: image/jpeg; base64, {base64.b64encode(imgmck.stdout).decode()}">'''

def skill(skill_name: str) -> str:
	try:
		with open(f'skill_icons/{skill_name}.svg', 'rb') as skill_icon_src:
			return f'<button class="skill_badge"><img class="skill_badge_img" src="data: image/svg+xml; base64, {base64.b64encode(skill_icon_src.read()).decode()}"></button>'

	except FileNotFoundError:
		return f'<button class="skill_badge"><img><span class="skill_badge_txt">{skill_name}</span></button>'

def svg(filename: str, height: int) -> str:
	with open(asset(filename), 'rb') as f:
		return f'<img height="{height}" src="data: image/svg+xml; base64, {base64.b64encode(f.read()).decode()}">'
