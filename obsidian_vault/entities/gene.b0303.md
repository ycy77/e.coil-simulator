---
entity_id: "gene.b0303"
entity_type: "gene"
name: "rclB"
source_database: "NCBI RefSeq"
source_id: "gene-b0303"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0303"
  - "rclB"
---

# rclB

`gene.b0303`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0303`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rclB (gene.b0303) is a gene entity. It encodes rclB (protein.P75687). Encoded protein function: FUNCTION: Probably involved in reactive chlorine species (RCS) stress resistance. {ECO:0000269|PubMed:24078635}. EcoCyc product frame: G6173-MONOMER. EcoCyc synonyms: ykgI. Genomic coordinates: 318331-318567. EcoCyc protein note: An rclB deletion mutant is more sensitive to HOCl treatment than wild type, and rclB expression is upregulated under RCS (reactive chlorine species) stress conditions . The expression of rclB is also upregulated in bacteria phagocytosed by neutrophils, probably due to HOCl produced by neutrophils . RNAseq analysis in response to HOSCN exposure revealed the log-fold increase in G6174 was significantly higher than for G6173 and G6171. Deletion mutants of each rclABC gene individually and the three genes together resulted in zinc depletion along with upregulation of G6167 and G7061, in addition to a variety of general stress response genes and some poorly characterized genes, such as G6253. Expression of genes that responded differently to the different rcl mutants, such as G6570 and EG10670 were also examined . RclB: "reactive chlorine resistance B"

## Biological Role

Activated by rclR (protein.P77379).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75687|protein.P75687]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P77379|protein.P77379]] `RegulonDB` `S` - regulator=RclR; target=rclB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001043,ECOCYC:G6173,GeneID:945658`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:318331-318567:-; feature_type=gene
