import yaml

from img_utils import image, svg

with open('personal_details.yaml') as personal_details_src:
	personal_details=yaml.safe_load(personal_details_src)

outfile=open("LiamMcCormick_CV.html", "w+")
outfile.write('<html>')

#head
outfile.write('<head>')

#style
with open('styles.css') as styles:
	outfile.write('<style>')
	outfile.write(styles.read())
	outfile.write('</style>')

#end head, begin body
outfile.write('</head><body>')

#about me
outfile.write(f'''
<div style="display: inline-flex">{image('me2023.jpg',136)}<div class="aboutme invisible-links"><div style="font-size: 24px; padding-bottom: 6px">{personal_details["name"]}</div>''')

for link, label, icon in [
	('mailto:'+personal_details["email"], personal_details["email"], 'email-1572-svgrepo-com.svg'),
	('https://github.com/ljmc2000', 'github.com/ljmc2000', 'github.svg'),
	(personal_details['linkedin_final'], personal_details['linkedin'], 'iconmonstr-linkedin-3.svg'),
	]:
	outfile.write(f'''<div><a href={link}>{image(icon,16,scale=2)} {label}''')
outfile.write(f'''<div>{image('cell-phone-svgrepo-com.svg',16,scale=2)} {personal_details["cellnumber"]}''')

outfile.write('</div></div>')

#end
outfile.write('</body></html>')
