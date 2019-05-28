import urllib.request
import ssl
class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None
        
        ssl._create_default_https_context = ssl._create_unverified_context
        opener = urllib.request.build_opener(urllib.request.HTTPSHandler())
        urllib.request.install_opener(opener)
        response = urllib.request.urlopen(url)
        if response.getcode()!=200:
            return None
        
        return response.read()

