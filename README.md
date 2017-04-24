# Minions
This repository works for monitoring text file changes and triggering job based on json content.  It provides a watch dog daemon which reads json files and periodically updates.
Basically a replacement for  cronjob, which provides more intuisive management - using folder structure.

# Getting started
Let's see a example from template.json

{
  "name": "ps command",
  "command": "ps aux"
}

Modify main() in boss.py and load this config.
