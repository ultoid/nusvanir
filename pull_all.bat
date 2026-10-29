@echo off
echo ========================================================
echo  Menarik Pembaruan Repositori Nusvanir ^& Game Project
echo ========================================================
echo.

echo [1/2] Menarik pembaruan Nusvanir (World Building ^& Database)...
git pull origin main
echo.

echo [2/2] Menarik pembaruan Game Project (Tales of The Dark Time)...
git -C "Game Project\Tales of The Dark Time" pull origin main
echo.

echo ========================================================
echo  Pembaruan Selesai! Kedua repositori telah sinkron.
echo ========================================================
pause

