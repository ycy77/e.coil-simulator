---
entity_id: "gene.b1326"
entity_type: "gene"
name: "mpaA"
source_database: "NCBI RefSeq"
source_id: "gene-b1326"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1326"
  - "mpaA"
---

# mpaA

`gene.b1326`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1326`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mpaA (gene.b1326) is a gene entity. It encodes mpaA (protein.P0ACV6). Encoded protein function: FUNCTION: Involved in muropeptide degradation. Catalyzes the hydrolysis of the gamma-D-glutamyl-diaminopimelic acid (gamma-D-Glu-Dap) amide bond in the murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelic acid, leading to the formation of L-Ala-gamma-D-Glu and Dap (PubMed:12511517, PubMed:22970852). Has weak activity with L-Ala-gamma-D-Glu-L-Lys, MurNAc-tripeptide and gamma-D-Glu-meso-Dap (PubMed:22970852). Cannot hydrolyze murein tetrapeptide (PubMed:22970852). {ECO:0000269|PubMed:12511517, ECO:0000269|PubMed:22970852}. EcoCyc product frame: G6662-MONOMER. EcoCyc synonyms: ycjI. Genomic coordinates: 1389870-1390598.

## Biological Role

Repressed by pgrR (protein.P77333).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACV6|protein.P0ACV6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77333|protein.P77333]] `RegulonDB` `S` - regulator=PgrR; target=mpaA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004450,ECOCYC:G6662,GeneID:945969`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1389870-1390598:-; feature_type=gene
