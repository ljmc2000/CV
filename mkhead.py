def mkhead(outfile, TARGET='pdf', font_size='12px'):
	#head
	outfile.write('<head>')

	#utf8
	outfile.write('<meta charset="UTF-8">')

	#style
	with open('styles.css') as styles:
		outfile.write('<style>')
		outfile.write(f'body {{ font-size: {font_size}; }}')
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
				color: #DC1438;
				text-decoration: underline;
				text-weight: bold;
			}''')
		outfile.write('</style>')

	outfile.write('</head>')
