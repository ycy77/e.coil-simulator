---
entity_id: "reaction.ecocyc.TRANS-RXN0-205"
entity_type: "reaction"
name: "TRANS-RXN0-205"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-205"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-205

`reaction.ecocyc.TRANS-RXN0-205`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-205`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

E. coli is definitely able to import pyridoxine which is then utilized in the pyridoxal 5'-phosphate salvage pathway, but the transporter responsible for this is unkown. EcoCyc reaction equation: PYRIDOXINE -> PYRIDOXINE; direction=LEFT-TO-RIGHT. E. coli is definitely able to import pyridoxine which is then utilized in the pyridoxal 5'-phosphate salvage pathway, but the transporter responsible for this is unkown.

## Biological Role

Catalyzed by pyridoxine transporter (protein.ecocyc.MONOMER0-2797). Substrates: Pyridoxine (molecule.C00314). Products: Pyridoxine (molecule.C00314).

## Annotation

E. coli is definitely able to import pyridoxine which is then utilized in the pyridoxal 5'-phosphate salvage pathway, but the transporter responsible for this is unkown.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.ecocyc.MONOMER0-2797|protein.ecocyc.MONOMER0-2797]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00314|molecule.C00314]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00314|molecule.C00314]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-205`

## Notes

PYRIDOXINE -> PYRIDOXINE; direction=LEFT-TO-RIGHT
