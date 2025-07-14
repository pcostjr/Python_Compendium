# sqlite_main.py
# description: As per Assignment 2, a basic sqlite handler that reads data from a csv to populate into a sqlite database
# preconditions: SQLite is installed on the target system, and the file we read in is a csv
# author: pcostjr
# created: 7.14.2025
# last update: 7.14.2025

# import sqlite3 to handle sqlite, and pandas to easily read in the csv
import sqlite3
import pandas

# configuration parameters:
TABLE_NAME = "UCI Credit Card Data"
TARGET_FILE = "UCI_Credit_Card.csv"


# establish a connection to the target sqlite server and create a cursor
def establish_connection(database_name):
    database = sqlite3.connect(database_name)
    return database, database.cursor()


# read the contents of the target csv file
# use it to populate a new table
def read_to_sql(database, filename, table_name):
    with open(filename) as file:
        contents = pandas.read_csv(file)
    if contents is not None:
        # on the table name, with our cursor, replace the existing table if there,
        # and do not create an index for the table
        contents.to_sql(table_name, database, if_exists='replace', index=False)


# analyze the db using the parameters outlined in the Assignment instructions
def analyze_db(table_name, cursor):
    # selection statement that will group like values into a count and store the query as a list of tuples
    marriage_status = cursor.execute(f"SELECT \"MARRIAGE\", "
                                     f"COUNT(*) FROM \"{table_name}\""
                                     f" GROUP BY \"MARRIAGE\"").fetchall()
    # the same as the previous query, but this time accounting for if they have a default payment next month
    payment_status = cursor.execute(f"SELECT \"MARRIAGE\", COUNT(*)"
                                    f" FROM \"{table_name}\""
                                    f"WHERE \"default.payment.next.month\" = '1' "
                                    f"GROUP BY \"MARRIAGE\"").fetchall()

    # output the requested data from the instructions with formatting and context
    print(f"Total number of non-married parties: {marriage_status[2][1] + marriage_status[3][1]}")
    print(f"Total number of married parties: {marriage_status[1][1]}")
    print()
    print(f"Total number of default payments for non-married parties: {payment_status[2][1] + payment_status[2][1]}")
    print(f"Total number of default payments for married parties: {payment_status[1][1]}")
    print()
    print(f"Total percentage of singles with default payments:"
          f" {format((payment_status[2][1] + payment_status[2][1])/(marriage_status[2][1] + marriage_status[3][1]), '.2%')}")
    print(f"Total percentage of married with default payments:"
          f" {format(payment_status[1][1]/marriage_status[1][1], '.2%')}")


# main method declaration
if __name__ == "__main__":
    db, cur = establish_connection("example.db")
    read_to_sql(db, TARGET_FILE, TABLE_NAME)
    analyze_db(TABLE_NAME, cur)
