---
entity_id: "gene.b0892"
entity_type: "gene"
name: "rarA"
source_database: "NCBI RefSeq"
source_id: "gene-b0892"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0892"
  - "rarA"
---

# rarA

`gene.b0892`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0892`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rarA (gene.b0892) is a gene entity. It encodes rarA (protein.P0AAZ4). Encoded protein function: FUNCTION: DNA-dependent ATPase that plays important roles in cellular responses to stalled DNA replication processes. {ECO:0000269|PubMed:11459952, ECO:0000269|PubMed:15743409, ECO:0000269|PubMed:21297161}. EcoCyc product frame: EG12690-MONOMER. EcoCyc synonyms: ycaJ, mgsA. Genomic coordinates: 937994-939337.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAZ4|protein.P0AAZ4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rarA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003034,ECOCYC:EG12690,GeneID:945505`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:937994-939337:+; feature_type=gene
