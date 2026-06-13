---
entity_id: "gene.b0556"
entity_type: "gene"
name: "rzpD"
source_database: "NCBI RefSeq"
source_id: "gene-b0556"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0556"
  - "rzpD"
---

# rzpD

`gene.b0556`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0556`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rzpD (gene.b0556) is a gene entity. It encodes rzpD (protein.P75719). Encoded protein function: FUNCTION: Necessary for host cell lysis. It is believed to code for an endopeptidase that cleaves the amino-carboxyl cross-link between the diaminopimelic acid and D-alanine residues in the murein component of the bacterial cell wall (By similarity). {ECO:0000250}. EcoCyc product frame: G6311-MONOMER. EcoCyc synonyms: ybcT. Genomic coordinates: 578107-578568. EcoCyc protein note: RzpD is a predicted lysis protein of the cryptic lambdoid prophage DLP12 and is part of the lysis cassette. An rzpD/rzoD mutant is impaired in curli-based biofilm formation, which may be an indirect effect due to altered peptidoglycan metabolism . Deletion of the lysis module of DLP12 defective prophage (essD, rrrD, rzpD/rzoD) induces an hypervesiculation phenotype (possibly due to an excess of PG fragments in the periplasmic space); expression of the module is sensitive to environmental stress factors (low temperature, high osmolarity and acidic pH) . Expression of the DLP12 lysis cassette is positively regulated by Hha , YbcQ , and the alternative sigma factor RPOE-MONOMER σE . In an rzpD/rzoD deletion mutant, induction of Hha results in significantly less growth inhibition than in wild-type .

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75719|protein.P75719]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rzpD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001900,ECOCYC:G6311,GeneID:945929`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:578107-578568:+; feature_type=gene
