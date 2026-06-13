---
entity_id: "reaction.ecocyc.RXN-16995"
entity_type: "reaction"
name: "RXN-16995"
source_database: "EcoCyc"
source_id: "RXN-16995"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16995

`reaction.ecocyc.RXN-16995`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16995`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Phosphorylated-beta-phosphoglucomutase + CPD-448 -> GLUCOSE-16-DIPHOSPHATE + Beta-phosphoglucomutase + PROTON; direction=REVERSIBLE EcoCyc reaction equation: Phosphorylated-beta-phosphoglucomutase + CPD-448 -> GLUCOSE-16-DIPHOSPHATE + Beta-phosphoglucomutase + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: beta-D-Glucose 1-phosphate (molecule.C00663). Products: H+ (molecule.C00080), glucose-1,6-bisphosphate (molecule.ecocyc.GLUCOSE-16-DIPHOSPHATE).

## Annotation

Phosphorylated-beta-phosphoglucomutase + CPD-448 -> GLUCOSE-16-DIPHOSPHATE + Beta-phosphoglucomutase + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.GLUCOSE-16-DIPHOSPHATE|molecule.ecocyc.GLUCOSE-16-DIPHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00663|molecule.C00663]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16995`

## Notes

Phosphorylated-beta-phosphoglucomutase + CPD-448 -> GLUCOSE-16-DIPHOSPHATE + Beta-phosphoglucomutase + PROTON; direction=REVERSIBLE
