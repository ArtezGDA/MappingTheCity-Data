# Mapping the City - Data

##### Shared Data collections with data sources about cities and agglomeration.

This repository will hold the collection of data that is to be researched and scraped for the [Mapping the City](https://github.com/ArtezGDA/Course-Material/blob/master/MappingTheCity.md) assignment.

Currently it contains two files:

- [List_of_Resources.md](List_of_Resources.md): a list containing possible source of data
- [Collaborative_Research.md](Collaborative_Research.md): a list of student groups and their research topics

For each research topic the following file structure should be created

- Folder with the topic of the research
	- a `README.md` file describing:
		- a url to the original data (where it was downloaded from)
		- a url to the meta data about this data (the page explaining what it is)
		- the purpose of the research, research goal or hypothesis
		- the contents of the source data
		- the structure of the scraped data and all of its attributes
		- an explanation of the tools created and used to get from the source to the groomed data
		- a how to install and use of these tools
		- a list of contributers and authors of these tools (your names)
	- Folder with the `Source_Data`
		- Source data as `.csv` file
		- Make sure the file is not ridiciculous large > 5 MB. If it is don't include it, just link to it.
	- python scripts to scrape and groom the data
	- Results as .json file
		- If there are more than one .json file, put them in a `json_data` folder