#!/bin/bash
source /home/khan/.local/modules/miniconda/bin/activate scraper
python scrape_biwta.py
git commit -a -m "Updates on $(date +%Y%m%d%H%M)"
git push
echo `date`
