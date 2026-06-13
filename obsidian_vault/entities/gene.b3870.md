---
entity_id: "gene.b3870"
entity_type: "gene"
name: "glnA"
source_database: "NCBI RefSeq"
source_id: "gene-b3870"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3870"
  - "glnA"
---

# glnA

`gene.b3870`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3870`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glnA (gene.b3870) is a gene entity. It encodes glnA (protein.P0A9C5). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent biosynthesis of glutamine from glutamate and ammonia. {ECO:0000250|UniProtKB:P0A1P6}. EcoCyc product frame: ADENYLYL-GS. Genomic coordinates: 4056625-4058034.

## Biological Role

Repressed by glnG (protein.P0AFB8). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), lrp (protein.P0ACJ0), glnG (protein.P0AFB8), zraR (protein.P14375), rpoN (protein.P24255).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9C5|protein.P0A9C5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=glnA; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=glnA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `C` - regulator=NtrC; target=glnA; function=-+
- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=glnA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=glnA; function=+
- `represses` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `C` - regulator=NtrC; target=glnA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0012640,ECOCYC:EG10383,GeneID:948370`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4056625-4058034:-; feature_type=gene
