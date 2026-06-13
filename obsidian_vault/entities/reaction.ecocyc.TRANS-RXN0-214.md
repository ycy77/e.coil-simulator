---
entity_id: "reaction.ecocyc.TRANS-RXN0-214"
entity_type: "reaction"
name: "TRANS-RXN0-214"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-214"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-214

`reaction.ecocyc.TRANS-RXN0-214`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-214`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

E. coli is able to import pyridoxal, which is then utilized in the pyridoxal 5'-phosphate salvage pathway, but the transporter responsible for this has not been identified. EcoCyc reaction equation: PYRIDOXAL -> PYRIDOXAL; direction=LEFT-TO-RIGHT. E. coli is able to import pyridoxal, which is then utilized in the pyridoxal 5'-phosphate salvage pathway, but the transporter responsible for this has not been identified.

## Biological Role

Catalyzed by MONOMER0-2799 (protein.ecocyc.MONOMER0-2799). Substrates: Pyridoxal (molecule.C00250). Products: Pyridoxal (molecule.C00250).

## Annotation

E. coli is able to import pyridoxal, which is then utilized in the pyridoxal 5'-phosphate salvage pathway, but the transporter responsible for this has not been identified.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.ecocyc.MONOMER0-2799|protein.ecocyc.MONOMER0-2799]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00250|molecule.C00250]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00250|molecule.C00250]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1605|molecule.ecocyc.CPD0-1605]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-214`

## Notes

PYRIDOXAL -> PYRIDOXAL; direction=LEFT-TO-RIGHT
