import yaml

from img_utils import image, svg

with open('personal_details.yaml') as personal_details_src:
	personal_details=yaml.safe_load(personal_details_src)

with open('experience.yaml') as experience_src:
	experience=yaml.safe_load(experience_src)

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
<div style="display: inline-flex">{image('me2023.jpg',136)}<div class="aboutme invisible_links"><div style="font-size: 24px; padding-bottom: 6px">{personal_details["name"]}</div>''')

for link, label, icon in [
	('mailto:'+personal_details["email"], personal_details["email"], 'email-1572-svgrepo-com.svg'),
	('https://github.com/ljmc2000', 'github.com/ljmc2000', 'github.svg'),
	(personal_details['linkedin_final'], personal_details['linkedin'], 'iconmonstr-linkedin-3.svg'),
	]:
	outfile.write(f'''<div><a href={link}>{image(icon,16)} {label}</a></div>''')
outfile.write(f'''<div>{image('cell-phone-svgrepo-com.svg',16)} {personal_details["cellnumber"]}</div>''')

outfile.write('</div></div>')

#Experience
outfile.write('<div class="section_header">Experience</div>')
for company, details in experience.items():
	outfile.write(f'''
	<div class="job_outline">
		<b>{details["start_date"]} to {details["end_date"]}:</b> {details["title"]} at {company}
	</div>''')

	if tech_stack:=details.get('tech_stack'):
		outfile.write('<div>')
		for tech in tech_stack:
			outfile.write(f'<button class="skill_badge">{tech}</button>')
		outfile.write('</div>')

	if duties:=details.get('duties'):
		outfile.write('<ul class="job_details">')
		for duty in duties:
			outfile.write(f'<li>{duty}</li>')
		outfile.write('</ul>')

#Education
outfile.write(f'''<div class="section_header">Education and Certifications</div>
	<div> <b>Bachelor of Science in Computer Science (Infrastructure)</b> | First Class Honors | <i>Technological University of Dublin</i> | Sep 2016 - Jun 2020 </div>
	<div> <b>Leaving Certificate</b> | 410 points | <i>St. Josephs CBS</i> | Sep 2010 - Jun 2016 </div>
	<div> <b>KNIME L3 Certificate</b> | April 2021 </div>
''')

#end
outfile.write('</body></html>')
