---
entity_id: "gene.b1608"
entity_type: "gene"
name: "rstA"
source_database: "NCBI RefSeq"
source_id: "gene-b1608"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1608"
  - "rstA"
---

# rstA

`gene.b1608`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1608`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rstA (gene.b1608) is a gene entity. It encodes rstA (protein.P52108). Encoded protein function: FUNCTION: Member of the two-component regulatory system RstB/RstA. EcoCyc product frame: PHOSPHO-RSTA. EcoCyc synonyms: urpT. Genomic coordinates: 1682159-1682878. EcoCyc protein note: RstA appears to control genes involved in different biological processes, such as acid tolerance, curli fimbria formation, and anaerobic respiration, among others . Some phenotypes caused by RstA have been identified by mutational analysis. For example, RstA is a suppressor of a lesion in yjeE, a gene essential for cell growth and whose cellular function is unknown . RstA overproduction causes drug resistance . RstA belongs to the two-component system RstA/RstB . Both genes, rstA, encoding the response regulator, and rstB, encoding the sensor kinase, are transcribed together in an operon that is induced under low-Mg2+ growth conditions through the PhoP/PhoQ two-component system . rstA expression is reduced in a phoP phoQ double mutant and in phoP phoQ pmrA and phoP phoQ pmrB triple mutants . The autophosphorylation of RstB appears to be stimulated by low pH . Subsequently, the phosphate group is transferred from RstB to RstA to activate it . A 14-bp DNA sequence that contains the TACA direct repeat has been identified as the RstA DNA-binding site and is called the RstA box...

## Biological Role

Activated by arcA (protein.P0A9Q1), phoP (protein.P23836).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52108|protein.P52108]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=rstA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=rstA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005370,ECOCYC:G6864,GeneID:946199`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1682159-1682878:+; feature_type=gene
