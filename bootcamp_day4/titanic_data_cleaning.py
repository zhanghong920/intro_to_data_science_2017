import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
import os


class TitanicDataCleaning(object):
    def __init__(self):
        """
        Initialized variables
        """
        self.data = None
        self.df_train = None
        self.df_validation = None
        self.df_test = None

    def readin_data(self, path):
        """
        Read in data. Save to self.data.
        :param path: path to the data
        :return: None
        """
        # 'https://raw.githubusercontent.com/eclarson/DataMiningNotebooks/master/data/titanic.csv'
        self.data = pd.read_csv(path)

    def drop_columns(self, drop_columns):
        """
        Drop columns not used.
        :param drop_columns: columns to drop
        :return: None
        """
        # ['PassengerId', 'Name', 'Cabin', 'Ticket']
        self.data = self.data.drop(drop_columns, axis=1)

    def dummification(self, dummy_columns):
        """
        Dummify columns.
        :param dummy_columns: columns to dummify
        :return: None
        """
        # ["Sex", "Embarked"]
        self.data = pd.get_dummies(self.data, columns=dummy_columns)

    def data_split(self):
        """
        Split data into train, validation and test.
        :return: None
        """
        df_temp, self.df_test = train_test_split(self.data, test_size=0.2,
                                                 random_state=666)
        self.df_train, self.df_validation = train_test_split(self.data,
                                                             test_size=0.3,
                                                             random_state=666)

    def __actual_impute(self, df, the_imputer):
        """
        Impute the data with a trained imputer
        :param df: imput dataframe
        :param the_imputer: trained imputer
        :return: imputed dataframe
        """
        column_names = df.columns
        df = pd.DataFrame(the_imputer.transform(df))
        df.columns = column_names
        return df

    def imputation(self):
        """
        Impute the data.
        Train with training data then impute validation and test sets.
        :return: None
        """
        median_imputer = Imputer(strategy="median")
        median_imputer.fit(self.df_train)
        self.df_train = self.__actual_impute(self.df_train, median_imputer)
        self.df_validation = self.__actual_impute(self.df_validation,
                                                  median_imputer)
        self.df_test = self.__actual_impute(self.df_test, median_imputer)

    def save_model_ready_data(self, save_directory):
        """
        Save model ready data.
        :param save_directory: the directory to save train, validation and test.
        :return: None
        """
        self.df_train.to_csv(os.path.join(save_directory, 'df_train.csv'),
                             index=False)
        self.df_validation.to_csv(
            os.path.join(save_directory, 'df_validation.csv'),
            index=False)
        self.df_test.to_csv(os.path.join(save_directory, 'df_test.csv'),
                            index=False)
