#!/bin/zsh

# usage: run.zsh problem_name input_file

g++ -std=c++17 ~/Kattis/$1/$1.cpp -o ~/Kattis/$1/$1
~/Kattis/$1/$1 < ~/Kattis/$1/$2