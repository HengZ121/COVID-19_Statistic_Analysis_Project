Data Resource: Google Developer


HOW MOBILITY KEY IS CREATE:

 region_code+YYYYMMDD
e.g. mobility information in Toronto on 2020-Feb-01
      120200201

targeted_region = ["Toronto", "Durham", "Halton", "Peel", "York", "Ottawa"]
region_code = ["1","2","3","4","5","6"]

The mobility information was downloaded from Google, and original .csv file couldn't be precisely read by python, thus I have copied its content and pasted in "mobility.txt" in order to better process it using script