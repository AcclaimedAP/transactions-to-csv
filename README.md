# Converting transactions to CSV

A simple python script that runs through a text file with transactions and tries to format it into a .csv file.

### Instructions

There's two parts, first, the main.py code expects a file as argument, and the file has to follow the conventions specified further down.

It runs through the transaction list and splits up the transactions into a .csv format.

The group_by_type_and_date.py file will expect both a file and a type to check for.
It will only extract the transactions that match the specified type, and group them by date. It also excludes expenses, and only takes in income transactions. 


### Expected format of data

The data has some expectations, first, the data takes these values:
A date, which follows the format of YYYY-XX-XX. It should handle both YYYY-MM-DD and YYYY-DD-MM, however they have to be split by dashes, and consist of 4, 2 and 2 in length.
It then tries to extract the amount and balance, which has these expectations:
The amount uses a comma as decimal separator.
It uses space as thousand separator.
It does not handle million separator, as the transactions I was working with did not reach in the millions, it was not an issue for me, however it should be possible to add that as well.

After the Date, amount, and balance is extracted, the rest will be considered as a "reference", and it will try to strip whitespaces.

### Why

I got asked to help formatting these transactions, so I made a python script to ease the work. It is not flexible at all, and the input is a copy&paste from "SveaBank" pdf transactions export, with some very light pre-processing.

Please don't use this for anything serious, it's usecase is extremely niche and should at best be used as a reference.