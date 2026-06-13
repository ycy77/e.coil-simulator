---
entity_id: "reaction.ecocyc.TRANS-RXN0-213"
entity_type: "reaction"
name: "TRANS-RXN0-213"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-213"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-213

`reaction.ecocyc.TRANS-RXN0-213`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-213`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

E. coli is able to import pyridoxamine, which is then utilized in the pyridoxal 5'-phosphate salvage pathway, but the transporter responsible for this has not been identified. EcoCyc reaction equation: PYRIDOXAMINE -> PYRIDOXAMINE; direction=LEFT-TO-RIGHT. E. coli is able to import pyridoxamine, which is then utilized in the pyridoxal 5'-phosphate salvage pathway, but the transporter responsible for this has not been identified.

## Biological Role

Catalyzed by MONOMER0-2798 (protein.ecocyc.MONOMER0-2798). Substrates: Pyridoxamine (molecule.C00534). Products: Pyridoxamine (molecule.C00534).

## Annotation

E. coli is able to import pyridoxamine, which is then utilized in the pyridoxal 5'-phosphate salvage pathway, but the transporter responsible for this has not been identified.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.ecocyc.MONOMER0-2798|protein.ecocyc.MONOMER0-2798]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00534|molecule.C00534]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00534|molecule.C00534]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-213`

## Notes

PYRIDOXAMINE -> PYRIDOXAMINE; direction=LEFT-TO-RIGHT
