# Imports
import sqlite3
import pandas as pd
import os
from zipfile import ZipFile
from os.path import basename
import shutil



# Main
def main():
    # SQL connection
    con = sqlite3.connect("data-raw/sql/sql-murder-mystery.db")

    # Read tables
    read_table("interview", con)
    read_table("get_fit_now_check_in", con)
    read_table("get_fit_now_member", con)
    read_table("person", con)
    read_table("facebook_event_checkin", con)
    read_table("drivers_license", con)
    read_table("crime_scene_report", con)
    read_table("income", con)

    # Rename SQL city to R city
    r_city()

    # Split interviews dataframe
    split_crime_scene_report()

    # Pivot 
    # pivot_data()

    # Remove interview data
    if os.path.exists("data-raw/crime_scene_report.csv"):
        os.remove("data-raw/crime_scene_report.csv")

    # Zip data
    zip_data()

    # Move file
    shutil.move("r-murder-mystery.zip", "data-raw/r-murder-mystery.zip")

    # Remove files
    os.remove("data-raw/drivers_license.csv")
    os.remove("data-raw/facebook_event_checkin.csv")
    os.remove("data-raw/get_fit_now_check_in.csv")
    os.remove("data-raw/get_fit_now_member.csv")
    os.remove("data-raw/income.csv")
    os.remove("data-raw/interview.csv")
    os.remove("data-raw/person.csv")
    shutil.rmtree("data-raw/crime_scene_report")








# Functions
def read_table(table, con):
    # SQL stuff
    query = f'''SELECT * FROM {table}'''
    sql_query = pd.read_sql_query(query, con)
    
    # Pandas stuff
    df = pd.DataFrame(sql_query)

    # Write CSV
    df.to_csv(f"data-raw/{table}.csv", index=False)

def split_crime_scene_report():
    # Make dir
    os.mkdir("data-raw/crime_scene_report")
    
    # Read data
    crime_scene_report = pd.read_csv("data-raw/crime_scene_report.csv")

    # Split data
    for i in range(len(crime_scene_report)):
        person_id = crime_scene_report.iloc[i, 0]
        crime_scene_report.loc[[i]].to_csv(f"data-raw/crime_scene_report/{person_id}.csv", index=False)

def pivot_data():
    df = pd.read_csv("data-raw/get_fit_now_member.csv")

    df = df.pivot(columns="membership_status")

    df.to_csv("data-raw/test.csv", index=False)


def r_city():
    # read data
    df = pd.read_csv("data-raw/crime_scene_report.csv")

    # Replace SQL city with R city
    df.loc[df['city'] == "SQL City", 'city'] = "R City"

    # Write
    df.to_csv("data-raw/crime_scene_report.csv")

def zip_data():
    shutil.make_archive("r-murder-mystery", 'zip', "data-raw/")


# Run
if __name__ == "__main__":
    main()
