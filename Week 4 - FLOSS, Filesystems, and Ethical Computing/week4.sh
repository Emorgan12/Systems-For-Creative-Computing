#!/bin/bash

read -p "What are you having for tea?: " FOOD
echo "$USER, you are having $FOOD for tea"

touch tea.txt
echo "$USER :$FOOD" >> tea.txt