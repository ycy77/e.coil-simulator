---
entity_id: "gene.b3257"
entity_type: "gene"
name: "yhdT"
source_database: "NCBI RefSeq"
source_id: "gene-b3257"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3257"
  - "yhdT"
---

# yhdT

`gene.b3257`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3257`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhdT (gene.b3257) is a gene entity. It encodes yhdT (protein.P45566). Encoded protein function: Uncharacterized membrane protein YhdT EcoCyc product frame: G7693-MONOMER. Genomic coordinates: 3407375-3407617. EcoCyc protein note: The expression of yhdT is repressed in the presence of 10 μM cystine .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45566|protein.P45566]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yhdT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010690,ECOCYC:G7693,GeneID:947762`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3407375-3407617:+; feature_type=gene
