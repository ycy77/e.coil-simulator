---
entity_id: "protein.P0ABX8"
entity_type: "protein"
name: "fliL"
source_database: "UniProt"
source_id: "P0ABX8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliL cheC1 fla AI fla QI b1944 JW1928"
---

# fliL

`protein.P0ABX8`

## Static

- Type: `protein`
- Source: `UniProt:P0ABX8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Controls the rotational direction of flagella during chemotaxis. fliL is the first of seven genes within the flagellar associated flaA locus (see also ). The specific function of FliL remains uncertain - recent studies in E. coli and Salmonella typhimurium, report conflicting evidence implicating FliL in motor torque generation. FliL is required for the 'motor remodeling' that is associated with swarming; FliL may act as a hub to connect and stabilize the stator (MotAB) and core basal body complexes . Single flagella motors from ΔfliL strains rotate at lower speeds and switch directions less frequently when compared to wild type and this defect is exacebated under conditions of high load; a ΔfliL strain is defective in swarming and mutant cells appear to have fractured or released filaments on swarm agar . Loss of fliL does not affect motor torque generation under a range of loads; loss of fliL does not affect rotor-stator associations (the number of stator units engaged by motors at high loads is similar in wild-type and fliL mutants); loss of fliL does not affect motor-reversal (switching) and a fliL deletion mutant is capable of swarming . Varying phenotypes have been reported for fliL null mutants. The non-flagellate phenotype of a fliL insertion mutant is the result of polarity; in-frame fliL deletion mutants exhibit wild-type chemotactic swarming...

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452), flagellar basal body (complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Controls the rotational direction of flagella during chemotaxis.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX|complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1944|gene.b1944]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABX8`
- `KEGG:ecj:JW1928;eco:b1944;ecoc:C3026_11010;`
- `GeneID:75172063;946443;`
- `GO:GO:0005886; GO:0006935; GO:0009425; GO:0042802; GO:0071978`

## Notes

Flagellar protein FliL
