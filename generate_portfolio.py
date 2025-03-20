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

mkhead(outfile, TARGET)

outfile.write('<body>')
outfile.write('<div class="portfolio">')
for name, details in portfolio.items():
	outfile.write(f'''<div class="portfolio_item">
		{image(details["preview"], 180, 180, class_names="portfolio_item_preview")}
		<div>
			<span class="portfolio_item_name">{name}</span>
			<a href="{details['video']}">Demo Video</a>
		</div>
		{" ".join([skill(s) for s in details["skills"]])}
		<div class="project_description">{details["description"]}</div>
		<div>
			{f"Try it for yourself: \
			{' '.join([f'<a href="{link}">{label}</a>' for label,link in demos.items()])}" if (demos:=details.get('demos')) else ''}
		</div>
		<div>Source code available at <a href="{details['source']}">{details['source']}</a></div>
		<div class="sep"></div>
	</div>''')
outfile.write('</div>')
outfile.write('</body>')
outfile.write('</html>')
