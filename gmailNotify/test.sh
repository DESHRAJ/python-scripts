#!/bin/bash
for i in {0..100..10}
    do
          killall notify-osd
          notify-send "testing" $i
          sleep 3
    done