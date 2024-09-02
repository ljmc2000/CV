import base64, subprocess
from os import environ

BASE_SCALE=float(environ.get('BASE_SCALE', 1.75))
COMPRESS_IMAGES=True if environ.get('COMPRESS_IMAGES', 0) else False

def asset(filename):
	return 'assets/'+filename

if COMPRESS_IMAGES:
	def image(filename: str, height: int, width: int=None, *, scale: int=1, class_names='', style='') -> str:
		if width:
			w=f'{scale*BASE_SCALE*width}'
			width=f'width="{width}" '
		else:
			w=''
			width=''

		h=f'{scale*BASE_SCALE*height}'
		height=f'height="{height}" '

		class_names=f'class="{class_names}" ' if class_names else ""
		style=f'style="{style}" ' if style else ""

		imgmck=subprocess.run(['magick', asset(filename), '-geometry', f'{w}x{h}', 'JPG:-'], stdout=subprocess.PIPE)
		return f'''<img {class_names}{style}{width}{height} src="data: image/jpeg; base64, {base64.b64encode(imgmck.stdout).decode()}">'''

	def skill(skill_name: str) -> str:
		imgmck=subprocess.run(['magick', '-background', 'transparent', f'skill_icons/{skill_name}.svg', '-geometry', f'x{16*BASE_SCALE}', 'WEBP:-'], stdout=subprocess.PIPE)

		if imgmck.returncode==0:
			return f'<button class="skill_badge skill_badge_img"><img src="data: image/png; base64, {base64.b64encode(imgmck.stdout).decode()}"></button>'

		else:
			return f'<button class="skill_badge skill_badge_txt"><img><span>{skill_name}</span></button>'

else:
	def image(filename: str, height: int, width: int=None, *, scale: int=1, class_names='', style='') -> str:
		mimetype=subprocess.run(['file', '-b', '--mime-type', asset(filename)], stdout=subprocess.PIPE)
		width=f'width={width} ' if width else ""
		height=f'height="{height}" '
		class_names=f'class="{class_names}" ' if class_names else ""
		style=f'style="{style}" ' if style else ""

		with open(asset(filename), 'rb') as f:
			return f'<img {class_names}{style}{width}{height} src="data: {mimetype.stdout.decode()}; base64, {base64.b64encode(f.read()).decode()}">'

	def skill(skill_name: str) -> str:
		try:
			with open(f'skill_icons/{skill_name}.svg', 'rb') as skill_icon_src:
				return f'<button class="skill_badge skill_badge_img"><img src="data: image/svg+xml; base64, {base64.b64encode(skill_icon_src.read()).decode()}"></button>'

		except FileNotFoundError:
			return f'<button class="skill_badge skill_badge_txt"><img><span>{skill_name}</span></button>'
