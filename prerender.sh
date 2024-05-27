gcc -P -E -w -x c CV.html -o CV_intermediate.html
#wkhtmltopdf --enable-local-file-access --encoding utf-8 CV_intermediate.html LiamMcCormick_CV.pdf
#ls -lh LiamMcCormick_CV.pdf | awk '{print "generated a " $5 " CV"}'
