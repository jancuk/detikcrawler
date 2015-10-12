from detik_xpath import DetikXpath
from detik_xpath import DetikCalulcate

URL = "http://detik.com"
TOTAL_SIZE      = 0

responses       = DetikXpath.parsing_html(URL)
total_images    = len(responses)

for image in responses:
    try:
        im = DetikCalulcate.calculate_images(image["src"])
        TOTAL_SIZE += int(im)
    except:
        print "failed"
        print image["src"]

print ""
print "==== RESULT ===="
print ""
print "Total Images is (%d)" % total_images
print "TOTAL SIZE / Content Length (%d)" % TOTAL_SIZE
