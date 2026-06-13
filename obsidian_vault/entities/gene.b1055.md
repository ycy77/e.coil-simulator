---
entity_id: "gene.b1055"
entity_type: "gene"
name: "trhO"
source_database: "NCBI RefSeq"
source_id: "gene-b1055"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1055"
  - "trhO"
---

# trhO

`gene.b1055`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1055`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trhO (gene.b1055) is a gene entity. It encodes trhO (protein.P24188). Encoded protein function: FUNCTION: Catalyzes oxygen-dependent 5-hydroxyuridine (ho5U) modification at position 34 in tRNAs, the first step in 5-carboxymethoxyuridine (cmo5U) biosynthesis (PubMed:31253794). May be part of an alternate pathway, which is able to bypass cmo5U biogenesis in a subset of tRNAs under aerobic conditions (PubMed:31253794). {ECO:0000269|PubMed:31253794}. EcoCyc product frame: EG11116-MONOMER. EcoCyc synonyms: yceA. Genomic coordinates: 1116807-1117859. EcoCyc protein note: TrhP is involved in the formation of the cmo5U34 modification on tRNAs during anaerobic growth conditions, while TrhO-mediated formation of ho5U34 utilizes molecular oxygen as the oxygen atom donor . A ΔtrhP trhO double mutant has lost all modification of the U34 wobble base of tRNAVal1 and grows more slowly than wild type. Additional knockout of EG30094 serU, EG30104 thrW or EG30066 proK, which encode tRNAs responsible for decoding G-ending codons, results in further reduction of growth . Mutagenesis of the predicted active site residues C200, T201, G203, and R205, and residues K112 and R114 predicted to be involved in substrate binding of TrhO results in loss of activity in the mutant strain . TrhO: "tRNA hydroxylation O"

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24188|protein.P24188]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003581,ECOCYC:EG11116,GeneID:945601`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1116807-1117859:+; feature_type=gene
