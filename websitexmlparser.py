from bs4 import BeautifulSoup
import requests
import re
# import xlsxwriter module
import xlsxwriter

searchkeywords = ['COVID-19','Coronavirus']
keywordmatches = None

url = 'https://www.pharmaceutical-technology.com/news/coronavirus-a-timeline-of-how-the-deadly-outbreak-evolved/'
#source code of request object from url
source = ''
try:
    source = requests.get(url,timeout=5).text
except:
    print('Unable to connect to url')

soup = BeautifulSoup(source,'html.parser')

#This portion will change as per the website
content = soup.find('div',class_='microblog-updates')
postArr = []
articlecount = 0
for post in content.find_all('div',attrs={"class":"microblog-update cf"}):
    article = ''
    #print(post)
    #every post has a title
    title = post.h2.text

    #To retrieve paragraphs and build article
    for paras in post.find_all('p'):
        article = article + ' ' + paras.text

    articlecount = articlecount+1
    #print(str(articlecount) + '' + str(article))
    #match the keyword here
    for keywords in searchkeywords:
        #pattern = 'r\'\\b' + str(keywords) + '\\b\''
        pattern = keywords
        #print(str(pattern))
        keywordmatches = re.search(pattern, article, flags=re.IGNORECASE)
        #print(keywordmatches)
        # Add to the list only if it founds the keyword
        if keywordmatches!=None:
            postObj = {
                "title": title,
                "article_number": articlecount,
                "article": article
            }
            postArr.append(postObj)
        break
#print((postArr))
#export data to xlsx format
# Workbook is created
workbook = xlsxwriter.Workbook(r'C:\Users\goura\OneDrive\Desktop\pharmaceutical-technology.xlsx')
# add_sheet is used to create sheet.
worksheet = workbook.add_worksheet("Data sheet")
#Column names
worksheet.write(0, 0, 'Article Number')
worksheet.write(0, 1, 'Title of Headline')
worksheet.write(0, 2, 'Article')

for data in range(len(postArr)):
    #print(postArr[data])
    worksheet.write(data+1, 0, postArr[data]['article_number'])
    worksheet.write(data+1, 1, postArr[data]['title'])
    worksheet.write(data+1, 2, postArr[data]['article'])
workbook.close()


