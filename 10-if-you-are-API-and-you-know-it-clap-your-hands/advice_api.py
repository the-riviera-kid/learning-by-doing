import requests


def main():
    url = 'https://api.adviceslip.com/advice'
    obj = get_obj(url)
    main_menu = True
    while main_menu:
        print('1. Random piece of advice\n2. Get advice by ID\n3. Search by keyword\n4. Quit\n')
        menu_number = int(input('Choose a menu option: '))
        advice, main_menu = advice_option(menu_number, url, obj)
        print(advice, end='\n\n')

def get_obj(url):
    r = requests.get(url)
    obj = r.json()
    return obj

def advice_option(menu_number, url, obj):
    advice_options = [get_random_advice, get_advice_by_id, get_advice_by_keyword, quit]
    return advice_options[menu_number -1](url, obj)

def get_random_advice(url, obj):
    return obj['slip']['advice'], True

def get_advice_by_id(url, obj):
    id = input('Enter the ID number of the advice you wish to see: ')
    combined_url = f'{url}/{id}'
    obj = get_obj(combined_url)
    return obj['slip']['advice'], True

def get_advice_by_keyword(url, obj):
    keyword = input('Enter your keyword: ')
    keyword_url = url + '/search/' + keyword
    obj = get_obj(keyword_url)
    if 'message' in obj:
        return obj['message']['text'], True
    else:
        for adv in obj['slips']:
            return adv['advice'], True

def quit(url, obj):
    return f'Quit Program', False

if __name__ == '__main__':
    main()