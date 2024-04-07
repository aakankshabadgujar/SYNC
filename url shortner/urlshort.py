import pyshorteners
url = input('Enter the url: ')

def shorteurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))
    
shorteurl(url)