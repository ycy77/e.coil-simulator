---
entity_id: "gene.b2987"
entity_type: "gene"
name: "pitB"
source_database: "NCBI RefSeq"
source_id: "gene-b2987"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2987"
  - "pitB"
---

# pitB

`gene.b2987`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2987`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pitB (gene.b2987) is a gene entity. It encodes pitB (protein.P43676). Encoded protein function: FUNCTION: Low-affinity inorganic phosphate transporter. {ECO:0000269|PubMed:11489853}. EcoCyc product frame: PITB-MONOMER. Genomic coordinates: 3134872-3136371. EcoCyc protein note: Early work in E. coli indicated that there are two genetically separable transport systems for inorganic phosphate (Pi) - a high affinity, low velocity Pst (phosphate specific transport) system (the ABC-27-CPLX) and a low affinity, high velocity Pit (Pi transport) system *. This latter system is constitutive in nature and catalyses an electrogenic metal phosphate:H+ symport . Pi uptake via Pit is dependent on the presence of divalent cations, like Mg2+, Ca2+, Co2+, or Mn2+, which form soluble metal phosphate (MeHP04) complexes . The Pit system in E. coli K-12 consists of two transporters - PitA and PitB - which have 81% sequence identity at the protein level; pitA is likely constitutive while pitB is repressed or inactivated through the pho regulon; chromosomally encoded PitB catalyses Pi uptake in a phoB-phoR deleted strain; both proteins may have contributed to the kinetic values and substrate specificities determined in earlier studies . The Pit proteins are predicted to contain 10 transmembrane helices . The Pit system also transports the phosphate analogue, arsenate...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P43676|protein.P43676]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=pitB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009800,ECOCYC:EG12883,GeneID:947475`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3134872-3136371:-; feature_type=gene
