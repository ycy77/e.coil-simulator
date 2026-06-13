---
entity_id: "gene.b0554"
entity_type: "gene"
name: "essD"
source_database: "NCBI RefSeq"
source_id: "gene-b0554"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0554"
  - "essD"
---

# essD

`gene.b0554`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0554`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

essD (gene.b0554) is a gene entity. It encodes essD (protein.P0A9R2). Encoded protein function: Prophage lysis protein S homolog EssD (Lysis protein S homolog from lambdoid prophage DLP12) EcoCyc product frame: G6309-MONOMER. EcoCyc synonyms: vlyS, ybcR. Genomic coordinates: 577398-577613. EcoCyc protein note: EssD is a predicted class II holin of the cryptic lambdoid prophage DLP12. The protein has two potential transmembrane domains . EssD has also been predicted to be a bitopic inner membrane protein . The effect of an essD deletion on biofilm formation is dependent on the strain background. In the BW25113 background, an essD mutation increases biofilm formation , while an essD mutant is impaired in curli-based biofilm formation, which may be an indirect effect due to altered peptidoglycan (PG) metabolism . Deletion of the lysis module of DLP12 defective prophage (essD, rrrD, rzpD/rzoD) induces an hypervesiculation phenotype (possibly due to an excess of PG fragments in the periplasmic space); expression of the module is sensitive to environmental stress factors (low temperature, high osmolarity and acidic pH) .

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9R2|protein.P0A9R2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=essD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001895,ECOCYC:G6309,GeneID:947545`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:577398-577613:+; feature_type=gene
