# SI507-Final-Project


## Instructions: 
1. To run application, navigate to the project folder and run $ python3 webpage/flaskpage.py
2. Once you view the page, enter a link to a Spotify Playlist, select a vibe, and click Check Vibe
  * I have created several test playlists for this 
  * [Party Playlist](https://open.spotify.com/playlist/4ZkR6u2ZfGWj1UwT7i6MwI?si=4d24aa7570a6414e
  * [Car Jams Playlist](https://open.spotify.com/playlist/1lBJ68syJlYWq6iNjSnygm?si=ed3fddc0bf2246e8)
  * [Kickback Playlist] (https://open.spotify.com/playlist/1axW5f4McdO9GTk3oY0Wcs?si=48212f5dc4114956)
  * [Quiet Playlist] (https://open.spotify.com/playlist/0ydK0BtZX9Dor3lBe25bw2?si=4578704df0034079)
  
## Data Structures
* My data structure is primarily trees. Whenever a new playlist is input into this system, my program takes its song data and enters it into the tree to be a reference for recommendations. Once the tree has been built, I cache it into a file to save the data. When it’s time to make a recommendation, the program retrieves the data from the cached file, rebuilds the tree, finds a range of scores based on the vibe the user wants, and retrieves a random song in that range and suggests it to the user. 
I pre-loaded several playlists from both Top 40 hits and from my personal playlist library to give the tree some initial data to work with when making recommendations
* JSON file: song_data.json
* Standalone: caching.py



