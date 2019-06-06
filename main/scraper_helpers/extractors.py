xpath_name = '//h1[@id="title"]//text()'
xpath_sale_price = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
xpath_original_price = '//td[contains(text(),"List Price") or contains(text(),"M.R.P") or contains(text(),"Price")]/following-sibling::td/text()'
xpath_category = '//div[@id="wayfinding-breadcrumbs_feature_div"]//ul/li[last()]//text()'
xpath_dimension = '//td[contains(text(),"Product Dimensions")]/following-sibling::td/text()'
xpath_img = '//div[@id="main-image-container"]//ul/li/span//div/img[@id="landingImage"]/@src'
xpath_rank_numbers = '//tr[@id="SalesRank"]/td[@class="value"]/ul/li[@class="zg_hrsr_item"]//span[@class="zg_hrsr_rank"]/text()'
xpath_rank_categories = '//tr[@id="SalesRank"]/td[@class="value"]/ul/li/span/a/text()'
xpath_rank = '//tr[@id="SalesRank"]/td[@class="value"]/ul'


def get_product_title(tree):
    raw_name = tree.xpath(xpath_name)
    return ' '.join(''.join(raw_name).split()) if raw_name else None


def get_sale_price(tree):
    raw_sale_price = tree.xpath(xpath_sale_price)
    return ' '.join(
        ''.join(raw_sale_price).split()) if raw_sale_price else None


def get_product_original_price(tree):
    raw_original_price = tree.xpath(xpath_original_price)
    return ' '.join(''.join(
        raw_original_price).split()) if raw_original_price else None


def get_product_category(tree):
    raw_category = tree.xpath(xpath_category)
    return ' '.join(''.join(raw_category).split()) if raw_category else None


def get_product_dimension(tree):
    raw_dimension = tree.xpath(xpath_dimension)
    return ' '.join(''.join(raw_dimension).split()) if raw_dimension else None


def get_product_img(tree):
    raw_img = tree.xpath(xpath_img)
    return ' '.join(''.join(raw_img).split()) if raw_img else None


def get_product_rank(tree):
    raw_rank_numbers = tree.xpath(xpath_rank_numbers)
    raw_rank_categories = tree.xpath(xpath_rank_categories)
    rank = ""
    for i in range(len(raw_rank_numbers)):
        rank += "%s %s" % (raw_rank_numbers[i], raw_rank_categories[i])
        if (i != len(raw_rank_numbers)):
            rank += ','
    return rank if len(raw_rank_numbers) > 0 else None
