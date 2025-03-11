import os, yaml

from decorations import li
from img_utils import image, skill
from mkhead import mkhead

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

os.makedirs('output', exist_ok=True)
outfile=open(f'output/{personal_details["name"].replace(" ","_")}_CV.html', 'w+')
outfile.write('<html>')
mkhead(outfile, TARGET)
outfile.write('<body>')

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

#Profile
outfile.write('<div class="section_header">Profile</div>')
outfile.write('''A tenacious, precise individual with 3 years experience in the technology sector. Capable of rapidly and accurately learning new tools as well a producing efficient, maintainable code. Currently seeking any manor of IT position in order to utilize and expand IT skills. Full category B drivers license''')

#Key Skills
outfile.write('<div class="section_header">Key Skills</div>')
outfile.write('''<ul>
	<li>3 years professional experience in several tech stacks mostly involving Java, but also including Spring, MySQL, Selenium and JavaScript</li>
	<li>Full time linux user across several distros including debian, atomic fedora and archlinux</li>
	<li>Creator of documentation in both video and textual formats</li>
	<li>Concise communicator</li>
</ul>''')

#Experience
outfile.write('<div class="section_header">Experience</div>')
for company, details in experience.items():
	outfile.write(f'''
	<div class="job_outline">
		<b>{details["start_date"]} to {details["end_date"]}:</b> {details["title"]} at {company}{', '+company_summary if (company_summary:=details.get("company_summary")) else None}
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
	outfile.write('<div class="education_item"><div class="top">')
	outfile.write(f'{certification["title"]}')
	outfile.write(f'<div class="date">{certification["attended"]}</div>')
	if subject:=certification.get("subject"):
		outfile.write(f' in {subject}')
	if grade:=certification.get("grade"):
		outfile.write(f', {grade}')
	outfile.write('</div>')

	outfile.write(f'<i>{certification["institution"]}</i>')

	if skills:=certification.get('skills'):
		outfile.write('<div class="education_item_skills">')
		outfile.write(" • ".join([skill(s) for s in skills]))
		outfile.write('</div>')
		# outfile.write('<table class="education_skills_table"><tr>')
		# for i, s in enumerate(certification['skills']):
		# 	if i%10==0 and i!=0:
		# 		outfile.write('</tr><tr>')
		# 	outfile.write(f'<td>{skill(s)}</td>')
		# outfile.write('</tr></table>')
	outfile.write('</div>')

#Skills
#outfile.write('<div class="section_header">Other Skills</div>')
#outfile.write(" • ".join([skill(s) for s in misc_skills]))

#Hobbies
outfile.write('<div class="section_header">Hobbies</div><ul>')
for hobby in hobbies:
	outfile.write(f'<li>{hobby}</li>')
outfile.write('</ul>')

#footer
outfile.write('<div class="references">References available upon request</div>')

#end
outfile.write('</body></html>')
