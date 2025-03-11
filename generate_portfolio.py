import os, yaml

from decorations import li
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
