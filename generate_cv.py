import os, yaml

from decorations import li
from img_utils import image, skill

TARGET=os.environ.get("TARGET","pdf")

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

os.makedirs('output', exist_ok=True)
outfile=open(f'output/{personal_details["name"].replace(" ","_")}_CV.html', 'w+')
outfile.write('<html>')

#head
outfile.write('<head>')

#style
with open('styles.css') as styles:
	outfile.write('<style>')
	outfile.write(styles.read())
	if TARGET=="print":
		outfile.write('''
		.IMPORTANT {
			text-decoration: underline;
			text-weight: bold;
		}''')
	else:
		outfile.write('''
		.IMPORTANT {
			color: red;
			text-decoration: underline;
			text-weight: bold;
		}''')
	outfile.write('</style>')

#end head, begin body
outfile.write('</head><body>')

#about me
def td(label: str, icon, *, link=None, colspan=1) -> str:
	if link:
		outfile.write(f'<td colspan="{colspan}"><a href={link}>{image(icon,16)} {label}</a></td>')
	else:
		outfile.write(f'<td colspan="{colspan}">{image(icon,16)} {label}</td>')

outfile.write(f'''<table class="aboutme invisible_links">''')
outfile.write(f'''<tr><td colspan="2" style="font-size: 24px; text-align: center; padding-bottom: 6px">{personal_details["name"]}</td></tr>''')

outfile.write('<tr>')
td(personal_details["email"], 'email-1572-svgrepo-com.svg', link='mailto:'+personal_details["email"])
td(personal_details["cellnumber"], 'cell-phone-svgrepo-com.svg')
outfile.write('</tr><tr>')
td('github.com/ljmc2000', 'github.svg', link='https://github.com/ljmc2000')
td(personal_details["address"], 'house-svgrepo-com.svg')
outfile.write('</tr><tr>')
td(personal_details['linkedin'], 'iconmonstr-linkedin-3.svg', link=personal_details['linkedin_final'], colspan=2)
outfile.write('</tr></table>')

#Experience
outfile.write('<div class="section_header">Experience</div>')
for company, details in experience.items():
	outfile.write(f'''
	<div class="job_outline">
		<b>{details["start_date"]} to {details["end_date"]}:</b> {details["title"]} at {company}
	</div>''')

	if tech_stack:=details.get('tech_stack'):
		outfile.write('<div>')
		outfile.write(' • '.join([skill(tech) for tech in tech_stack]))
		outfile.write('</div>')

	if duties:=details.get('duties'):
		outfile.write('<ul class="job_details">')
		for duty in duties:
			outfile.write(li(duty))
		outfile.write('</ul>')

#Education
outfile.write(f'''<div class="section_header">Education</div>''')
for certification in education:
	outfile.write('<div class="education_item">')
	outfile.write(f'<div class="education_institution">{certification['institution']}</div>')
	outfile.write('<div class="education_item_details">')
	outfile.write(f'<i>{certification['title']}</i>')
	if subject:=certification.get('subject'):
		outfile.write(f', {subject}')
	outfile.write('<div>')
	outfile.write(certification['attended'])
	if grade:=certification.get('grade'):
		outfile.write(f', {grade}')
	outfile.write('</div></div>')
	outfile.write(" • ".join([skill(s) for s in certification['skills']]))
	outfile.write('</div>')

#Skills
outfile.write('<div class="section_header">Other Skills</div>')
outfile.write(" • ".join([skill(s) for s in misc_skills]))

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
	even = i%2==0
	if even:
		outfile.write('<div class="portfolio_row">')

	outfile.write(f'''<div class="portfolio_item {"portfolio_item_left" if even else 'portfolio_item_right'}">
		{image(details["preview"], 180, 180, class_names="portfolio_item_preview")}
		<h3>{name}</h3>
		<a href="{details['source']}">{details['source'].replace('ljmc2000/',"ljmc2000/<wbr>")}</a>
		{"/".join([f'<a class="ultravisible_link" href="{link}">{label}</a>' for (label, link) in details["demos"].items()]) if TARGET!="print" else ""}<br>
		{" ".join([skill(s) for s in details["skills"]])}
		<div class="project_description">{details["description"]}</div>
	</div>''')

	if i%2==1:
		outfile.write('</div>')

	i+=1

outfile.write('<div class="references">References available upon request</div>')

#end
outfile.write('</body></html>')
