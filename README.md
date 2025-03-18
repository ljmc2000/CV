# Dependencies
- Requires python
- Requires imagemagick and file to generate a CV with compressed images

# HTML
run generate_cv.py to build HTML version of CV  
run generate_portfolio.py to build portfolio  
run generate_all.sh to generate both

# Variables
HTML generation is subject to the following environment variables

| name        | type  | description                                                         |
|-------------|-------|---------------------------------------------------------------------|
| IM_OPTS     | str   | arguments to be passed to imagemagick                               |
| IMAGE_SCALE | float | if passed, convert images to png at at 96dpi times IMAGE_SCALE      |
| NO_IMG      | int   | if not 0 or None, generate the HTML without any images              |
| TARGET      | str   | if set to print, generate a different CV optimized for B&W printing |

# PDF
To generate pdf from html just use the print function of your favorite browser
