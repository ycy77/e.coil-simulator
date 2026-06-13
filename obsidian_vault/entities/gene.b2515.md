---
entity_id: "gene.b2515"
entity_type: "gene"
name: "ispG"
source_database: "NCBI RefSeq"
source_id: "gene-b2515"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2515"
  - "ispG"
---

# ispG

`gene.b2515`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2515`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ispG (gene.b2515) is a gene entity. It encodes ispG (protein.P62620). Encoded protein function: FUNCTION: Converts 2C-methyl-D-erythritol 2,4-cyclodiphosphate (ME-2,4cPP) into 1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate, using flavodoxin as the reducing agent. {ECO:0000255|HAMAP-Rule:MF_00159, ECO:0000269|PubMed:15978585, ECO:0000269|PubMed:16268586}. EcoCyc product frame: EG10370-MONOMER. EcoCyc synonyms: gcpE. Genomic coordinates: 2640686-2641804. EcoCyc protein note: 1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate synthase (IspG) catalyzes the sixth step of the mevalonate-independent NONMEVIPP-PWY methylerythritol phosphate (MEP) pathway, the conversion of 2C-methyl-D-erythritol 2,4-cyclodiphosphate into 1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate . IspG activity depends on additional proteins, most likely involved in the oxidation portion of the reaction . IspG contains a [4Fe-4S] cluster that is required for its activity . Mutations in cysteine residues responsible for Fe-S cluster coordination abolish IspG's enzymatic activity . In vitro, CPLX0-7617 ErpA can transfer a [4Fe-4S] cluster to apo-IspG . Increased IspG activity was observed under new assay conditions . Flux through the entire MEP pathway was shown to depend on the presence of FLAVODOXIN1-MONOMER, which may supply reducing equivalents necessary to reduce the Fe-S cluster and yield an active enzyme...

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P62620|protein.P62620]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008281,ECOCYC:EG10370,GeneID:946991`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2640686-2641804:-; feature_type=gene
