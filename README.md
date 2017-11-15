# Rover Coding Project

Rover.com was destroyed in a terrible Amazon and GitHub accident.
Thankfully, no dogs were harmed, but we have to rebuild our site using data we retrieved from the Google search index.
We'd like to:

- Rebuild our sitter profiles and user accounts.
- Recreate a search ranking algorithm
- Build an appealing search results page

You can use any language and frameworks you'd like to complete this project.
We're a Django shop, so if you feel strong with Django, please use that.
Otherwise, use the language and frameworks that you feel will best show your skills.

The work you create here should be representative of code that we'd expect to receive from you if you were hired tomorrow.
Our expectation is that you'll write production quality code including tests.

We encourage you to to add a readme (or update the existing one) to help us understand your approach work and thought process...design choices, trade-offs, dependencies, etc. Please include instructions on how to setup/run your project locally.

Typically, the project takes 2-4 hours to complete.  There is no time limit, although we don't want to take too much of your time, so we advise people to not spend more than 5 hours on the project.

Finally, this is not a trick project, so if you have any questions, don't hesitate to ask.

### When you're done with the project...

When you're done with the project, push your work back into the repo.  Then, reply to the email you received from us letting us know you've pushed your project.  You may be tempted to email us directly, but don't do that because we rely on an applicant tracking system (ATS) to keep on top of candidates in process. Replying through it will help ensure you don't slip through the cracks.

## Rebuilding Profiles

We were able to write a script and scrape the Google index for all of the reviews customers have left of sitters.
We have saved that information in the attached CSV.
Using the information in the file, we need to design a database schema and import the data from the .csv file.

**NOTE**: If a stay includes multiple dogs, those names will be included in the same column of the CSV "|" delimited.

## Recreating the Search Ranking Algorithm

- For each sitter, we calculate Overall Sitter Rank.
- Sitter Score is 5 times the fraction of the English alphabet comprised by the distinct letters in what we've recovered of the sitter's name.
- Ratings Score is the average of their stay ratings.
- The Overall Sitter Rank is a weighted average of the Sitter Score and Ratings Score, weighted by the number of stays. When a sitter has no stays, their Overall Sitter Rank is equal to the Sitter Score.  When a sitter has 10 or more stays, their Overall Sitter Rank is equal to the Ratings Score.
- In the event that two or more sitters have the same Overall Sitter Rank, the ordering is unimportant and does not need to be handled.

The Overall Sitter Rank and it's score components must be kept up to date. That means whenever a relevant event happens, that could affect the Overall Sitter Rank, we need to recompute it.

Think about what can make the Overall Sitter Rank change.

## Building a Sitter List

We need to display the sitters on a page in order of rank. This should be easy, simply render a list of sitters.

Each row should display one sitter with their name, photo and the average of their stay ratings.

**NOTE**: Make sure your search sorting and listing can scale well to a large number of records.

## Filtering Sitters

Finally, we need to allow customers to filter out sitters on the page with poor average stay ratings.
Without making another request to the server, allow users to filter out sitters whose average ratings is below a user specified value.
It’s okay to use UI controls &mdash; sliders, checkboxes, etc &mdash; that limit the values users can enter.

## Hint for Testing the Search Ranking Algorithm
Suppose there is a sitter whose Sitter Score is 2.5 and gets rating of 5.0 with every stay. Then, their score should
behave like:

| Stay          | Overall Sitter Rank         |
| ------------- | ------------- |
| 0 | 2.50
| 1 | 2.75
| 2 | 3.00
| 3 | 3.25
| 4 | 3.50
| 5 | 3.75
| 6 | 4.00
| 7 | 4.25
| 8 | 4.50
| 9 |  4.75
| 10 | 5.00
| 11 | 5.00
| 12 | 5.00


## Setup/Running instructions
I have used Python, Flask, Angularjs 1.x and Sqlite. 
'requirements.txt' has all the dependency modules.

To create schema and load the data run below command
'python loadData.py database_schema.txt reviews.csv'

To run the app run below command
'python main.py'

In a browser, open 'http://127.0.0.1:5000/' and you should see the list of sitters in descending order of their overall rank
You can use filter to filter out the sitters with lower rating score

Test cases are written under 'tests' directory

## Assumptions
I have assumed that dog's name per owner is unique so that we can build the data and add additional details like breed, 
size of the dog etc.


## Drawbacks
While loading the script, due to time constraint, I am currently querying db to get the sitter information (rating and 
number of reviews) to calculate the rating score and overall rank. This is done for every row read from the file 
which is an overhead. 


## Solution
We can store the average rating and number of reviews per sitter in Redis as we read the data from the file.
 
 sitter_id: {
    rating_score: <rating_score>,
    number_of_reviews: <number_of_reviews>
 }
 
