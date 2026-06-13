---
entity_id: "protein.P15070"
entity_type: "protein"
name: "fliN"
source_database: "UniProt"
source_id: "P15070"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein; Cytoplasmic side. Bacterial flagellum basal body."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliN flaN motD b1946 JW1930"
---

# fliN

`protein.P15070`

## Static

- Type: `protein`
- Source: `UniProt:P15070`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein; Cytoplasmic side. Bacterial flagellum basal body.

## Enriched Summary

FUNCTION: FliN is one of three proteins (FliG, FliN, FliM) that form a switch complex that is proposed to be located at the base of the basal body. This complex interacts with the CheY and CheZ chemotaxis proteins, in addition to contacting components of the motor that determine the direction of flagellar rotation. FliN, is one of three components of the flagellar motor's "switch complex." The crystal structure of the C-terminal domain of the FliN protein in Thermotoga maritime has been determined to 3.4 Å resolution . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452), flagellar basal body (complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX).

## Enriched Pathways

- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: FliN is one of three proteins (FliG, FliN, FliM) that form a switch complex that is proposed to be located at the base of the basal body. This complex interacts with the CheY and CheZ chemotaxis proteins, in addition to contacting components of the motor that determine the direction of flagellar rotation.

## Pathways

- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX|complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1946|gene.b1946]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15070`
- `KEGG:ecj:JW1930;eco:b1946;ecoc:C3026_11020;`
- `GeneID:946423;`
- `GO:GO:0003774; GO:0004721; GO:0005886; GO:0006935; GO:0009288; GO:0009433; GO:0071977; GO:0120107; GO:1902021`

## Notes

Flagellar motor switch protein FliN
