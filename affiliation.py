def generate_affiliation_link(url):
    url_split = url.split("/")
    return f'http://www.amazon.com/dp/{url_split[5]}/?tag=pyb0f-20'
    pass
