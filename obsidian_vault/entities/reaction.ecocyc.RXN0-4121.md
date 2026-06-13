---
entity_id: "reaction.ecocyc.RXN0-4121"
entity_type: "reaction"
name: "RXN0-4121"
source_database: "EcoCyc"
source_id: "RXN0-4121"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4121

`reaction.ecocyc.RXN0-4121`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4121`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GMP-LYSINE-PHOSPHORAMIDATE + WATER -> GMP + CPD0-1442; direction=LEFT-TO-RIGHT EcoCyc reaction equation: GMP-LYSINE-PHOSPHORAMIDATE + WATER -> GMP + CPD0-1442; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by purine nucleoside phosphoramidase (complex.ecocyc.CPLX0-7755). Substrates: H2O (molecule.C00001), GMP-N-ε-(N-α-acetyl lysine methyl ester) 5'-phosphoramidate (molecule.ecocyc.GMP-LYSINE-PHOSPHORAMIDATE). Products: GMP (molecule.C00144), N-α-acetyl lysine methyl ester (molecule.ecocyc.CPD0-1442).

## Annotation

GMP-LYSINE-PHOSPHORAMIDATE + WATER -> GMP + CPD0-1442; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7755|complex.ecocyc.CPLX0-7755]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1442|molecule.ecocyc.CPD0-1442]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.GMP-LYSINE-PHOSPHORAMIDATE|molecule.ecocyc.GMP-LYSINE-PHOSPHORAMIDATE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-2464|molecule.ecocyc.CPD0-2464]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-4121`

## Notes

GMP-LYSINE-PHOSPHORAMIDATE + WATER -> GMP + CPD0-1442; direction=LEFT-TO-RIGHT
