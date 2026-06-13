---
entity_id: "gene.b3821"
entity_type: "gene"
name: "pldA"
source_database: "NCBI RefSeq"
source_id: "gene-b3821"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3821"
  - "pldA"
---

# pldA

`gene.b3821`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3821`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pldA (gene.b3821) is a gene entity. It encodes pldA (protein.P0A921). Encoded protein function: FUNCTION: Has broad substrate specificity including hydrolysis of phosphatidylcholine with phospholipase A2 (EC 3.1.1.4) and phospholipase A1 (EC 3.1.1.32) activities. Strong expression leads to outer membrane breakdown and cell death; is dormant in normal growing cells. Required for efficient secretion of bacteriocins. EcoCyc product frame: MONOMER0-341. Genomic coordinates: 4004862-4005731.

## Biological Role

Repressed by nac (protein.Q47005). Activated by arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00565` Ether lipid metabolism (KEGG)
- `eco00592` alpha-Linolenic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A921|protein.P0A921]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=pldA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=pldA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012479,ECOCYC:EG10738,GeneID:948307`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4004862-4005731:+; feature_type=gene
