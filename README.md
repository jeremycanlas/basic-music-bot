# basic-music-bot

A basic music bot based on the tutorial https://www.youtube.com/watch?v=dRHUW_KnHLs&t=1s&ab_channel=Computeshorts. 

Some changes I have made:
1) Migrated to nextcord
2) I modified it so that music_queue is unique to each server instead of sharing the same queue as well as being able to play music in different servers all at once. 

    Specifically in the function play_music:
    
    ```
	async def play_music(self):
      # stuff
      if self.vc == None or not self.vc.is_connected():
	```
    I changed it to
    ```
    async def play_music(self):
      # stuff
      voice_client = nextcord.utils.get(self.bot.voice_clients, guild=ctx.guild)
      if self.vc == None or not voice_client:
    ```

3) Migrated from youtube_dl to yt-dlp because of some issues I was facing with youtube_dl https://github.com/yt-dlp/yt-dlp.
4) The bot also uses azapi https://github.com/elmoiv/azapi to get the lyrics of the currently played song. Need better exception handling.

---
## WIP How to create a bot
1) Click on **New Application** at the upper right corner and name your application anything you want in https://discord.com/developers/applications.


    <img src= "https://user-images.githubusercontent.com/80456535/219927014-96d7d8bc-6bac-418d-9962-0ba4e452bfe3.png" width="400" height="400">

2) Select **Bot** on the left menu and click on **Add Bot**.
    
    
    ![image](https://user-images.githubusercontent.com/80456535/219930044-8bec56ff-5a79-4151-b50e-63c0db3936f7.png)

## How to run the bot
1) Create a python virtual environment `virtualenv .venv` and go into your virtual environment `.venv\Scripts\activate`
2) Install dependencies `pip install -r requirements.txt`
3) Create a `.env` file in your main project directory and add your bot token there

    Example:
    `TOKEN=123412-0391203token120348129083`
4) 

