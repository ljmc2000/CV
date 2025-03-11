def mkhead(outfile, TARGET='pdf'):
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
				color: #DC1438;
				text-decoration: underline;
				text-weight: bold;
			}''')
		outfile.write('</style>')

	#end head
	outfile.write('<body>')
