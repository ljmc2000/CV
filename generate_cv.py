import yaml

from decorations import li, skill
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
			outfile.write(skill(tech))
		outfile.write('</div>')

	if duties:=details.get('duties'):
		outfile.write('<ul class="job_details">')
		for duty in duties:
			outfile.write(li(duty))
		outfile.write('</ul>')

#Education
outfile.write(f'''<div class="section_header">Education and Certifications</div>
	<div>
		<b>Bachelor of Science</b> in <b>Computer Science (Infrastructure)</b> from <i>TU Dublin</i> | Sep 2016 - Jun 2020 <br>
		<span class="grade_indicator">First Class Honors</span>
		{" ".join([skill(s) for s in ('Algorithms', 'Android Development', 'Basic Pen Testing', 'C', 'Cloud Computing', 'Database Admin', 'Databases', 'Docker', 'Java', 'Linux OS', 'Microsoft Azure', 'MongoDB', 'Maths', 'Networking', 'PHP', 'Program Design', 'Python', 'Python Flask', 'TCP Sockets', 'UDP Sockets', 'UI design', 'Unity Engine', 'Virtual Machines', 'Web Development')])}
	</div>
	<div>
		<b>Leaving Certificate</b> from <i>St. Josephs CBS</i> | Sep 2010 - Jun 2016 <br>
		<span class="grade_indicator">410 points</span>
		{" ".join([skill(s) for s in ('English', 'Irish', 'Mathmatics', 'History', 'Music', 'Chemistry', 'Spanish')])}
	</div>
	<div>
		<b>KNIME L3 Certificate</b> | April 2021 <br>
		{skill("KNIME")}
	</div>
''')

#end
outfile.write('</body></html>')
