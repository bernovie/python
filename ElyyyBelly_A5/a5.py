import string

def getChoice():
    option = raw_input("Please enter your choice: ");
    return option.lower();

def openFile():
    fileName = raw_input("What is the name of the file? ");
    fileMode = raw_input("Please enter the file mode: ");  
    return file(fileName, fileMode);

def myMethodIsBetter(self, parameter_list):
    pass
    
def printReport(myFile):
    total = 0
    total_pizza_profit = 0;
    pizza_type = myFile.readline().rstrip('\n').rstrip("\r")
    while pizza_type != '':
        pizza_price = float(myFile.readline().rstrip('\n'))
        pizza_cost = float(myFile.readline().rstrip('\n'))
        pizza_profit = pizza_price - pizza_cost
        total += 1
        total_pizza_profit += pizza_profit
        average_profit = total_pizza_profit / total
        print "\n\nPizza: ", pizza_type
        print"Price: $", format(pizza_price, '.2f')
        print "Cost: $", format(pizza_cost, '.2f')
        print "Profit: $", format(pizza_profit, '.2f')
        pizza_type = myFile.readline().rstrip('\n').rstrip("\r");
    print "\n\nEnd of file!" 
    print "A total of", total, "pizzas have been processed."
    print "The average profit is $", format(average_profit, '.2f')
    myFile.close()
    return 0;

def updateFile(inputFile, outputFile):
    numFileRecords = int(raw_input("How many records? "));
    for i in range(0, numFileRecords):
        inputPizzaType = inputFile.readline().rstrip("\n");
        inputPizzaPrice = float(inputFile.readline().rstrip("\n"));
        inputPizzaCost = float(inputFile.readline().rstrip("\n"));
        inputPizzaProfit = inputPizzaPrice-inputPizzaCost;
        outputFile.write(inputPizzaType+"\n"+str(inputPizzaPrice)+"\n"+str(inputPizzaCost)+"\n"+str(inputPizzaProfit)+"\n");
    outputFile.close();
    inputFile.close();
def main():
    getPrompt = "y";
    welcomeMessage = "Welcome to the file Program\n";
    welcomeMessage += "=============================\n";
    welcomeMessage += "P - Print Report\n";
    welcomeMessage += "U - Update File";
    while (getPrompt == "y"):
        print welcomeMessage;
        option = getChoice();
        if(option == "u"):
            print "Open input file: \n"
            inputFileName = raw_input("What is the name of the file? ")
            inputFileMode = raw_input("Please enter file mode: ");
            inputFile = file(inputFileName, inputFileMode);
            print "Open output file: \n"
            outputFileName = raw_input("What is the name of the file? ");
            outputFileMode = raw_input("Please enter file mode: ");
            outputFile = file(outputFileName, outputFileMode);
            updateFile(inputFile, outputFile);
        elif(option == "p"):
            myFile = openFile();
            printReport(myFile);
        else:
            print "Invalid choice!\n\n";
        getPrompt = raw_input("Do you want to continue? (Y or y for yes):").lower();
    return 0;

main();
        