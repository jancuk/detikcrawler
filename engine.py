import urllib2, cStringIO, re
from detik_xpath import DetikXpath
from detik_xpath import DetikCalulcate
from PIL import Image

URL = "http://detik.com"
TOTAL_WIDTH     = 0
TOTAL_HEIGHT    = 0

responses       = DetikXpath.parsing_html(URL)
total_images    = len(responses)

for image in responses:
    im = DetikCalulcate.calculate_images(image["src"])
    TOTAL_WIDTH  += im.size[0]
    TOTAL_HEIGHT += im.size[1]

print ""
print "==== RESULT ===="
print ""
print "Total Images is (%d)" % total_images
print "TOTAL WIDTH (%d)" % TOTAL_WIDTH
print "TOTAL HEIGHT (%d)" % TOTAL_HEIGHT
