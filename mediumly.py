from urllib.request import pathname2url
import newspaper
import textile
import os
import webbrowser

class cook:


    def __init__(self):
        #Using newspaper to fetch the title and the content of the article
        self.url=input("\nEnter the address: ")
        self.article=newspaper.Article(self.url)
        self.article.download()
        self.article.parse()
        self.title=self.article.title.strip()
        self.content=self.article.text
        self.headline=self.article.title.strip()
        self.image=self.article.top_image


    def convert_html(self):
        #using textile to parse the article content to html
        html_content=textile.textile(self.content)
        return html_content


    def write_file(self,html_content):
        #Adding the html parsed data into an html editor
        with open('medium_cooked.html','w') as file:
            file.write('<a href="https://medium.com/"><img src="header.png" /></a><br>') #MediumFeel
            file.write('<br><h1 align="center">'+self.headline+'</h1><br>') #Article Headline
            file.write('<div style="display: flex; justify-content: center;"><img src='+self.image+' style="float:right;"><br></div>') #Article Image
            file.write('<div style="margin-top:50px; margin-left:250px; margin-right:300px; border:1px solid white;""><font size="4px" style="color:#292929;text-align:middle">'+html_content) #Article Content
            file.write('<br><font size=3 align=middle>Designed by | <a href="https:github.com/asiffarhankhan">AlphaPhiKappa</a></font>')

    def main(self):
        #Openning the "Medium_Cooked" file on a browser window
        html_content=self.convert_html()
        self.write_file(html_content)
        self.url = 'file:{}'.format(pathname2url(os.path.abspath('medium_cooked.html')))
        webbrowser.open(self.url)


if __name__=='__main__':
    cook().main()