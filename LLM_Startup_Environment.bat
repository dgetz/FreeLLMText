@echo off
:: This opens the two folder locations for moving files around
start explorer.exe "C:\Users\Dan\Documents\LLMDownloads\Complete"
start explorer.exe "C:\Users\Dan\Documents\LLMDownloads\To Be Appended"

:: This opens GitHub desktop
start "" "C:\Users\Dan\AppData\Local\GitHubDesktop\GitHubDesktop.exe"

:: Open ChatGPT for programming questions
start firefox.exe "https://chat.openai.com/"

:: Open python
python -m idlelib.idle "C:\Users\Dan\Documents\GitHub\FreeLLMText\Text_File_Appender.py"