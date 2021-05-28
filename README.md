# CoWIN Bangalore Datadump

## Note: It will expand to about ~130GB, so be careful with that!

Click [here](https://mega.nz/file/m44FEAQY#mh728A01ZqbhfHcW2YztBC0oouSEEwC0n4XYHjQc_IQ) to download the file.

File names:

- City + Unix Timestamp when file is created + [Sessions / Telegram / Twitter]

- Example file names
  - `Bangalore-1620826549-sessions`
  - `Bangalore-1620826549-telegram`
  - `Bangalore-1620826549-twitter`
  
  All the files and data are in **JSON** format.

Sessions files:

- Array of calls made, each object contains the time the call was made, and the time the call was received, and the sessions object contains the data returned by CoWIN.

Twitter files and telegram files:

- These contain an array of calls made to Twitter API or Telegram API to send tweets or messages, each object contains the time call was made and the time a success message was received, this also contains the `session_id` which is the `Unique ID` used to represent a session on CoWIN and can be found attached to sessions in the sessions file

Lastly, go crazy with the data and try to find any patterns you can 😊 maybe things like how my tweets are affecting the speed at which slots are disappearing?

Feel free to raise issues or ask questions, and I will respond as soon as I can.
