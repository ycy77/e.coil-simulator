---
entity_id: "gene.b3128"
entity_type: "gene"
name: "garD"
source_database: "NCBI RefSeq"
source_id: "gene-b3128"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3128"
  - "garD"
---

# garD

`gene.b3128`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3128`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

garD (gene.b3128) is a gene entity. It encodes garD (protein.P39829). Encoded protein function: FUNCTION: Catalyzes the dehydration of galactarate to form 5-dehydro-4-deoxy-D-glucarate (5-KDG). {ECO:0000255|HAMAP-Rule:MF_02031, ECO:0000269|PubMed:31811683, ECO:0000269|PubMed:9772162}. EcoCyc product frame: GALACTARDEHYDRA-MONOMER. EcoCyc synonyms: yhaG. Genomic coordinates: 3275282-3276853.

## Biological Role

Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39829|protein.P39829]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=garD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010284,ECOCYC:EG12522,GeneID:947641`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3275282-3276853:+; feature_type=gene
