# SpotifyPoetry (early development)
## 
Inspired by Tumblr project Spotify Poetry (http://spotifypoetry.tumblr.com). Generating a Spotify playlist with titles that match an input poem. Objective is to practice using popular APIs with Python as a personal project for practice/fun. Python scripts continuously being updated.

### Purpose:
Powered by Spotify’s API. This program allows you to write a poem in the command line and receive a playlist of songs whose titles match the input text. 

### Method:
First time working with an Web API and Python. My main goal is to document and outline my thought process for solving the problem (seen below) and different algorithms I am thinking of using (outlined in **theory.txt**). 

#### Problem Solving Process:
  1. Understand goal and how inputs and outputs from API are structured.
  2. Create tentative timeline and plan for project.
  3. Outline a theoretical solution.
  4. Jump in and CODE!!! Trial and error. 
  5. Repeat steps 4-5. Revist 1-3 when necessary.

### Overview:
 * **spotifypoem.py** contains all Python code. 
 * To install, first clone the repo:
```
	git clone https://github.com/thisisspartina/spotifypoetry
```
 * Program executed via:
```
        python spotifypoem.py
```
  *(Note: Errors will occur and noted in "Main Issues")*

  * Assumed the following already installed. Four external Python libraries are currently used: 
    * `requests` is used to query the Spotify Metadata API 
    * `requests_cache` transparent persistent cache for requests
    * `pprint` make that json output look pretty :)
    * `string` help with messing around with input string
 
* Another program was written using using a lightweight Python library for the Spotify Web API, `spotipy`. This was to test out other Python libraries. It is not completed. Included as **spotipyexample.py** to show other methods I began experimenting with. https://github.com/plamere/spotipy
 
### Main Issues to Fix, Next Commit:
 * String splits into separate words. Also removes apostrophes from contractions or possessive words. 
 * Not optimized solution. Better coding with more time exploring Python.
 * Only partial solution, does not produce intended output. Code needs updating.
 * No test-coverage. Best practices in program writing is to include tests for new code that is written. 

## Future Advanced Improvements:
 *  After getting code to a working state, look at parallelizing query search. Everything sequentially mapped out now.
 * 'Redis' for caching the API results for later reuse.
 * `Flask' for possible web implementation. (That would be pretty awesome actually. XD )
 * Use `argparse` to allow loading of poems in command line.
