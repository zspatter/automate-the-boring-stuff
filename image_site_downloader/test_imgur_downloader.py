import os
import shutil

from image_site_downloader import imgur_downloader


def test_downloader():
    # dir at path created
    root = os.path.abspath(os.path.join('.', 'image_site_downloader', 'test_files'))

    # if dir exists, remove it (for consistent test results)
    if os.path.exists(root):
        shutil.rmtree(root)

    # make dir for results
    os.makedirs(root)

    assert len(os.listdir(root)) == 0

    imgur_downloader.downloader(query='happy', max_quantity=8, output_path=root)
    extensions = ['.jpeg', '.jpg', '.png', '.gif', '.apng', '.tiff', '.mov', '.mp4']
    results = os.listdir(root)

    # verifies results are less than or equal to max_quantity argument
    assert len(results) <= 8

    # verify extension of downloaded files are of the expected type
    for result in results:
        assert os.path.splitext(result)[1] in extensions

    # removes test directory (for consistent test results)
    shutil.rmtree(root)
