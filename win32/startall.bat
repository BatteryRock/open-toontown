@echo off
start "Starting Astron..." "start_astron_server.bat"
timeout /t 1 >nul
start "Starting UberDOG..." "start_uberdog_server.bat"
timeout /t 4 >nul
start "Starting AI..." "start_ai_server.bat"
timeout /t 4 >nul
start "Starting the game..." "start_game.bat"
