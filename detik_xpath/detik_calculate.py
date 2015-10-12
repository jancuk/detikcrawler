import urllib2, re

def get_size_image(url):
    return urllib2.urlopen(url).info()['Content-Length']

class DetikCalulcate:
    @classmethod
    def calculate_images(self, image_url):
        if re.search("http|cdn|https|www|cnnindonesia", image_url):
            hit_url = image_url
        else:
            hit_url = "http://www.detik.com/%s" % image_url
        try:
            im = get_size_image(hit_url)
            return im
        except:
            try:
                url_http    = hit_url.replace("//","http://")
                im = get_size_image(url_http)
                return im
            except:
                pass
