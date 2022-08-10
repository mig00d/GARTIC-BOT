import urllib.request


def download_image(url_image, file, path):
    """
    Télécharge l'image avec l'adresse de l'image
    :param url_image:
    :param file:
    :param path:
    :return:
    """
    full_path = f'{path}{file}.jpg'

    urllib.request.urlretrieve(url_image, full_path)
    print('image download')
    return full_path

