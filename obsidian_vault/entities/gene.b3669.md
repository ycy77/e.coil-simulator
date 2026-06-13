---
entity_id: "gene.b3669"
entity_type: "gene"
name: "uhpA"
source_database: "NCBI RefSeq"
source_id: "gene-b3669"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3669"
  - "uhpA"
---

# uhpA

`gene.b3669`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3669`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uhpA (gene.b3669) is a gene entity. It encodes uhpA (protein.P0AGA6). Encoded protein function: FUNCTION: Part of the UhpABC signaling cascade that controls the expression of the hexose phosphate transporter UhpT. Activates the transcription of the uhpT gene. Acts by binding specifically to the uhpT promoter region. {ECO:0000269|PubMed:3038843, ECO:0000269|PubMed:8999880}. EcoCyc product frame: PHOSPHO-UHPA. Genomic coordinates: 3850136-3850726.

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGA6|protein.P0AGA6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=uhpA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011995,ECOCYC:EG11051,GeneID:948178`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3850136-3850726:-; feature_type=gene
