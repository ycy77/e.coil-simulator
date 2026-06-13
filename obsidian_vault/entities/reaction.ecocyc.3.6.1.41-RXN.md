---
entity_id: "reaction.ecocyc.3.6.1.41-RXN"
entity_type: "reaction"
name: "3.6.1.41-RXN"
source_database: "EcoCyc"
source_id: "3.6.1.41-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "DIADENOSINETETRAPHOSPHATASE (SYMMETRICAL)"
  - "DINUCLEOSIDETETRAPHOSPHATASE (SYMMETRICAL)"
---

# 3.6.1.41-RXN

`reaction.ecocyc.3.6.1.41-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.6.1.41-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ALSO ACTS ON BIS(5'-GUANOSYL) TETRAPHOSPHATE AND BIS(5'-ADENOSYL) PENTAPHOSPHATE, AND, MORE SLOWLY, ON SOME OTHER POLYPHOSPHATES, FORMING A NUCLEOSIDE BIS-PHOSPHATE AS ONE PRODUCT IN ALL CASES (CF. EC 3.6.1.17). EcoCyc reaction equation: WATER + ADENOSYL-P4 -> PROTON + ADP; direction=LEFT-TO-RIGHT. ALSO ACTS ON BIS(5'-GUANOSYL) TETRAPHOSPHATE AND BIS(5'-ADENOSYL) PENTAPHOSPHATE, AND, MORE SLOWLY, ON SOME OTHER POLYPHOSPHATES, FORMING A NUCLEOSIDE BIS-PHOSPHATE AS ONE PRODUCT IN ALL CASES (CF. EC 3.6.1.17).

## Biological Role

Catalyzed by apaH (protein.P05637). Substrates: H2O (molecule.C00001), P1,P4-Bis(5'-adenosyl)tetraphosphate (molecule.C01260). Products: ADP (molecule.C00008), H+ (molecule.C00080).

## Annotation

ALSO ACTS ON BIS(5'-GUANOSYL) TETRAPHOSPHATE AND BIS(5'-ADENOSYL) PENTAPHOSPHATE, AND, MORE SLOWLY, ON SOME OTHER POLYPHOSPHATES, FORMING A NUCLEOSIDE BIS-PHOSPHATE AS ONE PRODUCT IN ALL CASES (CF. EC 3.6.1.17).

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `activates` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P05637|protein.P05637]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01260|molecule.C01260]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C04494|molecule.C04494]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1415|molecule.ecocyc.CPD0-1415]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.6.1.41-RXN`

## Notes

WATER + ADENOSYL-P4 -> PROTON + ADP; direction=LEFT-TO-RIGHT
