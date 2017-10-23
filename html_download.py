import urllib.request
class HtmlDownloader(object):
    def download(self, url):
        print('download...')
        if url is None:
            return None
        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None

        # pout = open('output_urls.html', 'w')
        # pout.write(response.read().decode('utf-8'))
        return response.read()