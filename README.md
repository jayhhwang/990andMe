# 990andMe
Find the fund for you!

# Introduction
IRS has provided 990 tax forms for nonprofit companies in XML format. This is not a format that is most easily used for querying or analyzing.

The Nonprofit Sector is big.  
Approximately 1.56 million nonprofits are registered with IRS.  
Nonprofit sector accounts for 5.4% ($985.4 billion) of the country's GDP.  
In 2017 alone, total private giving totaled $410.02 billion  
  
Boosting the number of contributors and recipients is a win-win for everyone

# Dataset
Form 990 is the form used by the United States Internal Revenue Service (IRS) to gather financial information about nonprofit organizations. By making electronic 990 filing data available, the IRS has made it possible for anyone to programmatically access and analyze information about individual nonprofits or the entire nonprofit sector in the United States. This also makes it possible to analyze it in the cloud without having to download the data or store it themselves, which lowers the cost of product development and accelerates analysis.

Each electronic 990 filing is available as a unique XML file in the “irs-form-990” S3 bucket in the AWS US East (N. Virginia) region. Information on how the data is organized and what it contains is available on the IRS 990 Filings on AWS Public Data Set landing page.

# Architecture
The data pipeline ingests from S3 into a Spark Cluster of EC2 Instances. The data is then processed using PySpark and uploaded into a MySQL database. A quick demo of the database is shown using a Tableau dashboard using live data connected to the MySQL database.  
  
Why did I choose my technology stack?  
  
S3 - IRS 990 forms were uploaded into an open S3 bucket  
Spark/EC2 - Flexible, scalable way to quickly manipulate XML files using Spark DataFrames  
MySQL - A schema-defined, relational database works well with the structured information provided by the XML files  
Tableau - A quick and easy way to demo use cases for the database  


![990andMe Pipeline](https://github.com/jayhhwang/990andMe/blob/master/images/pipeline.png)

# Engineering Challenges
Challenge #1:  
XML needs to be converted into a document that more readily stored by databases and processed by data scientists  
  
Solution:  
Used Databrick’s spark-xml package to convert XML to Spark DataFrames  
  
Challenge #2:  
Form formats differ between the forms (private foundation forms, public charity forms, etc.)  
  
Solution:  
Defined a schema for targeted sections (e.g. Filer information, Recipient information, etc.) that are shared across all forms

# What would I have done differently?
If I had more time, I would have set up a scheduler (e.g. AirFlow) to automatically digest monthly updates. I would have experimented with the size of my cluster to lower the processing time. Ideally, I would also automate the time-consuimg setup and configuration steps using a configuration management tool (e.g. Ansible).

# Links
[Slides](https://docs.google.com/presentation/d/1n87A_ZblqnpErJ5HqVuKxwYqb4mQ7zPJlx6LLg4b2kw/edit?usp=sharing) | [Demo](https://public.tableau.com/profile/jay.hwang#!/vizhome/Insight_Demo/Demo)
