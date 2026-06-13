---
entity_id: "gene.b1080"
entity_type: "gene"
name: "flgI"
source_database: "NCBI RefSeq"
source_id: "gene-b1080"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1080"
  - "flgI"
---

# flgI

`gene.b1080`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1080`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flgI (gene.b1080) is a gene entity. It encodes flgI (protein.P0A6S3). Encoded protein function: FUNCTION: Assembles around the rod to form the L-ring and probably protects the motor/basal body from shearing forces during rotation. EcoCyc product frame: FLGI-FLAGELLAR-P-RING. EcoCyc synonyms: flaM. Genomic coordinates: 1136274-1137371. EcoCyc protein note: FlgI is the structural component of the P (peptidoglycan ring) of the flagellar basal body . FlgI and FlgH (the structural component of the L ring) form the L-P ring complex which assembles around the rod and is thought to act as the molecular bushing that supports flagellar motor rotation (see ). Our knowledge on FlgI in E. coli is based, in part, on characterization of the homologous protein in Salmonella typhimurium (see ); the two proteins are 92% identical over their entire length. E. coli FlgI contains an intramolecular disulfide bond; the presence of this bond does not appear to be necessary for P-ring formation but has been implicated in preventing degradation of the protein in the periplasmic space . Cross-linking experiments suggest that FlgI may interact with the stator protein MotB . Early studies in E. coli K-12 identified the flaM gene within the region I fla (flagella) genes (see ). Incomplete flagella structures are detected in mutants with defects in flaM . flaM mutants are non-motile (see also )...

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6S3|protein.P0A6S3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003656,ECOCYC:G365,GeneID:947534`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1136274-1137371:+; feature_type=gene
