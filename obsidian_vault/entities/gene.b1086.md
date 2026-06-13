---
entity_id: "gene.b1086"
entity_type: "gene"
name: "rluC"
source_database: "NCBI RefSeq"
source_id: "gene-b1086"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1086"
  - "rluC"
---

# rluC

`gene.b1086`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1086`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rluC (gene.b1086) is a gene entity. It encodes rluC (protein.P0AA39). Encoded protein function: FUNCTION: Responsible for synthesis of pseudouridine from uracil at positions 955, 2504 and 2580 in 23S ribosomal RNA. {ECO:0000269|PubMed:9660827}. EcoCyc product frame: EG11118-MONOMER. EcoCyc synonyms: yceC. Genomic coordinates: 1144940-1145899. EcoCyc protein note: RluC catalyzes pseudouridylation of nucleotides U955, U2504, and U2580 in 23S rRNA; all three sites are located near the peptidyl transferase center of the ribosome . RluC also shows activity toward 16S rRNA in vitro . RluC associates with a pre-50S ribosomal particle . A proteolytic fragment consisting of amino acids 89-319 is catalytically active . The crystal structure of the C-terminal catalytic domain has been determined at 2 Å resolution . An rluC mutant lacks pseudouridylation of nucleotides U955, U2504, and U2580 in 23S rRNA, but does not exhibit an obvious growth defect . It was later shown that an rluC mutant shows some cold sensitivity . Insertion mutations in rluC suppress the cold-sensitive growth phenotype of a bipA deletion mutant . Inactivation of rluC leads to increased susceptibility to antibiotics that target the peptidyl transferase center, such as clindamycin, linezolid, and tiamulin...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA39|protein.P0AA39]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003675,ECOCYC:EG11118,GeneID:945637`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1144940-1145899:+; feature_type=gene
