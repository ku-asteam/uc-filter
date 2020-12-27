# UC-Filter
User-Content Filter Module via Statistical Analysis of User-Content Rating Matrix

## Introduction
User-Content Filter is a implementation of *a*STEAM Project (Next-Generation Information Computing Development Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Science and ICT). The function of this module is to downsize datasets with smaller system parameters, consisting of popular contents that were rated by active users, which thus alleviates the difficulty of analysis in mobile networks with large system parameters.

## Requirements and Dependencies
- `python >= 3.7`

## Instructions
* Prepare base data that contains a set of contents and a set of users who have reacted to some of the contents. (`data format: ['id', 'user', 'content', 'rating']`)
* Execute `uc-filter.py`

```shell script
$ python uc-filter.py BASE_DATA_FILE OUTPUT_FILE USER_SIZE CONTENT_SIZE REMOVE_SIZE
```

`BASE_DATA_FILE`: base data file's path

`OUTPUT_FILE`: output file's path

`USER_SIZE`: user size of filtered user-content rating matrix

`CONTENT_SIZE`: content size of filtered user-content rating matrix

`REMOVE_SIZE`: removing the top-N to prevent matrix from becoming too dense