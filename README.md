# Data Glacier Virtual Internship 

# Week1 - Version Control Assignment
Clone the VC repo (https://github.com/DataGlacier/VC.git Links to an external site.), create a new branch, checkout the newly created branch, run the add.py and provided my name and fav sport as input, run the test script using the command: pytest test/test.py -s, ignore warning and if there is no error then add, commit and push your changes to the repo.

# Week 2 - G2M insight for Cab Investment firm
The Client
XYZ is a private firm in US. Due to remarkable growth in the Cab Industry in the last few years and multiple key players in the market, it is planning for an investment in Cab industry, and as per their Go-to-Market(G2M) strategy they want to understand the market before taking the final decision.

There are multiple data sets that contain information on 2 cab companies. Each file (data set) provided represents different aspects of the customer profile. XYZ is interested in using your actionable insights to help them identify the right company to make their investment.

Deliverables:

• Exploratory Data Analysis(EDA) 

• Data Intake Report 

• Multiple hypotheses and recommendation

# Week 3 - Presentation of Week2 Use Case
Presentation is prepared for Week 2.

# Week 4 - Deployment On Flask
Machine learning model is deployed using Flask For this week. In this project, we've created a machine learning model that can predict a customer's annual income category by analyzing various demographic and behavioral attributes. We chose the Logistic Regression algorithm to build our predictive model, as it is a widely used method for tackling classification problems. We used a dataset that contains information about customers, including their age, gender, profession, spending score, work experience, and family size.

After we were done with the implementation of our model, we started to deploy our model on Flask. Our web application designed to predict a customer's annual income category based on their demographic and behavioral attributes. By inputting relevant customer data such as age, gender, profession, spending score, work experience, and family size, users can quickly receive predictions about the customer's annual income category. These categories include 'Very Low', 'Low', 'Moderate', 'High', and 'Very High'.

# Week 5 - Cloud and API Deployment
In this week, we used the model that is deployed last week by using Flask Framework and deployed our model on Heroku which is a container-based cloud Platform as a Service (PaaS).

# Week 6 - File Ingestion and Schema Validation
We processed a large CSV/Text file (2+ GB) using various Python libraries: pandas, Dask, Modin, and Ray. We measured the computational efficiency of each method. The data columns were validated by removing special characters and white spaces. We created a YAML file to store the column names and separator. We confirmed the data's integrity by checking it against the YAML file. The processed data was written to a pipe-separated text file in gzip format. The summary included the total rows, total columns, and file size.
