# <p align="center"> <ins>Python Challenge :desktop_computer:</ins>  

## PyBank and PyPoll

In this work, I first created a python script, which analyses the financial records of PyBanks, after reading a set of finacial data called [budget_data.csv](PyBank/Resources/budget_data.csv). This dataset is composed of two columns: 
> Date

> Profit/Losses 

This python script would analyse the records and calculate the following:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

[Finacial Analysis](https://github.com/HJandu/Python_challenge/blob/main/PyBank/Output/budget_data.txt)

```text
Finacial Analysis
------------------------
Total Months:    86
Average Change:    $-8311.11
Greatest Increase in Profits:  Aug-16  ($1862002)
Greatest Increase in Profits:  Aug-16  ($1862002)
Greatest Decrease in Losses:  Feb-14  ($-1825558)
```

The second python script was created to analyse the election result of PyPoll, using the [election_data.csv](PyPoll/Resources/election_data.csv). This dataset is composed of three columns: 

> Voter ID

> County

> Candidate

This python script would analyse the votes and calculate the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote

[Election Results](https://github.com/HJandu/Python_challenge/blob/main/PyPoll/Output/election_data.txt)

```text
Election Results
-----------------------
Total Votes:  369711
------------------------
Charles Casper Stockham:  23.049%  (85213)
Diana DeGette:   73.812%   (272892)
Raymon Anthony Doane:   3.139% .  (11606)
------------------------
Winner:  Diana DeGette
```









