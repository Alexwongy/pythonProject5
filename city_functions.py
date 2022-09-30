"""一系列处理城市的函数"""


def city_country(city, country, population):
    """返回一个城市，国家 - population 5000的字符串"""

    out_string =  f"{city.title()} {country.title()}"
    out_string += f'-population {population}'
    return out_string

if __name__ == '__main__':
    sc = city_country('santiago', 'chile', '600')
    print(sc)