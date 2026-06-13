---
entity_id: "protein.P26458"
entity_type: "protein"
name: "appB"
source_database: "UniProt"
source_id: "P26458"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "appB cbdB cyxB b0979 JW0961"
---

# appB

`protein.P26458`

## Static

- Type: `protein`
- Source: `UniProt:P26458`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: A terminal oxidase that catalyzes quinol-dependent, Na(+)-independent oxygen uptake. Prefers menadiol over other quinols although ubiquinol was not tested (PubMed:8626304). Generates a proton motive force using protons and electrons from opposite sides of the membrane to generate H(2)O, transferring 1 proton/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:21987791, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:8626304}. appB encodes subunit II of cytochrome bd-II. AppB has 57.5% homology with the CYDB-MONOMER "CydB" subunit of CYT-D-UBIOX-CPLX . The AppB subunit harbors a structural ubiquinone-8 or DEMETHYLMENAQUINONE demethylmenaquinone-8 molecule.

## Biological Role

Component of cytochrome bd-II ubiquinol:oxygen oxidoreductase (complex.ecocyc.APP-UBIOX-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: A terminal oxidase that catalyzes quinol-dependent, Na(+)-independent oxygen uptake. Prefers menadiol over other quinols although ubiquinol was not tested (PubMed:8626304). Generates a proton motive force using protons and electrons from opposite sides of the membrane to generate H(2)O, transferring 1 proton/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:21987791, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:8626304}.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.APP-UBIOX-CPLX|complex.ecocyc.APP-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0979|gene.b0979]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P26458`
- `KEGG:ecj:JW0961;eco:b0979;ecoc:C3026_05970;`
- `GeneID:93776434;947547;`
- `GO:GO:0005886; GO:0009055; GO:0009486; GO:0016682; GO:0019646; GO:0046872; GO:0070069`
- `EC:7.1.1.3`

## Notes

Cytochrome bd-II ubiquinol oxidase subunit 2 (EC 7.1.1.3) (Cytochrome bd-II oxidase subunit II)
