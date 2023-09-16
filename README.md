## Rtcamp Assignment


> Major Code is in api folder and respective DocTypes



**For students**

For Students They will Come and will do Signup
```
Frontend Demo URL: rtcamp.akazyti.com
```

**For HR**

(Basically HR Peoples will Use This URL (hr.akazyti.com) to do their administrative stuff)
```
backend Demo URL: hr.akazyti.com
user: Administrator
pwd: frappe


---
user: hr@akazyti.com
pwd: frappe123
```


```
demo video: https://drive.google.com/file/d/1tDiQx7fetBGQT0DCVg2ySeaEQgOa8Ssz/view?usp=sharing
```


Here is the Proposed Solution The Application Consists of 2 Faces.

1. For HR User to Do their Administrative Tasks which is Vanilla Frappe(version-14)
2. A Place for Candidates to do SignUp and See Jobs, Done using React with Parcel as Bundler

### Why Following Decision is Taken ?

1. Frappe/ERPNext is Good for Internal Team and Tools but The Website Part of Frappe Framework is not
That Flexible the Amount of Time it Takes to Do HTML and Release Forms and Deal with Version Changes
Bugs are Much More than Just Using React / Vue or Anything Else.. This Provides Some Room for Extension for App and some freedom of Choice.

2. Frappe By Itself Disables Sighup. Our Sighup is Done using A Special API can be found in api folder in auth file. This Just Leaves Room for Students to Do Sighup via API or Administrators Add HR People to Portal

### DocTypes

1. Candidate : For Keeping Information About Candidate There
2. Open Position: Open Positions in App
3. Candidate Application: Job Applications Candidate Apply

> The Names are Selected keeping Doctype Names Don't clash with ERPNext when Installed There and Can be Extendable with Hooks There. This App can Integrate with HRMS / ERPNext in Future via Hooks Using A Integrator App


### Roles

There are Following Roles By App
1. HR -> A Role for HR Professional
2. Candidate  -> A Role for Candidate

> Following As well is Done to  so that it don't clash with ERPNext or Frappe if Required

HR can do Following Things
1. CRUD on Candidate, Job Openings and Applicants

Candidate 
1. Read it's Own Information 


### Role Profiles

1. Student -> A Role Profile API Attaches to User when Candidate Sign's Up


### How Tasks are Achieved

###### A student will sign up to the ERP
Done via React App and API

##### After logging in they should be able to edit information

This is also done via custom api and Profile Page Can be Accessible from Navbar

1. Email Can't be changed because that requires a authentication method in real life. for now i have not provided into edit section

##### They should be able to see all the Job Openings

They can See List of Job Openings on Jobs Page

##### They should be able to apply for one or multiple jobs

They can Apply for Job from Job Page

1. It Allows Users to See Job but only let them submit when profile is complete

#### They should be able to edit their information such as Name, Contact Number etc

From Profile Page


##### HR should be able to do CRUD operations on the student data, Job Opening and Job Applicant

HR Should Login to Portal from FRAPPE UI not the Candidates Open Portal


##### HR should be able to create bulk interviews. I.e. Selecting multiple the Job Applicants, click on `Actions` and then select `Schedule Interview` option from the `Action List`.

1. Goto Candidate Applications Page
2. Select All Candidates
3. Click Schedule Interview
4. It will Schedule the Jobs in Background using Background Jobs
5. Background Jobs Also Publishes the Realtime Progress As well, 

> it's a open broadcast didn't cared about limiting to specific user who scheduled interview for now





### Faq's
1. Why name in Candidate is not the email of candidate ?
	 
	 because email in link is a bad practice.

2. What Features are Used to Make this App

   1. Realtime Updates
	 2. Background jobs
	 3. Frappe Whitelist API -> For Providing Custom API
	 4. Frappe Error Logging
	 5. Frappe Hooks => 

			1. Class Based for Now because it's a vanilla App
			2. hooks.py file is not used because we are not customizing any application

  3. What App Bundles with
		- 2 Roles, HR and Student
		- 1 Role Profile Called Students
		- 1 User which is Default System Manager (Because this is Dummy App)
		- Some Dummy Job Openings


### Installation

#### App

```
bench get-app <your-url-where-you-have-hosted-assignment-app>
bench --site <your-site> install-app rtcamp_assignment
```

#### Frontend

Use node 18 or grater version of it

```
git clone <your-url-where-you-have-hosted-frontend>
cd rt_camp_student_app
yarn install

yarn start
```

Please Change the .proxyrc file 

> Files Downloads will not work on parcel local setup you need to setup nginx and appropriate proxy for it

#### License

MIT
