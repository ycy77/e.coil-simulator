---
entity_id: "gene.b1079"
entity_type: "gene"
name: "flgH"
source_database: "NCBI RefSeq"
source_id: "gene-b1079"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1079"
  - "flgH"
---

# flgH

`gene.b1079`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1079`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flgH (gene.b1079) is a gene entity. It encodes flgH (protein.P0A6S0). Encoded protein function: FUNCTION: Assembles around the rod to form the L-ring and probably protects the motor/basal body from shearing forces during rotation. {ECO:0000250}. EcoCyc product frame: FLGH-FLAGELLAR-L-RING. EcoCyc synonyms: flaY. Genomic coordinates: 1135564-1136262. EcoCyc protein note: FlgH is the basic subunit which makes up the L or lipopolysaccharide ring of the flagellar basal body. The L ring lies in the plane of the outer membrane and encircles the basal body rod . FlgH is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). Early studies in E. coli K-12 identified the flaY gene within the region I fla (flagella) genes (see ). Incomplete flagella structures are detected in mutants with defects in flaY . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see .

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6S0|protein.P0A6S0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003654,ECOCYC:G364,GeneID:946996`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1135564-1136262:+; feature_type=gene
