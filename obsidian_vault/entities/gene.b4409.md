---
entity_id: "gene.b4409"
entity_type: "gene"
name: "blr"
source_database: "NCBI RefSeq"
source_id: "gene-b4409"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4409"
  - "blr"
---

# blr

`gene.b4409`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4409`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

blr (gene.b4409) is a gene entity. It encodes blr (protein.P56976). Encoded protein function: FUNCTION: Component of the cell division machinery, which is probably involved in the stabilization of the divisome under certain stress conditions. {ECO:0000269|PubMed:22885295}. EcoCyc product frame: MONOMER0-1561. Genomic coordinates: 1704551-1704676. EcoCyc protein note: Blr is a small membrane protein that appears to be involved in stabilization of the divisome under certain stress conditions and in resistance to a number of antibiotics which inhibit peptidoglycan synthesis . Blr does not affect beta-lactamase activity; resistance may be due to enhancement of drug exit from the cell or to prevention of drug entry into the cell. Blr is predicted to have a single transmembrane segment; the C-terminus is located in the periplasm . Blr interacts with FtsL as well as other cell division proteins, including FtsI, FtsK, FtsN, FtsQ, FtsW, and YmgF. Its localization to the cell division site is dependent on FtsQ and FtsN . A strain with a TnphoA insertion in blr has increased susceptibility to beta-lactam antibiotics, D-cycloserine, and bacitracin . In growth competition experiments, a blr deletion mutant is more resistant to cell envelope stress than the wild type . These phenotypes were not observed by...

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P56976|protein.P56976]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=blr; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047212,ECOCYC:G0-9561,GeneID:2847682`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1704551-1704676:+; feature_type=gene
