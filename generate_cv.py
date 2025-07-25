import os, yaml

from img_utils import image, skill, sub_skills
from mkhead import mkhead

TARGET=os.environ.get("TARGET","pdf")

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
mkhead(outfile, 'cv', TARGET, font_size='16px')
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
td(personal_details["email"], 'email-1572-svgrepo-com.svg', link='mailto:'+personal_details["email"], colspan=2)
outfile.write('</tr><tr>')
td("delilahsthings.ie", 'Globe_icon.svg', link="https://delilahsthings.ie")
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
outfile.write('''I am a TU qualified Software Developer with over 3-years' experience on IT teams in international financial institutions. I also maintain an open source android application called <a href="https://f-droid.org/en/packages/ie.delilahsthings.soothingloop/">Soothing Noise Player</a> with over 40 stars on GitHub. I learn quickly and work with a high level of attention to detail. I am quick to identify problems and tenaciously seek solutions. Being part of a team, I can be depended on to work collaboratively or independently as required. Continuous learning is important for my curious mind.''')
outfile.write('<div style="height: .75em"></div>')
outfile.write('I am eligible for the <a href="https://jobsplus.ie">JobsPlus Incentive</a>. A prospective employer could be entitled to a grant of €7,500 payable over 18 months.')
outfile.write('</div>')

#Experience
outfile.write('<div class="section">')
outfile.write('<div class="section_header">Experience</div>')
for company, details in experience.items():
	outfile.write(f'''
	<div class="job_outline">
		<b>{details["start_date"]} to {details["end_date"]}:</b> {details["title"]} at {company}{', '+company_summary if (company_summary:=details.get("company_summary")) else None}
	</div>''')

	if duties:=details.get('duties'):
		outfile.write(bullet_points(duties, className='job_details'))
outfile.write('</div>')

#Key Skills
outfile.write('<div class="section">')
outfile.write('<div class="section_header">Key Skills</div>')
outfile.write(bullet_points(key_skills))
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
outfile.write('<div class="footer">')
outfile.write('<div class="references">References available upon request</div>')
outfile.write('<div class="thanks4reading">Thank you for your time in reading my CV</div>')
outfile.write('</div>')

#end
outfile.write('</body></html>')
