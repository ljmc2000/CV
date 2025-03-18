import os, yaml

from img_utils import image, skill, sub_skills
from mkhead import mkhead

TARGET=os.environ.get("TARGET","pdf")

with open('additional_achievements.yaml') as additional_achievements_src:
	additional_achievements=yaml.safe_load(additional_achievements_src)

with open('education.yaml') as education_src:
	education=yaml.safe_load(education_src)

with open('experience.yaml') as experience_src:
	experience=yaml.safe_load(experience_src)

with open('hobbies.yaml') as hobbies_src:
	hobbies=yaml.safe_load(hobbies_src)

with open('key_skills.yaml') as key_skills_src:
	key_skills=yaml.safe_load(key_skills_src)

with open('misc_skills.yaml') as misc_skills_src:
	misc_skills=yaml.safe_load(misc_skills_src)

with open('personal_details.yaml') as personal_details_src:
	personal_details=yaml.safe_load(personal_details_src)

#util functions
def bullet_points(points, *, className=None) -> str:
	return f'''<ul{f' class="{className}"' if className else ''}>{'\n\t'.join(['<li>'+sub_skills(point)+'</li>' for point in points])}</ul>'''

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
outfile.write('<div class="section">')
outfile.write('<div class="section_header">Profile</div>')
outfile.write('''A passionate software developer with excellent written and oral English language communication skills. A fast learner with a high level of attention to detail. A dependable team player who who will not hesitate to make the problems of my team my own. An unusual mind capable of seeing solutions most cannot. A curious soul who never tires of learning new things.''')
outfile.write('</div>')

#Key Skills
outfile.write('<div class="section">')
outfile.write('<div class="section_header">Key Skills</div>')
outfile.write(bullet_points(key_skills))
outfile.write('</div>')

#Experience
outfile.write('<div class="section">')
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
		outfile.write(bullet_points(duties, className='job_details'))
outfile.write('</div>')

#Additional Achievements
outfile.write('<div class="section">')
outfile.write('<div class="section_header">Additional Achievements</div>')
outfile.write(bullet_points(additional_achievements))
outfile.write('</div>')

#Education
outfile.write('<div class="section">')
outfile.write(f'''<div class="section_header">Education</div>''')
for certification in education:
	outfile.write('<div class="education_item"><div class="top">')
	outfile.write(f'{certification["title"]}')
	if subject:=certification.get("subject"):
		outfile.write(f' in {subject}')
	if grade:=certification.get("grade"):
		outfile.write(f', {grade}')
	outfile.write(f' ({certification["attended"]})')
	outfile.write('</div>')

	outfile.write(f'<i>{certification["institution"]}</i>')

	if skills:=certification.get('skills'):
		outfile.write('<div class="education_item_skills">')
		outfile.write(" • ".join([skill(s) for s in skills]))
		outfile.write('</div>')
	outfile.write('</div>')
outfile.write('</div>')

#Skills
#outfile.write('<div class="section_header">Other Skills</div>')
#outfile.write(" • ".join([skill(s) for s in misc_skills]))

#Hobbies
outfile.write('<div class="section">')
outfile.write('<div class="section_header">Hobbies</div>')
outfile.write(bullet_points(hobbies, className="multi_column_list"))
outfile.write('</div>')

#footer
outfile.write('<div class="references">References available upon request</div>')

#end
outfile.write('</body></html>')
