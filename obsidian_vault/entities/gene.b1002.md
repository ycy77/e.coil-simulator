---
entity_id: "gene.b1002"
entity_type: "gene"
name: "agp"
source_database: "NCBI RefSeq"
source_id: "gene-b1002"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1002"
  - "agp"
---

# agp

`gene.b1002`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1002`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

agp (gene.b1002) is a gene entity. It encodes agp (protein.P19926). Encoded protein function: FUNCTION: Absolutely required for the growth of E.coli in a high-phosphate medium containing G-1-P as the sole carbon source. EcoCyc product frame: GLUCOSE-1-PHOSPHAT-MONOMER. Genomic coordinates: 1065585-1066826.

## Biological Role

Repressed by phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19926|protein.P19926]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB|EcoCyc` `S` - regulator=PhoB; target=agp; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003388,ECOCYC:EG10033,GeneID:945773`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1065585-1066826:+; feature_type=gene
