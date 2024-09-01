import yaml

from decorations import li
from img_utils import image, skill

with open('education.yaml') as education_src:
	education=yaml.safe_load(education_src)

with open('experience.yaml') as experience_src:
	experience=yaml.safe_load(experience_src)

with open('hobbies.yaml') as hobbies_src:
	hobbies=yaml.safe_load(hobbies_src)

with open('misc_skills.yaml') as misc_skills_src:
	misc_skills=yaml.safe_load(misc_skills_src)

with open('personal_details.yaml') as personal_details_src:
	personal_details=yaml.safe_load(personal_details_src)

with open('portfolio.yaml') as portfolio_src:
	portfolio=yaml.safe_load(portfolio_src)

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
		<mark>
			<b>{details["start_date"]} to {details["end_date"]}:</b> {details["title"]} at {company}
		</mark>
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
outfile.write(f'''<div class="section_header">Education and Certifications</div>''')
for certification in education:
	outfile.write(f'''
		<div class="education_item">
			<div class="education_item_header"><mark>{certification['html']}</mark></div>
			{" ".join([skill(s) for s in certification['skills']])}
		</div>
	''')

#Skills
outfile.write('<div class="section_header">Other Skills</div>')
for s in misc_skills:
	outfile.write(skill(s))

#Hobbies
outfile.write('<div class="section_header">Hobbies</div><ul>')
for hobby in hobbies:
	outfile.write(f'<li>{hobby}</li>')
outfile.write('</ul>')

#new page
outfile.write('<div class="new-page"></div>')

#Portfolio
outfile.write(f'<div class="section_header">Portfolio</div>')
i=0
for name, details in portfolio.items():
	if i%2==0:
		outfile.write('<div class="portfolio_row">')

	outfile.write(f'''<div class="portfolio_item">
		{image(details["preview"], 180, 180, class_names="portfolio_item_preview")}
		<h3>{name}</h3>
		<a href="{details['source']}">{details['source'].replace('ljmc2000/',"ljmc2000/<wbr>")}</a>
		{"/".join([f'<a class="ultravisible_link" href="{link}">{label}</a>' for (label, link) in details["demos"].items()])}<br>
		{"".join([skill(s) for s in details["skills"]])}
		<div class="project_description">{details["description"]}</div>
	</div>''')

	if i%2==1:
		outfile.write('</div>')

	i+=1

outfile.write('<div class="references">References available upon request</div>')

#end
outfile.write('</body></html>')
