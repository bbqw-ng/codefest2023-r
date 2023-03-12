# CODEFEST 2023: COMCAST EFFICIENT MEETINGS CHALLENGE!
### Backend Dev: Francis Nguyen // Frontend Dev: Brian Wang
---
### Purpose
This is a machine-learning program that will determine whether a meeting should be hosted in-person or be written in an e-mail instead.
We use a decision tree algorithm for a number of reasons:
1.) it's easier to visualize and add/remove from a decision tree model,
2.) decision nodes would be easier to provide metrics about the meeting (like the agenda, purpose, affiliates, etc.),
3.) creating a decision tree closely fits into how a software engineer would determine whether or not the meeting had been summarized on an e-mail.

### How it works

We wanted to improve upon many of the modern-day scheduling and calendar softwares using artificial intelligence (how cool would that be!).
This program could be implemented to schedules that deal more with the software development industry. A user can create a "post" on a calendar,
and they can add "tags" which pertains to the decision nodes on our decision tree model (see below). After each meeting, an e-mail would be sent
to every participant attached with a survey asking "Could this meeting have been summarized in an e-mail? (Yes/No)". Then, the survey data would
be accumulated into a .csv alongside the rest of our category data from the scheduling system. The survey data is our "target" which is used for
training data.

Our machine learning algorithm recognizes patterns of categories that are grouped together and outputs a value that predicts whether the meeting
should be held in-person or be written on an e-mail.

### Libraries, Citations, and Microframeworks Used

Pandas for Database Organization
Bootstrap for CSS and HTML handling
Flask for HTML microframework
Sklearn for Decision Tree Model

### Images
![yLEa6QAAAABJRU5ErkJggg](https://user-images.githubusercontent.com/110130404/224533710-bdf3785b-ab87-4a7f-81b0-b724c62c2722.png)
