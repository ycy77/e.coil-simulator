---
entity_id: "gene.b1075"
entity_type: "gene"
name: "flgD"
source_database: "NCBI RefSeq"
source_id: "gene-b1075"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1075"
  - "flgD"
---

# flgD

`gene.b1075`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1075`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flgD (gene.b1075) is a gene entity. It encodes flgD (protein.P75936). Encoded protein function: FUNCTION: Required for flagellar hook formation. May act as a scaffolding protein. EcoCyc product frame: G360-MONOMER. EcoCyc synonyms: flaV. Genomic coordinates: 1131854-1132549. EcoCyc protein note: Experiments using antibodies raised against the flagellar protein FlgD of Salmonella typhimurium have identified FlgD as a scaffold where assembly of hook proteins takes place. Immunoelectron microscopy shows that once the rod is completed, FlgD is added to its end, allowing assembly of hook proteins. Transport of FlgD occurs via the type III flagellar export apparatus. Once the hook is formed, the hook-filament junction proteins FlgK are added to the end and FlgD dissociates . Early studies in E. coli K-12 identified the flaV gene within the region I fla (flagella) genes (see ). Incomplete flagella structures are detected in mutants with defects in flaV . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see .

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75936|protein.P75936]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003645,ECOCYC:G360,GeneID:945813`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1131854-1132549:+; feature_type=gene
