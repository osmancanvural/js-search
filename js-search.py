import requests
import sys

links = str(sys.argv[1])
keywords = str(sys.argv[2])
output_file = str(sys.argv[3])

f = open(links, "r")
k = open(keywords, "r")
o = open(output_file, "w")

js_urls = f.readlines()
search_keywords = k.readlines()

for url in js_urls:
	if url.strip() != "":
		url = url[:-1]
		x = requests.get(url, headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
			})
		o.write("\n url = " + url+"\n"+"found keywords = ")

		for keyword in search_keywords:
			if keyword.strip() != "":
				keyword = keyword[:-1]
				if keyword in x.text:
					o.write(keyword+" ")
f.close()
k.close()
o.close()
