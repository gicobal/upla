#!/bin/sh

a=0
b=3

while [ $a -lt $b ]
do
   python upla.py
   a=`expr $a + 1`
   sleep 100m
done
