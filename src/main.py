from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    data = extract_data()
    df = transform_data(data)
    load_data(df)

    print("ETL finalizado com sucesso!")

if __name__ == "__main__":
    main()