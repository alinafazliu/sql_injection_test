import unittest
import HtmlTestRunner
import penetration as pen 
import webbrowser 
import os
import time
from ddt import ddt, data, unpack


def get_html_file():
    arr = os.listdir()
    for x in arr:
        if '.html' in x:
            return x 


def get_tests(path):
    tuples=[]
    f = open(path, "r")
    for x in f:
        x=x.split(' ')
        tuples.append((x[0],x[1]))

    f.close()
    return tuples

def convert_to_bool(str):
    if str=="True":
        return True
    return False

testing_data = get_tests('pages.txt')

@ddt
class TestName(unittest.TestCase):

        @data(*testing_data)
        @unpack
        def test_website(self, website_url, is_vulnerable):
            self.assertEqual(pen.scan_sql_injection(website_url), convert_to_bool(is_vulnerable))

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='.'))
        filename = 'file:///'+os.getcwd()+'/' + 'TestResults___main__.TestName_2021-02-12_20-14-33'
        webbrowser.open_new_tab(filename)
