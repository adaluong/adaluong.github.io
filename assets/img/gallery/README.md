# getting the photos on the website
perhaps there's a better way to do this, but for now:
* place photos into a folder
* strip all exif metadata (via Adobe Lightroom or otherwise)
* run the `img_html` script on the folder to generate the html
* add the generated html to `_pages/gallery.md`, rearranging as you wish