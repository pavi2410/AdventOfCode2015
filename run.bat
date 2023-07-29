@echo off
setlocal EnableDelayedExpansion
setlocal EnableExtensions

set day=%1
set command=%2
if !day! LEQ 9 (
  set day=0!day!
)
if !command! EQU t (
  set test=day!day!/test.py
  echo Running !test!
  pytest !test!
) else (
  set main=day!day!/main.py
  echo Running !main!
  py !main!
)
