---
entity_id: "reaction.ecocyc.OXAMATE-CARBAMOYLTRANSFERASE-RXN"
entity_type: "reaction"
name: "OXAMATE-CARBAMOYLTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "OXAMATE-CARBAMOYLTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Oxamic transcarbamylase"
---

# OXAMATE-CARBAMOYLTRANSFERASE-RXN

`reaction.ecocyc.OXAMATE-CARBAMOYLTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:OXAMATE-CARBAMOYLTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OXAMATE + CARBAMOYL-P -> Pi + CPD-389; direction=REVERSIBLE EcoCyc reaction equation: OXAMATE + CARBAMOYL-P -> Pi + CPD-389; direction=REVERSIBLE.

## Biological Role

Catalyzed by oxamate carbamoyltransferase (complex.ecocyc.CPLX0-12207). Substrates: Carbamoyl phosphate (molecule.C00169), Oxamate (molecule.C01444). Products: Oxalureate (molecule.C00802), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-41` allantoin degradation IV (anaerobic) (EcoCyc)

## Annotation

OXAMATE + CARBAMOYL-P -> Pi + CPD-389; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-41` allantoin degradation IV (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-12207|complex.ecocyc.CPLX0-12207]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00802|molecule.C00802]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00169|molecule.C00169]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01444|molecule.C01444]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:OXAMATE-CARBAMOYLTRANSFERASE-RXN`

## Notes

OXAMATE + CARBAMOYL-P -> Pi + CPD-389; direction=REVERSIBLE
