---
entity_id: "gene.b2921"
entity_type: "gene"
name: "srsR"
source_database: "NCBI RefSeq"
source_id: "gene-b2921"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2921"
  - "srsR"
---

# srsR

`gene.b2921`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2921`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

srsR (gene.b2921) is a gene entity. It encodes ygfI (protein.P52044). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YgfI EcoCyc product frame: G7518-MONOMER. EcoCyc synonyms: ygfI. Genomic coordinates: 3066277-3067173. EcoCyc protein note: YgfI is a LysR-type transcription factor involved in regulation of formate, glycerol, dihydroxyacetone, and fucose utilization, hydrogen peroxide resistance, biofilm formation, antibiotic resistance, and stationary phase . The transcription of the srsR gene increases during transition to stationary phase for growth in LB medium, reaching levels in stationary phase 25 times higher than those of the exponential phase . YgfI was also found transcriptionally up-regulated in the presence of threonine (Thr) in M9 medium . Genome-wide YgfI binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium and in vitro by genomic systematic evolution of ligands using exponential enrichment (gSELEX-chip) . A total of 10 YgfI binding regions were identified by gSELEX-chip, some of them flanking operons, giving rise to an estimated of 30 putative regulated genes; the transcriptional regulation in vivo of various genes was confirmed by RT-qPCR...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52044|protein.P52044]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=srsR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009585,ECOCYC:G7518,GeneID:947401`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3066277-3067173:-; feature_type=gene
