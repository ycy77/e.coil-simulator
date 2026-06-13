---
entity_id: "gene.b0522"
entity_type: "gene"
name: "purK"
source_database: "NCBI RefSeq"
source_id: "gene-b0522"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0522"
  - "purK"
---

# purK

`gene.b0522`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0522`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purK (gene.b0522) is a gene entity. It encodes purK (protein.P09029). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent conversion of 5-aminoimidazole ribonucleotide (AIR) and HCO(3)(-) to N5-carboxyaminoimidazole ribonucleotide (N5-CAIR). {ECO:0000255|HAMAP-Rule:MF_01928, ECO:0000269|PubMed:8117684}. EcoCyc product frame: PURK-MONOMER. EcoCyc synonyms: purE2. Genomic coordinates: 551527-552594.

## Biological Role

Repressed by purR (protein.P0ACP7). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09029|protein.P09029]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=purK; function=+
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=purK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001794,ECOCYC:EG10796,GeneID:945153`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:551527-552594:-; feature_type=gene
