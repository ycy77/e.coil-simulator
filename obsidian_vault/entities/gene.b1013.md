---
entity_id: "gene.b1013"
entity_type: "gene"
name: "rutR"
source_database: "NCBI RefSeq"
source_id: "gene-b1013"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1013"
  - "rutR"
---

# rutR

`gene.b1013`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1013`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rutR (gene.b1013) is a gene entity. It encodes rutR (protein.P0ACU2). Encoded protein function: FUNCTION: Master transcription regulator which represses the degradation of pyrimidines (rutABCDEFG) and purines (gcl operon) for maintenance of metabolic balance between pyrimidines and purines. It also regulates the synthesis of pyrimidine nucleotides and arginine from glutamine (carAB) and the supply of glutamate (gadABWX). {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:17919280}. EcoCyc product frame: PD01352. EcoCyc synonyms: ycdC. Genomic coordinates: 1074242-1074880.

## Biological Role

Repressed by rutR (protein.P0ACU2). Activated by rpoD (protein.P00579), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACU2|protein.P0ACU2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rutR; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rutR; function=+
- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `C` - regulator=RutR; target=rutR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003422,ECOCYC:EG12301,GeneID:945075`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1074242-1074880:+; feature_type=gene
