@echo off

call %~dp0PizzaProject\venv\Scripts\activate

cd %~dp0PizzaProject

set TOKEN=5361794779:AAH5wt4vWt3n5BbpwYFo5DcHEQbmQYA3Zns

python bot_telegram.py

pause 