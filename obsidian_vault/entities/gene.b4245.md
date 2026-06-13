---
entity_id: "gene.b4245"
entity_type: "gene"
name: "pyrB"
source_database: "NCBI RefSeq"
source_id: "gene-b4245"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4245"
  - "pyrB"
---

# pyrB

`gene.b4245`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4245`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pyrB (gene.b4245) is a gene entity. It encodes pyrB (protein.P0A786). Encoded protein function: FUNCTION: Catalyzes the condensation of carbamoyl phosphate and aspartate to form carbamoyl aspartate and inorganic phosphate, the committed step in the de novo pyrimidine nucleotide biosynthesis pathway. {ECO:0000255|HAMAP-Rule:MF_00001, ECO:0000269|PubMed:13319326}. EcoCyc product frame: ASPCARBCAT-MONOMER. Genomic coordinates: 4471460-4472395.

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A786|protein.P0A786]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=pyrB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013892,ECOCYC:EG10805,GeneID:948767`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4471460-4472395:-; feature_type=gene
