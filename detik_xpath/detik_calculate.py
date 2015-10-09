import urllib2, cStringIO, re
from PIL import Image

def fetch_url(url):
    return urllib2.urlopen(url)

def fetch_source_images(url):
    return cStringIO.StringIO(url)

def image_open_by_url(url):
    return Image.open(url)

class DetikCalulcate:
    @classmethod
    def calculate_images(self,image_url):
        if re.search("http|cdn|https|www|cnnindonesia", image_url):
            hit_url = image_url
        else:
            hit_url = "http://www.detik.com/%s" % image_url
        try:
            file_image = fetch_source_images(fetch_url(hit_url).read())
            im = image_open_by_url(file_image)
            return im
        except:
            try:
                url_http    = hit_url.replace("//","http://")
                file_image  = fetch_source_images(fetch_url(url_http).read())
                im = image_open_by_url(file_image)
                return im
            except:
                print hit_url
