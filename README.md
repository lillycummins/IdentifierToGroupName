# identifier_to_group_name

A Python3 script that replaces identifier numbers with the corresponding group name as the sequence descriptions of a `pan_genome_reference.fa` output file from [Panaroo](https://gtonkinhill.github.io/panaroo/#/) (only applicable to Panaroo versions prior to v1.1.2 when this issue was resolved in an update).


### Required input files

This script requires the `pan_genome_reference.fa`, `gene_presence_absence.csv` and `gene_data.csv` files that are output from [Panaroo](https://gtonkinhill.github.io/panaroo/#/).


### Usage

`identifier_to_group_name.py -i pan_genome_ref.fa -m gene_presence_absence.csv -g gene_data.csv -o output`


```python

```
