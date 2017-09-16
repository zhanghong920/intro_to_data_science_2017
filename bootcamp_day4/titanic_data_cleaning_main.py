from titanic_data_cleaning import TitanicDataCleaning


def get_data_ready():
    # Instanciate
    cleaning_data = TitanicDataCleaning()

    # Read in data
    readin_data_path = 'https://raw.githubusercontent.com/eclarson/DataMiningNotebooks/master/data/titanic.csv'
    cleaning_data.readin_data(readin_data_path)

    # Clean data

    drop_columns = ['PassengerId', 'Name', 'Cabin', 'Ticket']
    cleaning_data.drop_columns(drop_columns)

    dummy_columns = ["Sex", "Embarked"]
    cleaning_data.dummification(dummy_columns)

    cleaning_data.data_split()
    cleaning_data.imputation()

    # Save data
    cleaning_data.save_model_ready_data('../data/titanic')

if __name__ == "__main__":
    get_data_ready()