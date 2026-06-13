---
entity_id: "gene.b4232"
entity_type: "gene"
name: "fbp"
source_database: "NCBI RefSeq"
source_id: "gene-b4232"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4232"
  - "fbp"
---

# fbp

`gene.b4232`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4232`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fbp (gene.b4232) is a gene entity. It encodes fbp (protein.P0A993). Encoded protein function: Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) EcoCyc product frame: F16B-MONOMER. EcoCyc synonyms: fdp. Genomic coordinates: 4454611-4455609.

## Biological Role

Activated by DNA-binding transcriptional dual regulator Cra (complex.ecocyc.PC00061), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A993|protein.P0A993]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.PC00061|complex.ecocyc.PC00061]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=fbp; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013842,ECOCYC:EG10283,GeneID:948753`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4454611-4455609:-; feature_type=gene
