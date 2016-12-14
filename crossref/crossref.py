import requests
import json


doi="10.1109/EDUCON.2011.5773299"
url= requests.get("http://api.crossref.org/works/"+doi)
if url.status_code==200:
    print "completo"
    data=json.loads(url.text)
    member=data['message']['member']
    print "DOI:"+ data['message']['DOI']
    print "URL:"+ data['message']['URL']
    print "Miembro "+member.lstrip("http://id.crossref.org/member/"+"\n")
    member=member.lstrip("http://id.crossref.org/member/")


    url_member= requests.get("http://api.crossref.org/members/"+member)
    data_member=json.loads(url_member.text)
    print "Informacion member\n"
    print "Nombre: " + data_member['message']['primary-name']
    print "Locacion: "+data_member['message']['location']
