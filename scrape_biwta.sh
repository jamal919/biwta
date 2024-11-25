#!/bin/bash
source /home/khan/.local/modules/miniconda/bin/activate scraper
python scrape_biwta.py
echo `date`
