---
entity_id: "gene.b3462"
entity_type: "gene"
name: "ftsX"
source_database: "NCBI RefSeq"
source_id: "gene-b3462"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3462"
  - "ftsX"
---

# ftsX

`gene.b3462`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3462`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsX (gene.b3462) is a gene entity. It encodes ftsX (protein.P0AC30). Encoded protein function: FUNCTION: Part of the ABC transporter FtsEX involved in cellular division. Important for assembly or stability of the septal ring. Encoded in an operon consisting of genes ftsY, ftsE and ftsX. {ECO:0000269|PubMed:10048040, ECO:0000269|PubMed:14729705}. EcoCyc product frame: FTSX-MONOMER. EcoCyc synonyms: ftsS. Genomic coordinates: 3601028-3602086. EcoCyc protein note: FtsE and FtsX localize to the cell division site; localization is dependent on FtsZ, FtsA and ZipA, but not FtsK, FtsQ, FtsL and FtsI . FtsEX is important for assembly or stability of the septal ring under low-salt growth conditions . FtsX contains 4 transmembrane region with the C and N terminus located in the cytoplasm; a large periplasmic loop is located between the first and second transmembrane region . FtsX-GFP localizes to the septal ring in a ftsEX null mutant . FtsS: FtsX: "filamentous temperature sensitive X" Review:

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC30|protein.P0AC30]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011311,ECOCYC:EG10345,GeneID:947969`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3601028-3602086:-; feature_type=gene
