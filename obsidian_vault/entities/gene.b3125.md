---
entity_id: "gene.b3125"
entity_type: "gene"
name: "garR"
source_database: "NCBI RefSeq"
source_id: "gene-b3125"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3125"
  - "garR"
---

# garR

`gene.b3125`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3125`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

garR (gene.b3125) is a gene entity. It encodes garR (protein.P0ABQ2). Encoded protein function: FUNCTION: Catalyzes the reduction of tatronate semialdehyde to D-glycerate. {ECO:0000255|HAMAP-Rule:MF_02032, ECO:0000269|PubMed:9772162}. EcoCyc product frame: TSA-REDUCT-MONOMER. EcoCyc synonyms: yhaE. Genomic coordinates: 3271867-3272751. EcoCyc protein note: Tartronate semialdehyde reductase (GarR) catalyzes the reduction of tatronate semialdehyde to yield glycerate . GarR is one of two tartronate semialdehyde reductase isozymes in E. coli. Enzymatic activity of tartronate semialdehyde reductase is induced by growth on D-glucarate, D-galactarate, and D-glycerate .

## Biological Role

Repressed by fur (protein.P0A9A9).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABQ2|protein.P0ABQ2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=garR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010273,ECOCYC:EG11176,GeneID:947631`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3271867-3272751:-; feature_type=gene
