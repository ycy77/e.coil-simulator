---
entity_id: "gene.b2176"
entity_type: "gene"
name: "pdeN"
source_database: "NCBI RefSeq"
source_id: "gene-b2176"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2176"
  - "pdeN"
---

# pdeN

`gene.b2176`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2176`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdeN (gene.b2176) is a gene entity. It encodes pdeN (protein.P76446). Encoded protein function: FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}. EcoCyc product frame: G7148-MONOMER. EcoCyc synonyms: rtn. Genomic coordinates: 2270726-2272282. EcoCyc protein note: PdeN is a predicted c-di-GMP phosphodiesterase; the protein is predicted to contain two transmembrane domains flanking a periplasmic CSS domain containing two highly conserved cysteines, followed by a cytoplasmic C-terminal EAL domain with predicted phosphodiesterase activity . PdeN is one of 5 CSS domain containing c-di-GMP phosphodiesterases in E. coli K-12; redox control and proteolysis of these enzymes is believed to modulate their activity and affect matrix production in biofilm (see ). A screen for suppressors of the motility defect of a EG12252 ΔpdeH mutant identified activating mutations in E. coli's alternative c-di-GMP phosphodiesterases (PDEs), including PdeN. This supports the view that many of the candidate c-di-GMP phosphodiesterases encoded in the E. coli genome require an appropriate stimulus to become active...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76446|protein.P76446]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007203,ECOCYC:G7148,GeneID:946695`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2270726-2272282:+; feature_type=gene
