# Imports
import sqlite3
import pandas as pd
import os

# Main
def main():
    # SQL connection
    con = sqlite3.connect("raw-data/sql/sql-murder-mystery.db")

    # Read tables
    read_table("interview", con)
    read_table("get_fit_now_check_in", con)
    read_table("get_fit_now_member", con)
    read_table("person", con)
    read_table("facebook_event_checkin", con)
    read_table("drivers_license", con)
    read_table("crime_scene_report", con)
    read_table("income", con)

    # Split interviews dataframe
    split_interviews()

    # Rename SQL city to R city
    r_city()

    # Pivot 
    pivot_data()

    # Remove interview data
    if os.path.exists("raw-data/csv/interview.csv"):
        os.remove("raw-data/csv/interview.csv")


# Functions
def read_table(table, con):
    # SQL stuff
    query = f'''SELECT * FROM {table}'''
    sql_query = pd.read_sql_query(query, con)
    
    # Pandas stuff
    df = pd.DataFrame(sql_query)

    # Write CSV
    df.to_csv(f"raw-data/csv/{table}.csv", index=False)

def split_interviews():
    # Read data
    interviews = pd.read_csv("raw-data/csv/interview.csv")

    # Split data
    for i in range(len(interviews)):
        person_id = interviews.iloc[i, 0]
        interviews.loc[[i]].to_csv(f"raw-data/csv/interviews/{person_id}.csv", index=False)

def pivot_data():
    df = pd.read_csv("raw-data/csv/get_fit_now_member.csv")

    df = df.pivot(columns="person_id")

    df.to_csv("raw-data/csv/get_fit_now_member.csv", index=False)


def r_city():
    # read data
    df = pd.read_csv("raw-data/csv/crime_scene_report.csv")

    # Replace SQL city with R city
    df.loc[df['city'] == "SQL City", 'city'] = "R City"

    # Write
    df.to_csv("raw-data/csv/crime_scene_report.csv")

# Run
if __name__ == "__main__":
    main()
