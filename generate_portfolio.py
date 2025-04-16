import os, yaml

from img_utils import image, skill
from mkhead import mkhead

TARGET=os.environ.get("TARGET","pdf")

with open('personal_details.yaml') as personal_details_src:
	personal_details=yaml.safe_load(personal_details_src)

with open('portfolio.yaml') as portfolio_src:
	portfolio=yaml.safe_load(portfolio_src)

os.makedirs('output', exist_ok=True)
outfile=open(f'output/{personal_details["name"].replace(" ","_")}_portfolio.html', 'w+')
outfile.write('<html>')
outfile.write('<title>My Portfolio</title>')

mkhead(outfile, 'portfolio', TARGET, '1.5em')

outfile.write('<body>')
outfile.write('<div class="portfolio">')
for name, details in portfolio.items():
	video=''

	if youtube := details.get('youtube'):
		video = f'<iframe width="1280" height="720" src="https://www.youtube.com/embed/{youtube}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'

	elif webm := details.get('webm'):
		video = f'''
		<video width="1280" height="720" controls>
			<source src="{webm}" type="video/webm">
		</video>'''

	outfile.write(f'''<div class="portfolio_item">
		<h2>{name}</h2>
		<div>
			<div class="portfolio_item_video">
				{video}
			</div>
			<div class="portfolio_item_text">
				{" ".join([skill(s) for s in details["skills"]])}
				<div class="project_description">{details["description"]}</div>
				<div style="height: 1em"></div>
				<div>
					{f"Try it for yourself: \
					{' '.join([f'<a href="{link}">{label}</a>' for label,link in demos.items()])}" if (demos:=details.get('demos')) else ''}
				</div>
				<div>Source code available at <a href="{details['source']}">{details['source']}</a></div>
			</div>
		</div>
		<div class="sep"></div>
	</div>''')
outfile.write('</div>')
outfile.write('</body>')
outfile.write('</html>')
