## codypy
#### Useful toolkit in Python3
-----
##### Setup
Install required packages  
>`pip install -r requirements.txt`
-----
##### `utilityfunctions.py`
* Contains general functions for reading, shaping, and simple data manipulations

##### `bed_to_csv.py`
* Converts a _.bed_ file that defines an amplicon sequencing panel to a mutable _.csv_ file  
 * _.bed_ format is described by the [UCSC Genome Browser](https://genome.ucsc.edu/FAQ/FAQformat.html#format1)  
 More information can be found at the [Ensembl](https://www.ensembl.org/info/website/upload/bed.html?redirect=no) or [IGV](https://software.broadinstitute.org/software/igv/BED) websites.

##### `hamming.py`
* Calculate hamming distances of strings.  
Useful for sequence diversity comparisons.
