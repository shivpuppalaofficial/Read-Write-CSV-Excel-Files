
import pandas as pd


def main():
    # Read data from CSV
    try:
        csv_data = pd.read_csv("data.csv")
        print("✅ CSV Data:")
        print(csv_data)

        # Write to Excel
        csv_data.to_excel("data_output.xlsx", index=False)
        print("\n💾 Data written to data_output.xlsx")

        # Read back from Excel
        excel_data = pd.read_excel("data_output.xlsx")
        print("\n📖 Excel Data:")
        print(excel_data)

    except FileNotFoundError:
        print("❌ Please make sure 'data.csv' exists in this folder.")


if __name__ == "__main__":
    main()
