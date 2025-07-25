import base64, re, subprocess
from os import environ

def asset(filename):
	return 'assets/'+filename

IM_OPTS=environ.get("IM_OPTS")
IM_OPTS=IM_OPTS.split(' ') if IM_OPTS else []

if environ.get('NO_IMG'):
	def image(filename: str, *args, **kargs):
		return f'<img>'

elif IMAGE_SCALE:=float(environ.get('IMAGE_SCALE',0)):
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
	return f'<span class="skill">{skill_name}</span>'

skill_pattern = re.compile(r'skill\(([\w ]+)\)')
def sub_skills(string):
	return skill_pattern.sub(lambda match: skill(match.group(1)), string)
