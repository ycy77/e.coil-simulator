---
entity_id: "gene.b1019"
entity_type: "gene"
name: "efeB"
source_database: "NCBI RefSeq"
source_id: "gene-b1019"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1019"
  - "efeB"
---

# efeB

`gene.b1019`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1019`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

efeB (gene.b1019) is a gene entity. It encodes efeB (protein.P31545). Encoded protein function: FUNCTION: Involved in the recovery of exogenous heme iron. Extracts iron from heme while preserving the protoporphyrin ring intact. Also displays peroxidase activity on guaiacol in vitro. {ECO:0000269|PubMed:16551627, ECO:0000269|PubMed:19564607}. EcoCyc product frame: EG11735-MONOMER. EcoCyc synonyms: ycdB. Genomic coordinates: 1083376-1084647. EcoCyc protein note: efeB is predicted to encode a periplasmic component of a ferrous iron transport system (see ) that is cryptic in E. coli K-12; EfeB is implicated in exogenous heme iron acquisition. Analysis of transcriptional efe-lacZ fusions suggest that efeB does not possess a proximal promoter and is co-transcribed with efeUO . efeU in E. coli K-12 is disrupted by a frameshift mutation leaving the efeU_1 and efeU_2 fragments nonfunctional; EfeB (and EfeO) are produced despite the frameshift mutation . The functional efeU (ycdN) gene in E. coli Nissle 1917 encodes an oxidase-dependent, OFeT family ferrous iron permease . The efeUOB operon of enterohaemorrhagic E. coli O157:H7 lacks any frameshift and is functional . EfeB has been implicated in exogenous heme iron acquisition. Due to the lack of an outer membrane receptor for heme, E. coli K-12 is unable to utilize heme as a source of iron...

## Biological Role

Repressed by fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31545|protein.P31545]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=efeB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003451,ECOCYC:EG11735,GeneID:946500`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1083376-1084647:+; feature_type=gene
