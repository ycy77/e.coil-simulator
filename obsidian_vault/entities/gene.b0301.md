---
entity_id: "gene.b0301"
entity_type: "gene"
name: "rclC"
source_database: "NCBI RefSeq"
source_id: "gene-b0301"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0301"
  - "rclC"
---

# rclC

`gene.b0301`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0301`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rclC (gene.b0301) is a gene entity. It encodes rclC (protein.P75685). Encoded protein function: FUNCTION: Probably involved in reactive chlorine species (RCS) stress resistance. {ECO:0000269|PubMed:24078635}. EcoCyc product frame: G6171-MONOMER. EcoCyc synonyms: ykgB. Genomic coordinates: 317726-318319. EcoCyc protein note: An rclC deletion mutant is more sensitive to HOCl treatment than wild type, and rclC expression is upregulated under RCS (reactive chlorine species) stress conditions . Membrane topology predictions using experimentally determined C terminus locations indicate that YkgB has 3 transmembrane helices and the C-terminus is located in the cytoplasm . RNAseq analysis in response to HOSCN exposure revealed the log-fold increase in G6174 was significantly higher than for G6173 and G6171. Deletion mutants of each rclABC gene individually and the three genes together resulted in zinc depletion along with upregulation of G6167 and G7061, in addition to a variety of general stress response genes and some poorly characterized genes, such as G6253. Expression of genes that responded differently to the different rcl mutants, such as G6570 and EG10670 were also examined . RclC: "reactive chlorine resistance C"

## Biological Role

Activated by rclR (protein.P77379).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75685|protein.P75685]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P77379|protein.P77379]] `RegulonDB` `S` - regulator=RclR; target=rclC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001038,ECOCYC:G6171,GeneID:944974`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:317726-318319:-; feature_type=gene
