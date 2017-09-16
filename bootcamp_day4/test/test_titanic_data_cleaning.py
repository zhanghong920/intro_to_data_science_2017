# run with:
# nosetests -v test_titanic_data_cleaning.py
import unittest
import tempfile
import shutil
import pandas as pd
from bootcamp_day4.titanic_data_cleaning import TitanicDataCleaning


class TestTitanicDataCleaning(unittest.TestCase):
    def setUp(self):
        self.temp_dir = None
        self.df = pd.DataFrame([[1, 2, 3, 'a'], [1, 2, 3, 'b'], [1, 2, 3, 'c']])
        self.df.columns = ['one', 'two', 'three', 'letter']
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_readin_data(self):
        cleaning_data = TitanicDataCleaning()
        readin_data_path = 'https://raw.githubusercontent.com/eclarson/DataMiningNotebooks/master/data/titanic.csv'
        cleaning_data.readin_data(readin_data_path)
        assert (isinstance(cleaning_data.data, pd.DataFrame))
        assert (cleaning_data.data.shape[0] != 0)
        assert (cleaning_data.data.shape[1] != 0)

    def test_drop_columns(self):
        cleaning_data = TitanicDataCleaning()
        cleaning_data.data = self.df
        drop_columns = ['one', 'two']
        cleaning_data.drop_columns(drop_columns)
        assert (len(cleaning_data.data.columns) == 2)


if __name__ == '__main__':
    unittest.main()