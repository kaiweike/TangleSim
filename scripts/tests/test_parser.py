import os
import pandas as pd

from parsing import FileParser
from main import parse_arg

config = parse_arg()
config.cd['CONFIGURATION_PATH'] = os.path.join(os.getcwd(), 'tests', 'resources', 'dataset', 'mb.config')
parser = FileParser(config.cd)

fn =  os.path.join(os.getcwd(), 'tests', 'resources', 'dataset', 'general', 'BlockInformation.csv')
variation = 'ParentsCount'

def test_parse_block_information_file():
    file_path1 = os.path.join(os.getcwd(), 'tests', 'resources', 'expected', 'block_info', 'tuple_1.csv')
    file_path2 = os.path.join(os.getcwd(), 'tests', 'resources', 'expected', 'block_info', 'tuple_2.csv')
    file_path3 = os.path.join(os.getcwd(), 'tests', 'resources', 'expected', 'block_info', 'tuple_3.csv')
    file_path4 = os.path.join(os.getcwd(), 'tests', 'resources', 'expected', 'block_info', 'tuple_4.csv')

    expected_1 = pd.read_csv(file_path1, index_col=0)['Confirmation Time (ns)']
    expected_2 = pd.read_csv(file_path2, index_col=0)['Confirmation Time (ns)']
    expected_3 = pd.read_csv(file_path3, index_col=0)['Issuance Time Since Start (ns)']
    expected_4 = pd.read_csv(file_path4, index_col=0)['Issuance Time Since Start (ns)']

    # actual = parser.parse_block_information_file(fn, variation)
    actual = parser.parse_file(fn, variation, 'block_info')

    assert isinstance(actual, tuple)
    assert actual[0] == '8'
    pd.testing.assert_series_equal(actual[1], expected_1)
    pd.testing.assert_series_equal(actual[2], expected_2)
    pd.testing.assert_series_equal(actual[3], expected_3)
    pd.testing.assert_series_equal(actual[4], expected_4)