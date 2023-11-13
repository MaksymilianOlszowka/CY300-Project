import csv
import matplotlib.pyplot as py
    
exit = False
fileName = "Project/smoking.csv"
columnNames = []
rows = []

with open(fileName, mode = 'r') as (inFile) :
    readerFile = csv.reader(inFile)
    columnNames = next(readerFile)
    
    for (row) in (readerFile) :
        rows.append(row)
        
class Data :
    def __init__(self, countryName: str, rows: list, countryYear: str = None,
                 sex: str = None) :        
        self.countryName = countryName
        self.dailyCigarettes = 0
        self.percentageMale = 0
        self.percentageFemale = 0
        self.percentageTotal = 0
        self.smokersTotal = 0
        self.smokersFemale = 0
        self.smokersMale = 0
        self.count = 0
        
        def fillData(self) :
            # initializes the __init__ variables with meaningful data
            self.count += 1
            self.dailyCigarettes += float(row[2])
            self.percentageMale += float(row[3])
            self.percentageFemale += float(row[4])
            self.percentageTotal += float(row[5])
            self.smokersTotal += int(row[6])
            self.smokersFemale += int(row[7])
            self.smokersMale += int(row[8])
            
        def calculateMean(self) :
            # calculates the mean for every __init__ variable               
            self.avgDailyCigarettes = (self.dailyCigarettes / self.count)
            self.avgPercentageMale = (self.percentageMale / self.count)
            self.avgPercentageFemale = (self.percentageFemale / self.count)
            self.avgPercentageTotal = (self.percentageTotal / self.count)
            self.avgSmokersTotal = (self.smokersTotal / self.count)
            self.avgSmokersFemale = (self.smokersFemale / self.count)
            self.avgSmokersMale = (self.smokersMale / self.count)    
        
        for (row) in (rows) :
            if (countryYear != None) :
                if (countryYear) in (row) :
                    fillData()
            else :
                if (countryName) in (row) :
                    fillData()
            if (sex != None) :
                fillData()
     
        calculateMean()
             
    def returnMean(self) -> list :
        # returns the mean of every variable in the __init__ method
        return [self.avgDailyCigarettes,
                self.avgPercentageMale,
                self.avgPercentageFemale,
                self.avgPercentageTotal,
                self.avgSmokersTotal,
                self.avgSmokersFemale,
                self.avgSmokersMale]      
    
    def returnCount(self) -> int:
        # returns the total count of whatever is trying to be measured 
        # (i.e) total counts for a country, year, or sex
        return self.count
       
    def minMax(self, rows: list) : 
        # returns the minimum and maximum values for every variables within the
        # __init__ method
        return None
            
while (exit == False) :
    # primary main menu code
    print("\nWhat do you want to see?", end = '')
    print("\n\n\t1. Summary Statistics\n\t2. Graphing\n\t3. Adding Data \
          \n\t4. Exit")
    
    userInput = int(input("\nEnter choice here : "))
    
    match (userInput) :
        case (1) :
            print("\nWhat do you want to filter by?")
            print("\n\t1. Country\n\t2. Year\n\t3. Gender")
            
            userInputFilter = int(input("\nEnter choice here : "))
            
            match (userInputFilter) :
                case (1) :
                    print("\nWhich country?\n")
                    
                    userInputCountry = str(input("Enter country name: "))
                    # create a class object of the country of choice
                    # print summary statistics in table for input country
                    
                    
                case (2) :
                    print("\nWhich year?\n")
                    
                    userInputYear = int(input("Enter choice here: "))
                    # create a class object of the year of choice
                    # print summary statistics in table for input year
                    
                case (3) :
                    print("\nMale or Female?\n")
                    
                    userInputSex = str(input("Enter choice here (M/F) : "))
                    # create a class object of the sex of choice
                    # print summary statistics in table for input sex
                    
        case (2) :
            print("\nWhat type of graph do you want?")
            print("\n\t1. Pie\n\t2. Line\n\t3. Bar\n\t4. Scatter")
            
            userInputGraph = int(input("\nEnter choice here : "))
            # use matplotlib methods and functions to create the plot
            # according to user choice
            
        case (3) :
            print("\nNew or existing country?")
            print("\n\t1. New\n\t2. Existing")
            
            userInputCountry = int(input("\nEnter choice here : "))
            # create functions or use pre built ones in Python csv
            # to append new data to the dataset
            
        case (4) :
            print("\nGoodbye!\n")
            exit = True