---
entity_id: "protein.P0AB20"
entity_type: "protein"
name: "hspQ"
source_database: "UniProt"
source_id: "P0AB20"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hspQ yccV b0966 JW5970"
---

# hspQ

`protein.P0AB20`

## Static

- Type: `protein`
- Source: `UniProt:P0AB20`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in the degradation of certain denaturated proteins, including DnaA, during heat shock stress. HspQ binds to hemimethylated DNA at oriC . The HspQ protein of Yersinia pestis functions as a specificity-enhancing factor for the Lon protease . In Salmonella enterica, HspQ switches from activating Lon to binding and inhibiting ClpS-dependent proteolysis upon acetylation . The HspQ protein appeared to form dimers and higher order multimers in solution ; in a crystal structure, HspQ forms a homotrimer . An hspQ mutant suppresses the temperature sensitivity of the dnaA508 and dnaA167 alleles ; reports differ on whether or not an hspQ mutant also suppresses the temperature sensitivity of the dnaA46 allele. Overexpression of HspQ exacerbates the growth defect of the dnaA508 and dnaA167 alleles . Overexpression of the D25A, D27A, W51A, H53A, or Y67A mutants of HspQ exacerbate the dnaA508 growth defect to a lesser degree than wild type; thus, these residues appear to be involved in the in vivo function of HspQ . HspQ protein stimulates the degradation of the DnaA508 mutant protein, but not of DnaA46 . In an hspQ mutant, levels of DnaA appear to be increased . hspQ transcription depends on the heat shock sigma factor σ32 . HspQ: "heat shock protein Q"

## Biological Role

Component of heat shock protein HspQ (complex.ecocyc.CPLX0-3921).

## Annotation

FUNCTION: Involved in the degradation of certain denaturated proteins, including DnaA, during heat shock stress.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3921|complex.ecocyc.CPLX0-3921]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0966|gene.b0966]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB20`
- `KEGG:ecj:JW5970;eco:b0966;ecoc:C3026_05905;`
- `GeneID:86863484;93776448;945578;`
- `GO:GO:0005737; GO:0009408; GO:0042802; GO:0044729; GO:0070207`

## Notes

Heat shock protein HspQ
