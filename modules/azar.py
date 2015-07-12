import urllib2
import json
def wpes(phenny, input):
    random = urllib2.urlopen("http://es.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&format=json")
    data = json.loads(random.read())
    pages = data["query"]["random"]
    ## print [page["title"] for page in pages]
    ## print pages
    ## print page
    ## print pages[0]
    ## print pages[0]["title"]
    article = pages[0]["title"]
    link = 'http://es.wikipedia.org/wiki/' + article
    finalink = link.replace (" ", "_") ; 
    phenny.say( finalink )
wpes.command = ['azar']
wpes.priority = 'high'
