---
entity_id: "gene.b2153"
entity_type: "gene"
name: "folE"
source_database: "NCBI RefSeq"
source_id: "gene-b2153"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2153"
  - "folE"
---

# folE

`gene.b2153`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2153`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

folE (gene.b2153) is a gene entity. It encodes folE (protein.P0A6T5). Encoded protein function: GTP cyclohydrolase 1 (EC 3.5.4.16) (GTP cyclohydrolase I) (GTP-CH-I) EcoCyc product frame: GTP-CYCLOHYDRO-I-MONOMER. Genomic coordinates: 2242984-2243652.

## Biological Role

Repressed by sgrS (gene.b4577), metJ (protein.P0A8U6), arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6T5|protein.P0A6T5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[gene.b4577|gene.b4577]] `RegulonDB` `S` - regulator=SgrS; target=folE; function=-
- `represses` <-- [[protein.P0A8U6|protein.P0A8U6]] `RegulonDB` `S` - regulator=MetJ; target=folE; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=folE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007117,ECOCYC:EG11375,GeneID:949040`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2242984-2243652:-; feature_type=gene
