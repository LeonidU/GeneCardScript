from seleniumbase import BaseCase
from bs4 import BeautifulSoup
import time
BaseCase.main(__name__, __file__)

print(__name__)

class MyTestClass(BaseCase):
    def test_basics(self):
        ff = open("result.txt", 'w')
#        self.open("https://www.genecards.org")
#        driver2.get("https://www.genecards.org")
#        self.sleep(5)
#        driver2.quit()
#        exit()
        for elem in open("example.xls", 'r'):
            driver2 = self.get_new_driver()
            gene = elem.split(" ")[1]
#            self.type("input.form-control", gene)
#            self.sleep(5)
#            self.click('button.btn.btn-warning.search-bar-btn-addon.search-btn-cta')
#            self.sleep(30)
            driver2.get("https://www.genecards.org/Search/Keyword?queryString="+gene)
            source = self.get_page_source()
            soup = BeautifulSoup(source, 'html.parser')
            if (soup.find('table', {'class': 'table table-striped table-condensed'}) is None):
                ff.write(gene+"\t")
                ff.write("Undefined\t")
                ff.write("Undefined\t")
                ff.write("RNA gene\t")
                ff.write("\n")
                driver2.quit()
                continue
            else:
                table = soup.find('table', {'class': 'table table-striped table-condensed'}).find('tbody')
                rows = table.find_all('tr')
                first_row = rows[0]
                full_name = first_row.find_all('td', {'class': 'gc-highlight description-col'})
                type_protein = first_row.find_all('td', {'class': 'category-col'})
                name = first_row.find('a', {'target': '_blank'})
        #        ff.write(str(first_row))
                # Loop through each cell and print its text
                ff.write(gene+"\t")
                ff.write(str(name.get('data-ga-label'))+"\t")
                ff.write(str(full_name[0].text)+"\t")
                ff.write(str(type_protein[0].text)+"\t")
                ff.write("\n")
                driver2.quit()
