---
entity_id: "gene.b0196"
entity_type: "gene"
name: "rcsF"
source_database: "NCBI RefSeq"
source_id: "gene-b0196"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0196"
  - "rcsF"
---

# rcsF

`gene.b0196`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0196`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rcsF (gene.b0196) is a gene entity. It encodes rcsF (protein.P69411). Encoded protein function: FUNCTION: Essential component of the Rcs signaling system, which controls transcription of numerous genes. Plays a role in signal transduction from the cell surface to the histidine kinase RcsC. May detect outer membrane defects. The system controls expression of genes involved in colanic acid capsule synthesis, biofilm formation and cell division. {ECO:0000255|HAMAP-Rule:MF_00976, ECO:0000269|PubMed:13129944, ECO:0000269|PubMed:14651646, ECO:0000269|PubMed:16166540, ECO:0000269|PubMed:16740933}. EcoCyc product frame: RCSF-MONOMER. Genomic coordinates: 219591-219995. EcoCyc protein note: RcsF is a surface exposed outer membrane lipoprotein which detects perturbations or defects in the cell envelope and activates the PWY0-1493 "Rcs signal transduction system". RcsF contains a lipidated N-terminal Cys, a proline rich linker domain and a C-terminal periplasmic domain ; RcsF is a surface exposed lipoprotein; experimental topology analysis suggests RcsF is a transmembrane protein with the lipidated N terminus and the linker domain surface exposed and the core domain in the periplasm...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69411|protein.P69411]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000663,ECOCYC:EG11502,GeneID:949113`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:219591-219995:-; feature_type=gene
