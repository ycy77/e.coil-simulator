---
entity_id: "reaction.ecocyc.PYRAMKIN-RXN"
entity_type: "reaction"
name: "PYRAMKIN-RXN"
source_database: "EcoCyc"
source_id: "PYRAMKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PYRAMKIN-RXN

`reaction.ecocyc.PYRAMKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYRAMKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is an alternate substrate reaction for E.C. reaction number 2.7.1.35. EcoCyc reaction equation: ATP + PYRIDOXAMINE -> PROTON + ADP + PYRIDOXAMINE-5P; direction=LEFT-TO-RIGHT. This is an alternate substrate reaction for E.C. reaction number 2.7.1.35.

## Biological Role

Catalyzed by pyridoxal kinase 1 / hydroxymethylpyrimidine kinase (complex.ecocyc.PDXK-CPLX). Substrates: ATP (molecule.C00002), Pyridoxamine (molecule.C00534). Products: ADP (molecule.C00008), H+ (molecule.C00080), Pyridoxamine phosphate (molecule.C00647).

## Enriched Pathways

- `ecocyc.PLPSAL-PWY` pyridoxal 5'-phosphate salvage I (EcoCyc)

## Annotation

This is an alternate substrate reaction for E.C. reaction number 2.7.1.35.

## Pathways

- `ecocyc.PLPSAL-PWY` pyridoxal 5'-phosphate salvage I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.PDXK-CPLX|complex.ecocyc.PDXK-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00647|molecule.C00647]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00534|molecule.C00534]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1605|molecule.ecocyc.CPD0-1605]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PYRAMKIN-RXN`

## Notes

ATP + PYRIDOXAMINE -> PROTON + ADP + PYRIDOXAMINE-5P; direction=LEFT-TO-RIGHT
