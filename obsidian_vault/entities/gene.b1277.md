---
entity_id: "gene.b1277"
entity_type: "gene"
name: "ribA"
source_database: "NCBI RefSeq"
source_id: "gene-b1277"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1277"
  - "ribA"
---

# ribA

`gene.b1277`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1277`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ribA (gene.b1277) is a gene entity. It encodes ribA (protein.P0A7I7). Encoded protein function: FUNCTION: Catalyzes the conversion of GTP to 2,5-diamino-6-ribosylamino-4(3H)-pyrimidinone 5'-phosphate (DARP), formate and pyrophosphate. {ECO:0000269|PubMed:235552}. EcoCyc product frame: GTP-CYCLOHYDRO-II-MONOMER. Genomic coordinates: 1338570-1339160.

## Biological Role

Activated by soxS (protein.P0A9E2).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7I7|protein.P0A7I7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=ribA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004285,ECOCYC:EG11331,GeneID:945763`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1338570-1339160:-; feature_type=gene
