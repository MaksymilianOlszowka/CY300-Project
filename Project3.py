################################################################################
# Cadets: Ian Campbell and Maksymilian Olszowka
# CY300 Final Project Draft
# Version 0.3.0
# 02 DECEMBER 2023
################################################################################
# Must include a custom class
# Must include 4 Summary Statistics (e.g. min, max, mean, median, mode)
# Must include 4 data filter options (e.g. only show rows where a certain
# column has a value above a certain threshold)
# Must include at least 2 graphing options using matplotlib
# Must include ability to add a new data row to existing dataset
# When adding data, it does not modify the original dataset, but rather creates
# a new dataset with the new data added, and will give the user the ability to
# save the new dataset to a file
# Allow a user to press a key to select an option from a menu and return to the 
# main menu after displaying the requested data
# Dataset used is smoking.csv, a dataset of smoking statistics by country
# Will use an attractive, easy-to-use GUI
# Should include help text and error messages to assist users in understanding
# how to use the program
import csv
import matplotlib.pyplot as py

# Class that will have a method to display summary statistics, filter the data
# by a certain column, graph the data, and add a new row of data to the dataset
# The class will allow you to filter the data by country as well

# Generally, we need to work on the following:
# All graphing options
# Test cases
# Error handling (e.g. if user enters a string when they should enter an int)
# Documentation
# If possible, keep lines within the 80 character limit

class Data :
    def __init__(self) -> None :
        # Save every row of the csv file as a dictionary in a list (skipping
        # the first row, which is the header)
        with open("project/smoking.csv", 'r') as csv_file :
            csv_reader = csv.reader(csv_file)
            self.data = [row for row in csv_reader]
    
    def filter_data_threshold(self, column: int, threshold: float) -> list :
        filtered_data = [row for row in self.data[1:] if int(row[column])
                        > threshold]
    
        return filtered_data
        
    def filter_data_country(self, country: str) -> list :
        filtered_data = [row for row in self.data[1:] if row[0] == country]
        
        if not filtered_data:
            print(f"\nNo data found for the country {country}.")
            return None
        
        return filtered_data
        
    def filter_data_year(self, year: str) -> list :
        filtered_data = [row for row in self.data[1:] if row[1] == year]
        
        if not filtered_data:
            print(f"\nNo data found for the year {year}.")
            return None

        return filtered_data
    
    def display_summary_stats(self, column, country = None, year = None) -> dict :
        # Display summary statistics for the dataset
        # If filtering by country, display summary statistics, taking into
        # account every row in which that country appears, for that country.
        # If filtering by year, display summary statistics, taking into account
        # every row in which that year appears, for that year.
        # Then display summary statistics for selected columns
        
        if self.filter_data_country(country) is None :
            
            return None

        if self.filter_data_year(year) is None :
            
            return None

        if country != None :
            filtered_data = self.filter_data_country(country)
        
        if year != None :
            filtered_data = self.filter_data_year(year)
        
        values = [float(row[column]) for row in filtered_data
                if row[column] != ""]
        
        if values :
            summary_stats = {
                "min": min(values),
                "max": max(values),
                "mean": sum(values) / len(values),
                "median": sorted(values)[len(values) // 2],
            }
        else :
            summary_stats = {
                "min": "N/A",
                "max": "N/A",
                "mean": "N/A",
                "median": "N/A",
            }
            
        print(summary_stats)
        
    def print_column_names(self) -> None :
        # Print all column names enumerated by index
        # exluding the first and second columns, which are Country and Year
        print("\nColumn Names:\n")
        for i in range(2, len(self.data[0])) :
            print(f"\t{i}. {self.data[0][i]}")
            
    def add_data(self) -> None :
        new_data = []
        while True :
            while True :
                try :
                    country = str(input("\nEnter country name: "))
                except :
                    print("\nInvalid input. Please enter a string.\n")
                    continue
                break
            while True :
                try :
                    year = str(input("\nEnter year: "))
                except :
                    print("\nInvalid input. Please enter a string.\n")
                    continue
                break
            while True :
                try :
                    cigarette_avg = float(input("\nEnter cigarette average: "))
                except :
                    print("\nInvalid input. Please enter a number.\n")
                    continue
                break
            while True :
                try :
                    percentage_male = float(input("\nEnter male percentage: "))
                except :
                    print("\nInvalid input. Please enter a number.\n")
                    continue
                break
            while True :
                try :
                    percentage_female = float(input("\nEnter female percentage: "))
                except :
                    print("\nInvalid input. Please enter a number.\n")
                    continue
                break
            while True :
                try :
                    percentage_total = float(input("\nEnter total percentage: "))
                except :
                    print("\nInvalid input. Please enter a number.\n")
                    continue
                break
            while True :
                try :
                    total_smokers = float(input("\nEnter total smokers: "))
                except :
                    print("\nInvalid input. Please enter a number.\n")
                    continue
                break
            while True :
                try :
                    smokers_female = float(input("\nEnter female smokers: "))
                except :
                    print("\nInvalid input. Please enter a number.\n")
                    continue
                break
            while True :
                try :
                    smokers_male = float(input("\nEnter male smokers: "))
                except :
                    print("\nInvalid input. Please enter a number.\n")
                    continue
                break
            
            new_row = [country, year, cigarette_avg, percentage_male,
                    percentage_female, percentage_total, 
                    total_smokers, smokers_female, smokers_male]
            
            new_data.append(new_row)
            
            while True :
                try :
                    user_input = str(input("\nDo you want to add another row? (y/n) : "))
                except :
                    print("\nInvalid input. Please enter a character.\n")
                    continue
                break
            
            if user_input == "n" :
                break
        
        while True :
            try :
                export_file_name = str(input("Enter filename to save new dataset (do not add \".csv\"): "))
            except :
                print("\nInvalid input. Please enter a string.\n")
                continue
            break
        
        with open(export_file_name + ".csv", 'w') as csv_file :
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(self.data[0])
            csv_writer.writerows(self.data[1:])
            csv_writer.writerows(new_data)

    def display_menu(self) -> str :
        print("\n##############################################")
        print("# Welcome to the Smoking Statistics Analyzer! #")
        print("##############################################")
        while True :
            print("\nWhat do you want to do?")
            print("\n\t1. Display Summary Statistics")
            print("\t2. Filter Data")
            print("\t3. Graph Data")
            print("\t4. Add New Data")
            print("\t5. Exit\n")
            while True :
                try :
                    user_input = int(input("Enter choice here : "))
                except :
                    print("\nInvalid input. Please enter a number.\n")
                    continue
                break
            
            match user_input :
                case 1 :
                    print("\nWhat do you want to filter by?\n")
                    print("\t1. Country")
                    print("\t2. Year")
                    while True :
                        try :
                            user_input_filter = int(input("\nEnter choice here : "))
                        except :
                            print("\nInvalid input. Please enter a number.\n")
                            continue
                        break
                    
                    match user_input_filter :
                        case 1 :
                            country = str(input("\nEnter country name: "))
                            self.print_column_names()
                            column = int(input("\nEnter data you want summary statistics for: "))
                            
                            self.display_summary_stats(column, country = country)
                            
                        case 2 :
                            year = str(input("\nEnter year: "))
                            self.print_column_names()
                            column = int(input("\nEnter data you want summary statistics for: "))
                            
                            self.display_summary_stats(column, year = year)
                            
                case 2 :
                    print("\nWhat do you want to filter by?\n")
                    print("\t1. Threshold")
                    print("\t2. Country")
                    print("\t3. Year")
                    while True :
                        try :
                            user_input_filter2 = int(input("\nEnter choice here : "))
                        except :
                            print("\nInvalid input. Please enter a number.\n")
                            continue
                        break
                    
                    match user_input_filter2 :
                        case 1 :
                            self.print_column_names()
                            while True :
                                try :
                                    column = int(input("\nEnter data you want to filter by: "))
                                except :
                                    print("\nInvalid input. Please enter a number.\n")
                                    continue
                                break
                            while True :
                                try :
                                    threshold = float(input("\nOnly show rows when it is above what threshold? :"))
                                except :
                                    print("\nInvalid input. Please enter a number.\n")
                                    continue
                                break
                            
                            filtered_data = self.filter_data_threshold(column, threshold)
                            
                            if filtered_data is not None :
                                print("| {:<20} | {:<4} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} |".format(*self.data[0]))
                                for row in filtered_data :
                                    print("| {:<20} | {:<4} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} |".format(*row))
                        
                        case 2 :
                            while True :
                                try :
                                    country = str(input("\nEnter country name: "))
                                except :
                                    print("\nInvalid input. Please enter a string.\n")
                                    continue
                                break
                                
                            
                            filtered_data = self.filter_data_country(country = country)
                            
                            if filtered_data is not None :
                                print("| {:<20} | {:<4} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} |".format(*self.data[0]))
                                for row in filtered_data :
                                    print("| {:<20} | {:<4} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} |".format(*row))
                        case 3 :
                            while True : 
                                try :
                                    year = str(input("\nEnter year: "))
                                except :
                                    print("\nInvalid input. Please enter a string.\n")
                                    continue
                                break
                                
                            filtered_data = self.filter_data_year(year = year)
                            
                            print("| {:<20} | {:<4} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} |".format(*self.data[0]))
                            for row in filtered_data :
                                print("| {:<20} | {:<4} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} |".format(*row))
                            
                case 3 :
                    print("\nWhat type of graph do you want?\n")
                    print("\t1. Pie")
                    print("\t2. Line")
                    print("\t3. Bar")
                    print("\t4. Scatter")
                    while True :
                        try :
                            user_input_graph = int(input("\nEnter choice here : "))
                        except :
                            print("\nInvalid input. Please enter a number.\n")
                            continue
                        break
                    
                    match user_input_graph :
                        case 1 :
                            self.print_column_names()
                            column = int(input("\nEnter data you want to graph: "))
                            
                            values = [float(row[column]) for row in self.data[1:]
                                      if row[column] != ""]
                            
                            py.pie(values)
                            py.show()
                    
                case 4 :
                    # Add new data to the dataset
                    # Gathers data from the user and adds it to the dataset
                    # as a new row
                    # Allows user to specify a filename to save the new dataset
                    self.add_data()

                case 5 :
                    print("Exiting...")
                    break
                
if __name__ == "__main__" :
    data = Data()
    data.display_menu()
                    
                    
                    