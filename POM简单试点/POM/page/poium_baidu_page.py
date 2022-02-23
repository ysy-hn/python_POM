from poium import Page, Element


class BaiduPagePoium(Page):
    search_input = Element(id_='kw')
    search_button = Element(id_='su')


