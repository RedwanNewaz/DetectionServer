#!/usr/bin/env bash
clear
OBJ_DETECTOR_SERVER=http://0.0.0.0:5000/
test()
{
  echo "posting image to $OBJ_DETECTOR_SERVER"
  DATA=`cat /home/redwan/Pictures/pedstrians/DV1842346-abbey-road-beatle.jpg|base64 -w0`
  curl $OBJ_DETECTOR_SERVER -F "data=$DATA" -X POST
}

with_param()
{
  DATA=`cat $1|base64 -w0`
  echo "posting $1 to $OBJ_DETECTOR_SERVER"
  curl $OBJ_DETECTOR_SERVER -F "data=$DATA" -X POST
}

#test
with_param "/home/redwan/Pictures/pedstrians/DV1842346-abbey-road-beatle.jpg"