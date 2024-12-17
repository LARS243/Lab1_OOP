import requests
import json
import webbrowser
import urllib.parse

class wikipedia:
    def __init__(self, adress):
        self.adress = adress;
        self.pars_resualts = self.parser();  
    def parser(self):
        encoded_query = urllib.parse.quote(self.adress)
        url = "https://ru.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json&srsearch=" + encoded_query;
        request_data = requests.get(url).json();
        return request_data ['query']['search'];
    def print_resualts(self):
        print('Выберете страницу или введите 0 для выхода:')
        counter = 0;
        matrix = list();
        for element in self.pars_resualts:
            counter+=1;
            print(str(counter) + ')', element['title']);
            matrix.append(element['pageid']);
        self.chose_page(counter, matrix);
        
    def chose_page(self, counter, matrix):
        number_page = int(input());
        work = True;
        while ((number_page <= 0 or number_page > counter) and work):
            if (number_page == 0):
                work = False;
            else:
                print("Неверный ввод.");
                self.print_resualts();
        if (work):
            self.open_page(matrix[number_page-1]);
    def open_page(self, chose):
        url = f"https://ru.wikipedia.org/w/index.php?curid={chose}";
        webbrowser.open(url);        
        
def user_interface():
    print("Введите поисковый запрос: ")
    input_ = wikipedia('ЛЭТИ');
    input_.print_resualts();

user_interface();