---
entity_id: "gene.b0555"
entity_type: "gene"
name: "rrrD"
source_database: "NCBI RefSeq"
source_id: "gene-b0555"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0555"
  - "rrrD"
---

# rrrD

`gene.b0555`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0555`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrrD (gene.b0555) is a gene entity. It encodes rrrD (protein.P78285). Encoded protein function: FUNCTION: Essential for lysis of bacterial cell wall, by showing cell wall hydrolyzing activity. Exhibits lytic activity against E.coli and S.typhi cell wall substrate. {ECO:0000269|PubMed:17914239}. EcoCyc product frame: G6310-MONOMER. EcoCyc synonyms: lycV, ybcS. Genomic coordinates: 577613-578110. EcoCyc protein note: RrrD is an endolysin encoded by the cryptic lambdoid prophage DLP12 . Overexpression of RrrD leads to lysis of the cells . The effect of an rrrD deletion on biofilm formation is dependent on the strain background. An rrrD mutant is impaired in curli-based biofilm formation, which may be an indirect effect due to altered peptidoglycan metabolism . Deletion of the lysis module of DLP12 defective prophage (essD, rrrD, rzpD/rzoD) induces an hypervesiculation phenotype (possibly due to an excess of PG fragments in the periplasmic space); expression of the module is sensitive to environmental stress factors (low temperature, high osmolarity and acidic pH) .

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P78285|protein.P78285]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rrrD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001898,ECOCYC:G6310,GeneID:947539`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:577613-578110:+; feature_type=gene
