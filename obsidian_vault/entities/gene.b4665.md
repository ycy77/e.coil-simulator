---
entity_id: "gene.b4665"
entity_type: "gene"
name: "ibsC"
source_database: "NCBI RefSeq"
source_id: "gene-b4665"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4665"
  - "ibsC"
---

# ibsC

`gene.b4665`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4665`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ibsC (gene.b4665) is a gene entity. It encodes ibsC (protein.C1P615). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. Overexpression causes cessation of growth and rapid membrane depolarization. Overexpression induces stress-response, the psp phage shock and a number of membrane protein genes. {ECO:0000269|PubMed:18710431}. EcoCyc product frame: MONOMER0-2857. Genomic coordinates: 3056890-3056949. EcoCyc protein note: The small open reading frame G0-10631 was detected by similarity to the open reading frames encoded on the opposite strand of the sib small RNAs . Overexpression of an antisense-SibC (i.e. sense-IbsC) RNA suppresses cell growth, which can be attributed to the production of the toxic peptide IbsC . Overexpression of IbsC is toxic to the cell by disrupting membrane integrity. Whole-genome gene expression analysis after induction of IbsC expression shows changes in expression of many stress response and membrane proteins . The G0-10631 mRNA was one of over two hundred RNAs that were found to bind the aminoglycoside antibiotic CPD-4822 . IbsC is predicted to be a bitopic inner membrane protein . IbsC: "induction brings stasis"

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.C1P615|protein.C1P615]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ibsC; function=+

## External IDs

- `Dbxref:ECOCYC:G0-10631,GeneID:7751627`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3056890-3056949:-; feature_type=gene
