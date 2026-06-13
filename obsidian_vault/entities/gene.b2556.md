---
entity_id: "gene.b2556"
entity_type: "gene"
name: "glrK"
source_database: "NCBI RefSeq"
source_id: "gene-b2556"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2556"
  - "glrK"
---

# glrK

`gene.b2556`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2556`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glrK (gene.b2556) is a gene entity. It encodes glrK (protein.P52101). Encoded protein function: FUNCTION: Member of the two-component regulatory system GlrR/GlrK that up-regulates transcription of the glmY sRNA when cells enter the stationary growth phase. Activates GlrR by phosphorylation. {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:19843219}. EcoCyc product frame: MONOMER0-4141. EcoCyc synonyms: yfhZ, yfhK, qseE. Genomic coordinates: 2689671-2691098. EcoCyc protein note: This is the phosphorylated form of G7345-MONOMER "GlrK" - the sensor histidine kinase of the GlrKR two-component signal transduction system.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52101|protein.P52101]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=glrK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008409,ECOCYC:G7345,GeneID:947013`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2689671-2691098:-; feature_type=gene
