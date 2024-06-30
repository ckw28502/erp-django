@echo off
for /d %%D in (*_app*) do (
    py -m flake8 %%D
)