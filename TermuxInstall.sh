# @TheBaghirov - < https://t.me/TheBaghirov >
# Copyright (C) 2022
# Bütün haqları qorunur.
#
# Bu fayl, < https://github.com/bghrff/FileLock > parçasıdır.
# < https://www.github.com/bghrff/FileLock/blob/master/LICENSE/ >
# ================================================================

DOGE="🔐 FileLock kitabxanası qurulur..."
INFOX="📣 Telegram: @TheBaghirov"
INFOX+="\n "
INFOX+="\n💬 Dəstək Kanalı: @bybaghirov"
INFOX+="\n "
INFOX+="\n💫 PROSES DAVAM EDƏRKƏN TƏTBİQDƏN AYRILMAYIN!"
PACKAGEX="\n⏳ PAKETLƏRİ GÜNCƏLLƏYİRƏM..."
PYTHOX="\n⌛ PYTHON QURURAM..."
REQUIREX="\n⌛ LAZIM OLANLARI QURURAM..."
SPACEX="\n "
clear
echo -e $DOGE
echo -e $SPACEX
echo -e $SPACEX
echo -e $PACKAGEX
echo -e $SPACEX
pkg update -y
clear
echo -e $DOGE
echo -e $SPACEX
echo -e $INFOX
echo -e $SPACEX
echo -e $PYTHOX
echo -e $SPACEX
pkg install python -y
pip install --upgrade pip
clear
echo -e $DOGE
echo -e $SPACEX
echo -e $INFOX
echo -e $SPACEX
echo -e $REQUIREX
echo -e $SPACEX
pip install wheel
pip install -U FileLock
python3 -m FileLock
