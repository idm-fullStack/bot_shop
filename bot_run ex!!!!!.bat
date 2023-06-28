 @echo off

 call %~dp0bot_shop\venv\Scripts\activate  

 cd  %~dp0bot_shop

 set TOKEN=your token

 python bot_shop.py
 
 pause
