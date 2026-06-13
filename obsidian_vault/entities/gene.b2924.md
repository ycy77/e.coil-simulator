---
entity_id: "gene.b2924"
entity_type: "gene"
name: "mscS"
source_database: "NCBI RefSeq"
source_id: "gene-b2924"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2924"
  - "mscS"
---

# mscS

`gene.b2924`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2924`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mscS (gene.b2924) is a gene entity. It encodes mscS (protein.P0C0S1). Encoded protein function: FUNCTION: Mechanosensitive channel that participates in the regulation of osmotic pressure changes within the cell, opening in response to stretch forces in the membrane lipid bilayer, without the need for other proteins. Contributes to normal resistance to hypoosmotic shock. Forms an ion channel of 1.0 nanosiemens conductance with a slight preference for anions. The channel is sensitive to voltage; as the membrane is depolarized, less tension is required to open the channel and vice versa. The channel is characterized by short bursts of activity that last for a few seconds. {ECO:0000269|PubMed:10202137, ECO:0000269|PubMed:12015316, ECO:0000269|PubMed:12080120, ECO:0000269|PubMed:12446901, ECO:0000269|PubMed:12551944, ECO:0000269|PubMed:12767977, ECO:0000269|PubMed:23012406, ECO:0000269|PubMed:23074248, ECO:0000269|PubMed:2436228, ECO:0000269|PubMed:26551077, ECO:0000269|PubMed:7595939}. EcoCyc product frame: EG11160-MONOMER. EcoCyc synonyms: yggB. Genomic coordinates: 3068947-3069807. EcoCyc protein note: MscS is a mechanosensitive channel of small conductance; MscS conductance is 0.8-1 nanosiemens in E. coli giant protoplasts . MscS activity is adaptive, that is, it declines in response to sustained stimulation...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C0S1|protein.P0C0S1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009595,ECOCYC:EG11160,GeneID:947416`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3068947-3069807:-; feature_type=gene
