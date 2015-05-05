import scraperwiki
import lxml.html
import datetime
import time
import re

from threading import Thread
url = ['http://www.indiegogo.com/projects?filter_category=Technology&filter_country=CTRY_US&filter_quick=popular_all&pg_num=']
for x in url:
    def indiegogo():
        for i in range(1,4):
            try:
                url = x+str(i)
                print 'url: ' + str(url)
                root = scraperwiki.scrape(url)
                content = lxml.html.etree.HTML(root)
                categorie = content.xpath('//div[contains(@class,"project-category")]')
                nom = content.xpath('//div[contains(@class,"project-details")]/a')
                #porteur_projet = content.xpath('//p[contains(@class,"creator")]/a')
                porteur_projet = content.xpath('//p[contains(@class,"creator")]/span/a')
                details = content.xpath('//p[contains(@class,"description")]')
                stats = content.xpath('//span[contains(@id,"project-stats-funding-pct")]')
                montant = content.xpath('//span[contains(@class,"currency currency-medium")]/span')
                lien = content.xpath('//div[contains(@class,"project-details")]/a[@href]')
                for karazana,projet,olona,deta,marika,vola,rohy in zip(categorie,nom,porteur_projet,details,stats,montant,lien):
            #print olona.text,asa.text,deta.text,marika.text,vola.text
                    data = {
                                'Categorie': karazana.text,
                                'Projet' : projet.text,
                                'Nom du porteur': olona.text,
                                'details': deta.text,
                                'statistique': marika.text,
                                'montant obtenu': vola.text,
                                'lien':  "http://www.indiegogo.com"+rohy.attrib.get('href'),
                                'date' : datetime.datetime.now()
                            }
                    scraperwiki.sqlite.save(unique_keys=['Projet'], data=data)


            except:
                print "None"
    t = Thread(target=indiegogo)
    t.start()
    
