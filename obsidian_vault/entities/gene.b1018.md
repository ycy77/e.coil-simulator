---
entity_id: "gene.b1018"
entity_type: "gene"
name: "efeO"
source_database: "NCBI RefSeq"
source_id: "gene-b1018"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1018"
  - "efeO"
---

# efeO

`gene.b1018`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1018`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

efeO (gene.b1018) is a gene entity. It encodes efeO (protein.P0AB24). Encoded protein function: FUNCTION: Involved in Fe(2+) uptake. Could be an iron-binding and/or electron-transfer component. {ECO:0000269|PubMed:19701722}. EcoCyc product frame: G6527-MONOMER. EcoCyc synonyms: ycdO. Genomic coordinates: 1082243-1083370. EcoCyc protein note: EfeO is predicted to be the periplasmic, metal-binding component of a ferrous ion transport system (see ) that is cryptic in E. coli K-12. Analysis of transcriptional efe-lacZ fusions suggest that efeO does not possess a proximal promoter and is co-transcribed with efeU . efeU in E. coli K-12 is disrupted by a frameshift mutation leaving the efeU_1 and efeU_2 fragments nonfunctional; EfeO (and EfeB) are produced despite the frameshift mutation . The functional efeU (ycdN) gene in E. coli Nissle 1917 encodes an oxidase-dependent, OFeT family ferrous iron permease . The efeUOB operon of enterohaemorrhagic E. coli O157:H7, lacks any frameshift and is functional . efeUOB transcription in E. coli K-12 is subject to Fe(II)-Fur control in response to iron . EfeO levels increase under iron restriction and when Fur is inactivated; EfeO levels are independent of iron in a fur mutant . The efeUOB operon is induced at acid pH and subject to CpxAR dependent repression at alkaline pH . Low copy-number expression of a 'corrected' efeUOB operon in an E...

## Biological Role

Repressed by fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB24|protein.P0AB24]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=efeO; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003448,ECOCYC:G6527,GeneID:945603`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1082243-1083370:+; feature_type=gene
