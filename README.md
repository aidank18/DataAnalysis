# DataAnalysis
Welcome to my project on data analysis and cleaning!


# Problem Description
In this project I used fictional data detailing the sales of a cafe in 2023. I wanted to find out 
which products the cafe was making the most profit off of and how their sales changed as the year progressed.
This would allow me to advise the cafe on which products they should focus on to improve profits and help me identify
any slumps in sales.

# General Approach
My general approach for this project was to first clean the data using Python and its built in csv library
before exporting the cleaned data into Tableau where I could create clean and interactive visuals (linked below). These 
visuals would be key in helping me explain my findings to theoretical stakeholders.

# Problems Encountered
In general, the biggest problems came from the data themselves. The data came in a csv where each line corrosponded to
one transaction. Each transaction was supposed to have basic data as follows: 

    Transaction ID, Item, Quantity, Price Per Unit, Total Spent, Payment Method, Location, Transaction Date

Unfortunately there were many lines containing a mix of missing values, error messages, unknown values, and NaNs. 
As I didnt know which lines contained errors nor what the error values would be I had to build in checks to each value 
I looked at. Using Python I looped through each transaction and performed a series of if else checks on each value in 
the transaction to make sure it was valid. If the value was not valid I would either use the rest of the information in
the transaction to fill in the value, or if it couldnt be known I would set it to a standard UNKOWN. For example, if the
Total Spent was missing but I had the Price Per Unit and the Quantity then I could fill in Total Spent by taking
Price Per Unit * Quantity. This allowed me to fill in a serious amount of lost data, thus improving my analysis.

# Outcomes
Since this was fictional data the actual conclusions were a little silly but I was able to create two useful visualizations
that you can explore on Tableau. The first was a bar graph showing gross profit by item type sold over the whole year. 
This allowed me to easily see that salads were the cafes most profitable product sold. By including fiters I can also see 
sales month by month and see that salads were not just the most profitable over the whole year, but each month they were the 
best sellers. The only month its close is September where smoothies almost become more profitable. The second graph I have 
is a line graph showing the quantity of item sold split by month. Its not a very impressive graph becasue the data are randomly 
generated but it allows me to see that in September while salads stayed most profitable the cafe actually sold a higher quantity 
of smoothies, just more cheeply. 

By using Tableau and setting it up so the two graphs can be filters for each other the data becomes highly interactable. 
For example I can click on salad in the first graph and see the quantity sold graph change to reflect only the quantity 
of salads. In the other direction I can click on a month on the second graph and watch the first change to represent only 
gross profit for that month. I also have a seperate filter that allows me to remove certain months of data from both graphs. 
This is largely useful just to simplify the quantity graph.


# Visualization
After cleaning the data I uploaded it to Tableau to create some example visualizations, link below.
https://public.tableau.com/app/profile/aidan.knerr/viz/FictionalCafeSalesOver2023/Dashboard1
Or you can search on tableau for "Fictional Cafe Sales Over 2023" by Aidan Knerr.
