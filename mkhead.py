def mkhead(outfile, extra_styles, TARGET='pdf', font_size='12px'):
	#head
	outfile.write('<head>')

	#utf8
	outfile.write('<meta charset="UTF-8">')

	#style
	with open('styles_common.css') as styles, open(f'styles_{extra_styles}.css') as extra_styles:
		outfile.write('<style>')
		outfile.write(f'body {{ font-size: {font_size}; }}')
		outfile.write(styles.read())
		outfile.write(extra_styles.read())
		if TARGET=="print":
			outfile.write('''
			.IMPORTANT {
				text-decoration: underline;
				text-weight: bold;
			}''')
		else:
			outfile.write('''
			.IMPORTANT {
				color: #DC1438;
				text-decoration: underline;
				text-weight: bold;
			}''')
		outfile.write('</style>')

	outfile.write('</head>')
