---
entity_id: "protein.P09348"
entity_type: "protein"
name: "motA"
source_database: "UniProt"
source_id: "P09348"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "motA flaJ b1890 JW1879"
---

# motA

`protein.P09348`

## Static

- Type: `protein`
- Source: `UniProt:P09348`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: MotA and MotB comprise the stator element of the flagellar motor complex. Required for rotation of the flagellar motor. Probable transmembrane proton channel. Overexpression of MotA, with or without MotB, restores motility in a pdeH disruption, (a c-di-GMP phosphodiesterase) suggesting there is an interaction (direct or indirect) between the c-di-GMP-binding flagellar brake protein YcgR and the flagellar stator. {ECO:0000269|PubMed:20346719}. MotA and MOTB-FLAGELLAR-MOTOR-STATOR-PROTEIN MotB comprise the stator unit of the flagellar motor complex; MotAB complexes are anchored in the peptidoglycan and form a proton conducting channel across the inner membrane; movement of protons down their concentration gradient via the stator provides the energy for torque generation in the flagellar motor. Early studies in E. coli K-12 derived strains characterized mot mutants which are paralysed (cells possess flagella but are non-motile) and defined the 'Mocha' operon which includes the motA, motB and cheA cistrons . Inducing expression of cloned, wild-type motA restores torque to paralysed motA mutants . motA and motB gene products are integral inner membrane proteins which can be visualized, using freeze-fracture electron micrscopy, as intramembrane particle ring structures arrayed around the flagellar base...

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452), flagellar basal body (complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: MotA and MotB comprise the stator element of the flagellar motor complex. Required for rotation of the flagellar motor. Probable transmembrane proton channel. Overexpression of MotA, with or without MotB, restores motility in a pdeH disruption, (a c-di-GMP phosphodiesterase) suggesting there is an interaction (direct or indirect) between the c-di-GMP-binding flagellar brake protein YcgR and the flagellar stator. {ECO:0000269|PubMed:20346719}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX|complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1890|gene.b1890]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09348`
- `KEGG:ecj:JW1879;eco:b1890;ecoc:C3026_10745;`
- `GeneID:947564;`
- `GO:GO:0005886; GO:0006935; GO:0009288; GO:0015252; GO:0071973; GO:0071978; GO:0120101; GO:1902600`

## Notes

Motility protein A (Chemotaxis protein MotA)
