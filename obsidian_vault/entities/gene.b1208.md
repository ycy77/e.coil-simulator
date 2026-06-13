---
entity_id: "gene.b1208"
entity_type: "gene"
name: "ispE"
source_database: "NCBI RefSeq"
source_id: "gene-b1208"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1208"
  - "ispE"
---

# ispE

`gene.b1208`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1208`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ispE (gene.b1208) is a gene entity. It encodes ispE (protein.P62615). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of the position 2 hydroxy group of 4-diphosphocytidyl-2C-methyl-D-erythritol (PubMed:10570138, PubMed:10655484, Ref.6). Phosphorylates isopentenyl phosphate at low rates. Also acts on isopentenol, and, much less efficiently, dimethylallyl alcohol. Dimethylallyl monophosphate does not serve as a substrate (PubMed:10570138). {ECO:0000269|PubMed:10570138, ECO:0000269|PubMed:10655484, ECO:0000269|Ref.6}. EcoCyc product frame: EG11294-MONOMER. EcoCyc synonyms: ipk, ychB. Genomic coordinates: 1262026-1262877.

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P62615|protein.P62615]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004056,ECOCYC:EG11294,GeneID:945774`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1262026-1262877:-; feature_type=gene
