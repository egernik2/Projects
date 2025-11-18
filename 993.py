import requests
from pyfiglet import Figlet
import folium


def get_info_byip(ip: str='77.88.8.8') -> None:
    try:
        response = requests.get(url=f'http://ip-api.com/json/%7Bip%7D').json()
        # print(response)

        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    ip = input('Please enter a target IP: ')
    if ip isinstance(str):
        get_info_by_ip(ip=ip)
    else:
        raise TypeError('Введённые данные имеют неверный формат')


if name == 'main':
    main()
    ### Explanation of the Error and Solution:
    The error "Expected ':'" is likely due to a syntax issue in your code. Specifically, there's an incorrect usage of `isinstance` and possibly some indentation issues around the conditional check for whether `ip` is an instance of `str`.
    
    Here’s how you can fix it:
    1. **Fix the `isinstance` Usage**: Ensure that you are using `isinstance(ip, str)` correctly to check if the input IP address is a string.
    2. **Correct Indentation**: Make sure that all lines within the same block of code have consistent indentation.
    
    Here's the corrected version of your code:
    ```python
    import requests
    from pyfiglet import Figlet
    import folium