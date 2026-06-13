---
entity_id: "gene.b0465"
entity_type: "gene"
name: "mscK"
source_database: "NCBI RefSeq"
source_id: "gene-b0465"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0465"
  - "mscK"
---

# mscK

`gene.b0465`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0465`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mscK (gene.b0465) is a gene entity. It encodes mscK (protein.P77338). Encoded protein function: FUNCTION: Mechanosensitive channel that opens in response to membrane tension and specific ionic conditions. Requires high concentrations of external K(+), NH(4)(+), Rb(+) or Cs(+) to gate. May participate in the regulation of osmotic pressure changes within the cell, although it does not appear to have a major role in osmolarity regulation. Forms an ion channel of 1.0 nanosiemens conductance. The channel can remain active for between 30 seconds and over 3 minutes; it does not desensitize upon extended pressure. Its activity is masked in wild-type cells by the MscS channel. {ECO:0000269|PubMed:10202137, ECO:0000269|PubMed:11985727, ECO:0000269|PubMed:12374733}. EcoCyc product frame: G6255-MONOMER. EcoCyc synonyms: aefA, kefA. Genomic coordinates: 486536-489898. EcoCyc protein note: MscK is a potassium-dependent, mechanosensitive channel of small conductance. mscK encodes a mechanosensitive channel with similar or slightly lower conductance to the EG11160-MONOMER "MscS" channel of small conductance (0.8 - 1nS) ; MscK does not desensitize upon extended pressure application; ΔmscK cells survive the transition to low osmolarity media as do Δ(mscK mscS) double mutants . E. coli strain RQ2 carrying the kefA2 allele is unable to grow in high (0...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77338|protein.P77338]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001613,ECOCYC:G6255,GeneID:945132`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:486536-489898:+; feature_type=gene
