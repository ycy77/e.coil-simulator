---
entity_id: "gene.b4189"
entity_type: "gene"
name: "bsmA"
source_database: "NCBI RefSeq"
source_id: "gene-b4189"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4189"
  - "bsmA"
---

# bsmA

`gene.b4189`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4189`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bsmA (gene.b4189) is a gene entity. It encodes bsmA (protein.P39297). Encoded protein function: FUNCTION: Involved in protection of biofilms against oxidative stress. {ECO:0000269|PubMed:19833773}. EcoCyc product frame: G7852-MONOMER. EcoCyc synonyms: yjfO. Genomic coordinates: 4416441-4416770. EcoCyc protein note: bsmA is upregulated during biofilm growth on serine limited defined medium; a bsmA insertion mutant exhibits reduced microcolony formation in flow cells and greater flagellar motility on soft agar; biofilms from the mutant strain are less able to resist acid and peroxide stress . BsmA is a predicted lipoprotein BsmA: "biofilm stress and motility"

## Biological Role

Activated by yciT (protein.P76034).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39297|protein.P39297]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P76034|protein.P76034]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013706,ECOCYC:G7852,GeneID:948708`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4416441-4416770:-; feature_type=gene
