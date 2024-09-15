import scrapy
import json
from pathlib import Path
import re

class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["telegraphindia.com"]
    
    # Adding all URLs to scrape
    start_urls = [
        "https://www.telegraphindia.com/india/share-live-location-on-whatsapp-stay-on-call-with-cops-haryana-polices-new-drive-for-womens-safety/cid/2048126",
        "https://www.telegraphindia.com/india/prime-minister-narendra-modi-bangladeshi-rohingya-infiltration-major-threat-to-jharkhand/cid/2048130",
        "https://www.telegraphindia.com/india/all-doctors-to-have-unique-ids-national-medical-commission-starts-registration-on-its-portal/cid/2048125",
        "https://www.telegraphindia.com/india/deepika-padukone-discharged-from-hospital-after-giving-birth-to-baby-girl/cid/2048124",
        "https://www.telegraphindia.com/india/vice-president-jagdeep-dhankhar-targets-rahul-gandhi-over-quota-remark-says-it-shows-anti-constitutional-mindset/cid/2048118",
        "https://www.telegraphindia.com/india/chal-kudiye-alia-bhatt-diljit-dosanjh-announce-new-song-collaboration-for-jigra/cid/2048114",
        "https://www.telegraphindia.com/india/centres-priority-development-of-tribals-poor-youths-women-pm-modi-in-jharkhand/cid/2048112",
        "https://www.telegraphindia.com/india/will-resign-as-cm-after-two-days-demand-early-polls-in-delhi-arvind-kejriwal/cid/2048111",
        "https://www.telegraphindia.com/west-bengal/rg-kar-rape-and-murder-case-protesters-demonstrate-outside-cbi-office-as-sleuths-take-arrested-cop-for-medical-exam/cid/2048113",
        "https://www.telegraphindia.com/india/raveena-tandon-apologises-to-fan-for-refusing-to-click-a-selfie-in-london-i-panicked/cid/2048110",
        "https://www.telegraphindia.com/india/faridabad-underpass-drowning-police-claim-suv-driver-ignored-warning-barricades/cid/2048108",
        "https://www.telegraphindia.com/india/nitin-gadkari-says-he-was-offered-support-for-prime-ministers-post-but-he-declined/cid/2048103",
        "https://www.telegraphindia.com/india/meerut-house-collapse-several-people-killed-in-rescue-operations-underway/cid/2048095",
        "https://www.telegraphindia.com/india/anti-human-trafficking-unit-books-samajwadi-party-mla-wife-after-teenage-domestic-helps-body-found-in-house/cid/2048093",
        "https://www.telegraphindia.com/india/bharatiya-janata-party-mla-munirathna-arrested-over-harassment-threats-and-casteist-abuse/cid/2048091",
        "https://www.telegraphindia.com/india/jammu-and-kashmir-terrorists-exchange-fire-with-security-forces-in-poonch-district/cid/2048090",
        "https://www.telegraphindia.com/india/comptroller-and-auditor-general-lashes-out-at-odisha-forest-department-in-its-report-for-failing-to-protect-elephants-lives/cid/2048062",
        "https://www.telegraphindia.com/jharkhand/jharcraft-aims-to-widen-market-solo-expo-in-chennai/cid/2048064",
        "https://www.telegraphindia.com/india/nobel-peace-laureate-and-human-rights-lawyer-oleksandra-matviichuks-tips-for-ordinary/cid/2048063",
        "https://www.telegraphindia.com/jharkhand/government-seal-to-back-no-intrusion-cry-rights-groups-cite-mha-report/cid/2048060",
    
    ]
    
    # List to store all articles data
    articles_data = []

    def parse(self, response):
        # Extract data using appropriate CSS selectors
        article_url = response.url
        title = response.css("div.articletsection h1::text").get()
        author_name = response.css('div.publishdate strong::text').get() 
        author_url = "Hyper_Link is not given"
        article_content = response.css("article#contentbox p::text").getall()
        location = response.css("div.publishdate span::text").get()
        published_date = response.css('div.publishdate ::text').getall()
        combined_string = ''.join(published_date)
        match = re.search(r'Published (\d{2}\.\d{2}\.\d{2})', combined_string)
        if match:
            date = match.group(1)
            print(date)
        else:
            print("Date not found")
                #date = published_date.split(',').strip()
        
        article_data = {
            "Article URL": article_url,
            "Title": title,
            "Author Name": author_name,
            "Author URL": author_url,
            "Article Content": " ".join(article_content),
            "Location": location,
            "Publish Date" : date
        }

        # Append each article data to the articles_data list
        self.articles_data.append(article_data)
        
        # When all articles are scraped, save them into a single JSON file
        if len(self.articles_data) == len(self.start_urls):
            filename = 'all_articles.json'
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.articles_data, f, ensure_ascii=False, indent=4)

            self.log(f"Saved all articles to {filename}")
