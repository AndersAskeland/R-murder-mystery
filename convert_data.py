# Imports
import sqlite3
import pandas as pd

# Main
def main():
    # SQL connection
    con = sqlite3.connect("raw-data/sql-murder-mystery.db")

    # Read tables
    read_table("interview", con)
    read_table("get_fit_now_check_in", con)
    read_table("get_fit_now_member", con)
    read_table("person", con)
    read_table("facebook_event_checkin", con)
    read_table("drivers_license", con)
    read_table("crime_scene_report", con)
    read_table("income", con)
WITH interview as (SELECT * FROM interview JOIN person p ON p.id = person_id WHERE (name LIKE'%Annabel%' AND address_street_name = 'Franklin Ave') OR  (address_street_name = 'Northwestern Dr'))



# Functions
def read_table(table, con):
    # SQL stuff
    query = f'''SELECT * FROM {table}'''
    sql_query = pd.read_sql_query(query, con)
    
    # Pandas stuff
    df = pd.DataFrame(sql_query)

    # Write CSV
    df.to_csv(f"data/{table}.csv", index=False)

# Run
if __name__ == "__main__":
    main()
