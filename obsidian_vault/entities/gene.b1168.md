---
entity_id: "gene.b1168"
entity_type: "gene"
name: "pdeG"
source_database: "NCBI RefSeq"
source_id: "gene-b1168"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1168"
  - "pdeG"
---

# pdeG

`gene.b1168`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1168`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdeG (gene.b1168) is a gene entity. It encodes pdeG (protein.P75995). Encoded protein function: FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}. EcoCyc product frame: G6608-MONOMER. EcoCyc synonyms: ycgG. Genomic coordinates: 1217328-1218851. EcoCyc protein note: PdeG is a predicted c-di-GMP phosphodiesterase. PdeG is predicted to contain two transmembrane domains which flank a periplasmic CSS domain containing two highly conserved cysteines, followed by a cytoplasmic C-terminal EAL domain with predicted phosphodiesterase activity . PdeG consistently copurifies with the degradosome . PdeG is one of 5 CSS domain containing c-di-GMP phosphodiesterases in E. coli K-12; redox control and proteolysis of these enzymes is believed to modulate their activity and affect matrix production in biofilm (see ). No expression of pdeG was seen during growth in LB . PdeG is present at very low levels in wild-type cells grown in tryptone broth at 37 °C and is absent in ΔpdeH cells . PdeG: "phosphodiesterase G"

## Biological Role

Repressed by hns (protein.P0ACF8), glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75995|protein.P75995]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=pdeG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003918,ECOCYC:G6608,GeneID:945738`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1217328-1218851:+; feature_type=gene
