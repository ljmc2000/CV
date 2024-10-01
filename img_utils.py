import base64, subprocess
from os import environ

def asset(filename):
	return 'assets/'+filename

IM_OPTS=environ.get("IM_OPTS")
IM_OPTS=IM_OPTS.split(' ') if IM_OPTS else []

if IMAGE_SCALE:=float(environ.get('IMAGE_SCALE',0)):
	def image(filename: str, height: int, width: int=None, *, scale: int=1, class_names='', style='') -> str:
		if width:
			w=f'{scale*IMAGE_SCALE*width}'
			width=f'width: {width}px;'
		else:
			w=''
			width=''

		h=f'{scale*IMAGE_SCALE*height}'
		height=f'height: {height}px;'

		class_names=f'class="{class_names}" ' if class_names else ""
		style=f'style="{width}{height}{style}"'

		imgmck=subprocess.run(['magick', asset(filename), '-geometry', f'{w}x{h}', *IM_OPTS, 'JPG:-'], stdout=subprocess.PIPE)
		return f'''<img {class_names}{style} src="data: image/jpeg; base64, {base64.b64encode(imgmck.stdout).decode()}">'''

	def skill(skill_name: str) -> str:
		imgmck=subprocess.run(['magick', '-background', 'transparent', f'skill_icons/{skill_name}.svg', '-geometry', f'x{16*IMAGE_SCALE}', *IM_OPTS, 'WEBP:-'], stdout=subprocess.PIPE)

		if imgmck.returncode==0:
			return f'<img class="skill_badge_img" src="data: image/png; base64, {base64.b64encode(imgmck.stdout).decode()}">'

		else:
			return f'<span>{skill_name}</span>'

else:
	def image(filename: str, height: int, width: int=None, *, scale: int=1, class_names='', style='') -> str:
		mimetype=subprocess.run(['file', '-b', '--mime-type', asset(filename)], stdout=subprocess.PIPE)
		width=f'width: {width}px; ' if width else ""
		height=f'height: {height}px; '
		class_names=f'class="{class_names}" ' if class_names else ""
		style=f'style="{width}{height}{style}" '

		with open(asset(filename), 'rb') as f:
			return f'<img {class_names}{style} src="data: {mimetype.stdout.decode()}; base64, {base64.b64encode(f.read()).decode()}">'

	def skill(skill_name: str) -> str:
		try:
			with open(f'skill_icons/{skill_name}.svg', 'rb') as skill_icon_src:
				return f'<img class="skill_badge_img" src="data: image/svg+xml; base64, {base64.b64encode(skill_icon_src.read()).decode()}">'

		except FileNotFoundError:
			return f'<span>{skill_name}</span>'
