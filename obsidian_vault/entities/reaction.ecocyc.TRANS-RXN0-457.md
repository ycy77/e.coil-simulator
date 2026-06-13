---
entity_id: "reaction.ecocyc.TRANS-RXN0-457"
entity_type: "reaction"
name: "3-hydroxycinnamate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-457"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-hydroxycinnamate:proton symport

`reaction.ecocyc.TRANS-RXN0-457`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-457`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-10797 + PROTON -> CPD-10797 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-10797 + PROTON -> CPD-10797 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by mhpT (protein.P77589). Substrates: H+ (molecule.C00080), trans-3-Hydroxycinnamate (molecule.C12621). Products: H+ (molecule.C00080), trans-3-Hydroxycinnamate (molecule.C12621).

## Annotation

CPD-10797 + PROTON -> CPD-10797 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77589|protein.P77589]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C12621|molecule.C12621]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C12621|molecule.C12621]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-457`

## Notes

CPD-10797 + PROTON -> CPD-10797 + PROTON; direction=REVERSIBLE
