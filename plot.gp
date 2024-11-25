set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set datafile separator ","
plot 'records/1025.KUAKATA.1025.tides.observed.csv' using 1:2 with lines title 'KUAKATA'
replot 'records/1029.DHULASUR.1029.tides.observed.csv' using 1:2 with lines title 'DHULASUR'
replot 'records/1017.GALACHIPA.1017.tides.observed.csv' using 1:2 with lines title 'GALACHIPA'
replot 'records/1040.TEKNAF.1040.river.level.csv' using 1:2 with lines title 'TEKNAF'
replot 'records/1005.PATGATI.1005.tides.observed.csv' using 1:2 with lines title 'PATGATI'
replot 'records/1055.KAZIRHAT.1055.river.level.csv' using 1:2 with lines title 'KAZIRHAT'
replot 'records/1001.NALMURI.1001.tides.observed.csv' using 1:2 with lines title 'NALMURI'
replot 'records/1018.DASMONIA.1018.tides.observed.csv' using 1:2 with lines title 'DASMONIA'
replot 'records/1022.NANDIRBAZAR.1022.tides.observed.csv' using 1:2 with lines title 'NANDIRBAZAR'
replot 'records/1053.BAGHABARI.1053.river.level.csv' using 1:2 with lines title 'BAGHABARI'
replot 'records/1016.KHEPUPARA.1016.tides.observed.csv' using 1:2 with lines title 'KHEPUPARA'
replot 'records/1003.KALIKAPUR.1003.tides.observed.csv' using 1:2 with lines title 'KALIKAPUR'
set yrange [-5:10]
set key below horizontal
