---
entity_id: "gene.b0854"
entity_type: "gene"
name: "potF"
source_database: "NCBI RefSeq"
source_id: "gene-b0854"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0854"
  - "potF"
---

# potF

`gene.b0854`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0854`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

potF (gene.b0854) is a gene entity. It encodes potF (protein.P31133). Encoded protein function: FUNCTION: Part of the ABC transporter complex PotFGHI involved in putrescine uptake (PubMed:23719730, PubMed:8416922). Binds putrescine (PubMed:8416922, PubMed:9651355). Imports putrescine for maintenance of the optimal concentration of polyamines necessary for cell growth in the presence of glucose (PubMed:23719730). {ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:8416922, ECO:0000269|PubMed:9651355}. EcoCyc product frame: POTF-MONOMER. Genomic coordinates: 893784-894896. EcoCyc protein note: PotF is the periplasmic, putrescine binding protein of an ATP-dependent putrescine uptake system. PotF binds putrescine in a 1:1 ratio; PotF has 35% sequence similarity with POTD-MONOMER PotD - the spermidine preferential binding protein of the PotABCD polyamine uptake system . PotF binds its endogenous ligand, putrescine, with high affinity (Kd=4.8 nM ; Kd=68 nM ). Purified PotF also binds CADAVERINE (Kd=68 nM ) and AGMATHINE (Kd=0.22 µM ), and with less affinity, SPERMIDINE and SPERMINE )...

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0), arcA (protein.P0A9Q1), lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31133|protein.P31133]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=potF; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=potF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002913,ECOCYC:EG11629,GeneID:945480`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:893784-894896:+; feature_type=gene
