import urllib2

response = urllib2.urlopen("https://kist.edu.np")
page_source = response.read()
print("data",data)
jsonD = json.dumps(htmlContent.text)
jsonL = json.loads(jsonD)

ContentUrl='{ \"url\" : \"'+str(urls)+'\" ,'+"\n"+' \"uid\" : \"'+str(uniqueID)+'\" ,\n\"page_content\" : \"'+jsonL+'\" , \n\"date\" : \"'+finalDate+'\"}'