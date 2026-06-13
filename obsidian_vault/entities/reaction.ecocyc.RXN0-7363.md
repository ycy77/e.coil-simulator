---
entity_id: "reaction.ecocyc.RXN0-7363"
entity_type: "reaction"
name: "RXN0-7363"
source_database: "EcoCyc"
source_id: "RXN0-7363"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7363

`reaction.ecocyc.RXN0-7363`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7363`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CU+2 + OXYGEN-MOLECULE + NADH -> CU+ + WATER + NAD; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CU+2 + OXYGEN-MOLECULE + NADH -> CU+ + WATER + NAD; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cupric reductase RclA (complex.ecocyc.CPLX0-8542). Substrates: NADH (molecule.C00004), Oxygen (molecule.C00007), Cu2+ (molecule.ecocyc.CU_2). Products: H2O (molecule.C00001), NAD+ (molecule.C00003), Cu+ (molecule.ecocyc.CU_).

## Annotation

CU+2 + OXYGEN-MOLECULE + NADH -> CU+ + WATER + NAD; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8542|complex.ecocyc.CPLX0-8542]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CU|molecule.ecocyc.CU_]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7363`

## Notes

CU+2 + OXYGEN-MOLECULE + NADH -> CU+ + WATER + NAD; direction=LEFT-TO-RIGHT
