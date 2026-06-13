---
entity_id: "gene.b0720"
entity_type: "gene"
name: "gltA"
source_database: "NCBI RefSeq"
source_id: "gene-b0720"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0720"
  - "gltA"
---

# gltA

`gene.b0720`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0720`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltA (gene.b0720) is a gene entity. It encodes gltA (protein.P0ABH7). Encoded protein function: Citrate synthase (EC 2.3.3.16) EcoCyc product frame: CITSYN-MONOMER. EcoCyc synonyms: gluT, icdB. Genomic coordinates: 753185-754468.

## Biological Role

Repressed by arcA (protein.P0A9Q1), nac (protein.Q47005). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABH7|protein.P0ABH7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gltA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=gltA; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=gltA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=gltA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002451,ECOCYC:EG10402,GeneID:945323`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:753185-754468:-; feature_type=gene
