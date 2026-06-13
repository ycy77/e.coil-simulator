---
entity_id: "gene.b1083"
entity_type: "gene"
name: "flgL"
source_database: "NCBI RefSeq"
source_id: "gene-b1083"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1083"
  - "flgL"
---

# flgL

`gene.b1083`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1083`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flgL (gene.b1083) is a gene entity. It encodes flgL (protein.P29744). Encoded protein function: Flagellar hook-associated protein 3 (HAP3) (Hook-filament junction protein) EcoCyc product frame: EG11545-MONOMER. EcoCyc synonyms: flaT. Genomic coordinates: 1140033-1140986. EcoCyc protein note: Experiments in Salmonella typhimurium using antibodies against the flagellar proteins FlgK and FlgL identify them as junction proteins which connect the filament to the hook . Early studies in E. coli K-12 identified the flaT gene within the region I fla (flagella) genes (see ). For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see .

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P29744|protein.P29744]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=flgL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003666,ECOCYC:EG11545,GeneID:945646`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1140033-1140986:+; feature_type=gene
