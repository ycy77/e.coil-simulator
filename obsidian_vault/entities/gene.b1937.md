---
entity_id: "gene.b1937"
entity_type: "gene"
name: "fliE"
source_database: "NCBI RefSeq"
source_id: "gene-b1937"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1937"
  - "fliE"
---

# fliE

`gene.b1937`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1937`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliE (gene.b1937) is a gene entity. It encodes fliE (protein.P0A8T5). Encoded protein function: Flagellar hook-basal body complex protein FliE EcoCyc product frame: EG11346-MONOMER. EcoCyc synonyms: fla, flaAI, flaN. Genomic coordinates: 2012700-2013014. EcoCyc protein note: fliE is predicted to encode a structural protein of the flagellum hook-basal body complex. fliE constitutes a monocistronic operon in both E. coli K-12 and Salmonella typhimurium and the proteins are 82% identical (see also ). In Salmonella typhimurium, FliE is a component of the hook-basal body complex; it may act as a structural adaptor between the MS ring and the rod . Insertional inactivation of fliE in Salmonella typhimurium results in mutants that are unable to secrete flagellin (FliC) or assemble flagella . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see .

## Biological Role

Repressed by csgD (protein.P52106). Activated by FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8T5|protein.P0A8T5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=fliE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006447,ECOCYC:EG11346,GeneID:946446`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2012700-2013014:-; feature_type=gene
