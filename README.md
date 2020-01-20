SLGO OBIS Workshop - Jan 21-23 2020

This workshop has been adapted from the standard 4.5 day OBIS training workshop and tailored to an audience of software developers and data management professionals working at the St Lawrence Global Observatory in Rimouski, QC. Understanding that the audience expertise trends more towards Python than R, the R package component has been replaced by a hands-on walkthrough of how to interface directly with the OBIS and WoRMS APIs from Python. R examples are provided in ipython notebook format but are not core to the learning experience.

As SLGO is a world-class operational data aggregation and management platform actively serving a large and important ocean region in Canada, we also choose to encourage participant-directed subject matter and attempt to focus on operational outcomes that serve SLGO moving forward in the important hands-on sessions.

#### Facilitators
**Name** - *(home OBIS node)* email

Jon Pye - (Ocean Tracking Network) - jdpye@dal.ca

Brian Jones -  (Ocean Tracking Network) - brian.jones@dal.ca

Naomi Tress - (Ocean Tracking Network) - ntress@dal.ca

Many thanks to Ward Appeltans, Leen Vandepitte, Pieter Provoost, Daphnis De Pooter, Abby Benson and all those throughout the OBIS community who helped build and refine the source material used in assembling this workshop. We hope that our adaptation is useful, fit for purpose, and results in productive outcomes for these and other prospective OBIS contributors.

### Specifics of the initial request:

An existing biodiversity application is introspecting and serving data from an internally developed database that is very close to OBIS-compliant. Database designed to run the portal and is not necessarily an ideal data representation. Data and metadata live in this portal and a CKAN instance. Looking for a system-to-system approach to meeting OBIS compliance without designing too-disparate data pipelines. Considering all options and welcoming advice on meeting these goals.



### Goals of the Workshop:

Give attendees an idea of what OBIS is and how it functions, why and how to become compliant with OBIS data and metadata formatting and data policy, how OBIS reporting pipelines work. Allow time to investigate solutions to meeting OBIS-compliance from the existing biodiversity data portal at SLGO. Build prototype or work plan to do so.  


### Schedule:

**Day 1**

09:00  -  Welcome, Introductions, goals for the workshop  

Intro to OBIS

Intro to WoRMS

*10:20     Break*

10:35  -  Darwin Core I

History of DarwinCore  

Occurrence Core and Event Core

Occurrence, Location, Time, and Quantity in Darwin Core

12:00     Lunch

13:00  -  Darwin Core II  

Darwin Core Archives – how to represent DwC schemas and types

Occurrence Core, MeasurementOrFact, Event Core

Representing Event Core in DwC Archives

Ecological Metadata Language and OBIS

*14:20     Break*

14:35  -  Data processing, taxon matching, QC using the OBIS and WoRMS APIs

WoRMS

Accessing WoRMS webservices (REST API)

OBIS

Using the OBIS Data mapper to discover OBIS held datasets

OBIS API v3 – using the REST API  



**Day 2**

09:00  -  Becoming / contributing data to an OBIS Node

Process and organizational hierarchy

Technical / Policy implications

  OBIS Guidelines on Data Sharing and Use

Motivations for sharing data for curation

License selection and OBIS data license

Researcher control of additional restrictions w/ licensing

*10:20  -  Break*

10:35  -  Registering Datasets with OBIS IPT (and GBIF)

Use the OBIS IPT to register datasets and produce EML entries.

12:00  -  Lunch

13:00  -  Hands-on session 1 – mapping SLGO datasets to DwC archives

Select dataset to map and migrate the data and metadata to a DarwinCore archive

Register the resulting archive with a test IPT, building the EML

*14:20  -  Break*

14:35  -  Hands-on session 1 – cont. – Mapping datasets from OGSL.ca/bio to DwC Occurrence Core

Demo – mapping of output from ogsl.ca/bio extract to DwC terms.

Collaboratively map data flow from SLGO backend to DwC archives



**Day 3**

09:00  -  Hands-on session 2 – User-directed project(s)

Will identify one or more useful OBIS-adjacent projects / data pipelines / outcomes that SLGO staff identify as important and build towards implementation of those outcomes.

Suggested topics:

Work towards MVP of OBIS-compliant archives for SLGO biodiversity data

Build process to map and keep current SLGO-held data as it’s currently ingested or held into updating DwC archives in either OBIS Canada or a custom SLGO IPT

Build Python implementations of robis and/or obistools



12:00  -  Lunch

13:00  -  Infrastructure exercise – deployment [plan for] test-mode IPT for use at SLGO

Deploy or plan the deployment of an Integrated Publishing Toolkit to SLGO infrastructure. Continue to work in teams on user-directed projects from Hands-on Session 2

*14:20  -  Break*

14:35  -  Question and Answer, Wrap-up and Next Steps  

Answer questions, evaluate workshop content, and plan necessary follow-ups
