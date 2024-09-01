import base64, subprocess
from os import environ

BASE_SCALE=1.75
COMPRESS_IMAGES=True if environ.get('COMPRESS_IMAGES', 0) else False

def asset(filename):
	return 'assets/'+filename

def aspect_ratio(filename: str) -> float:
	check=subprocess.run(["magick", "identify", "-format", "%w:%h", asset(filename)], stdout=subprocess.PIPE)
	w,h=check.stdout.decode().split(':')
	return float(w)/float(h)

if COMPRESS_IMAGES:
	def image(filename: str, height: int, width: int=None, *, scale: int=1, class_names='', style='') -> str:
		if not width:
			width=int(height*aspect_ratio(filename))

		dimensions=f'{width}x{height}'
		class_names=f'class="{class_names}" ' if class_names else ""
		style=f'style="{style}" ' if style else ""

		imgmck=subprocess.run(['magick', asset(filename), '-resize', f'{scale*BASE_SCALE*width}x{scale*BASE_SCALE*height}', 'JPG:-'], stdout=subprocess.PIPE)
		return f'''<img {class_names}{style} width="{width}" height="{height}" src="data: image/jpeg; base64, {base64.b64encode(imgmck.stdout).decode()}">'''

	def skill(skill_name: str) -> str:
		imgmck=subprocess.run(['magick', '-background', 'transparent', f'skill_icons/{skill_name}.svg', '-geometry', f'x{12*BASE_SCALE}', 'WEBP:-'], stdout=subprocess.PIPE)

		if imgmck.returncode==0:
			return f'<button class="skill_badge"><img class="skill_badge_img" src="data: image/png; base64, {base64.b64encode(imgmck.stdout).decode()}"></button>'

		else:
			return f'<button class="skill_badge"><img><span class="skill_badge_txt">{skill_name}</span></button>'

else:
	def image(filename: str, height: int, width: int=None, *, scale: int=1, class_names='', style='') -> str:
		mimetype=subprocess.run(['file', '-b', '--mime-type', asset(filename)], stdout=subprocess.PIPE)
		width=f'width={width} ' if width else ""
		class_names=f'class="{class_names}" ' if class_names else ""
		style=f'style="{style}" ' if style else ""

		with open(asset(filename), 'rb') as f:
			return f'<img {class_names}{style}{width} height="{height}" src="data: {mimetype.stdout.decode()}; base64, {base64.b64encode(f.read()).decode()}">'

	def skill(skill_name: str) -> str:
		try:
			with open(f'skill_icons/{skill_name}.svg', 'rb') as skill_icon_src:
				return f'<button class="skill_badge"><img class="skill_badge_img" src="data: image/svg+xml; base64, {base64.b64encode(skill_icon_src.read()).decode()}"></button>'

		except FileNotFoundError:
			return f'<button class="skill_badge"><img><span class="skill_badge_txt">{skill_name}</span></button>'
