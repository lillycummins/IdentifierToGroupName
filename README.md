{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cccdc47f",
   "metadata": {},
   "source": [
    "# identifier_to_group_name\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0aa0903c",
   "metadata": {},
   "source": [
    "A Python3 script that replaces identifier numbers with the corresponding group name in the sequence descriptions of a `pan_genome_reference.fa` output file from [Panaroo](https://gtonkinhill.github.io/panaroo/#/) (versions prior to v1.1.2 when this issue was fixed within Panaroo).\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "34367f93",
   "metadata": {},
   "source": [
    "### Required input files\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "387a1cdc",
   "metadata": {},
   "source": [
    "Script takes the `pan_genome_reference.fa`, `gene_presence_absence.csv` and `gene_data.csv` Panaroo output files.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "855f74f1",
   "metadata": {},
   "source": [
    "### Usage\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2f4add02",
   "metadata": {},
   "source": [
    "`identifier_to_group_name.py -i pan_genome_ref.fa -m gene_presence_absence.csv -g gene_data.csv -o output`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "146c99ad",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
