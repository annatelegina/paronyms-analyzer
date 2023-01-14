import mysql.connector
from mysql.connector import Error
import xlsxwriter
import csv

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        #print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

    return result

def extract_all(out_path,name="adj_noun", table="_main_dict_inf"):
    table_name = "cosyco_base." + name + table
    connection = create_connection("cosyco.ru", "cosycoreader", "Rh@cysqIbyibkk@5")
    query = "select * from {:s} ".format(table_name)
    res = execute_read_query(connection, query)
    
    workbook = open(out_path + ".csv", 'w')
    writer = csv.writer(workbook)

    writer.writerow(["id_inf","token","freq","freq_de"])
    writer.writerows(res)
    workbook.close()


if __name__ == "__main__":
    extract_all(name="noun_verb", table="_main_dict_inf", out_path="noun_verb_main_dict_inf")

