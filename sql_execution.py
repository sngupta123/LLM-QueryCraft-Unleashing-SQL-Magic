import pandas as pd
import mysql.connector
from mysql.connector import Error


def execute_sf_query(p_sql):
    query = p_sql

    # Establish a connection to mysql Database
    conn = mysql.connector.connect(host='127.0.0.1',
                                   database='employees',
                                   user='root',
                                   password='rootroot')
    cur = conn.cursor()

    try:

        # Execute the query
        try:
            cur.execute(query)
        except Error as e:
            print("Query Compilation Error: ", e)
            return e

        # Fetch All results
        query_results = cur.fetchall()

        # Get Column names from the cursor description
        column_names = [col[0] for col in cur.description]

        # Create a Pandas Dataframe
        data_frame = pd.DataFrame(query_results, columns=column_names)
        return data_frame

    except ConnectionError as ce:
        print("Connection Error: ", ce)

    except Exception as e:
        print("An error occured: ", e)

    finally:
        # Close the cursor and Connection
        if conn.is_connected():
            cur.close()
            conn.close()
