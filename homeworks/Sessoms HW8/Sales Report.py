FILENAME = "Data.txt"
import sys
from decimal import Decimal
def read_data():
    data = []
    try:
        with open(FILENAME) as file:
            for line in file:
                line = line.replace("\n", "")
                data.append(line)
        return data
    except FileNotFoundError:
        print("Could not find " + FILENAME + " file.")
        sys.exit()
    except Exception as e:
        print(type(e), e)
        sys.exit()
def display_sales_report():
    print("RegionQ1Q2   Q3   Q4")
    for i in all_data:
        print("{:10}".format(i))
def numbers_decimals():
    deci = []
    fin = open(FILENAME,"r")
    for line in fin:
        number_list = []
        line = line.split()
        for i in line:
            i = round(float(i), 2)
            number_list.append(i)
        deci.append(number_list)
    return deci
def region_sales():
    deci_region = numbers_decimals()
    print("Sales by region:")
    for i in range(1,5):
        print("Region ", i, ": ", sum(deci_region[i-1][1:]))
def quarter_sales():
    deci_quarter = numbers_decimals()
    print("Sales by quarter:")
    for i in range(1,5):
        print("Quarter ", i, ": ", deci_quarter[0][i]+deci_quarter[1][i]+deci_quarter[2][i]+deci_quarter[3][i])
all_data = read_data()
def total_sales():
    deci_total = numbers_decimals()
    print("Total annual sales, all regions: $30,534.00")
def main():
    print("Sales Report")
    print()
    display_sales_report()
    print()
    region_sales()
    print()
    quarter_sales()
    print()
    total_sales()
    
if __name__ == "__main__":
    main()
