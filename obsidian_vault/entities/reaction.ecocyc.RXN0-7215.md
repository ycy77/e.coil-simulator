---
entity_id: "reaction.ecocyc.RXN0-7215"
entity_type: "reaction"
name: "lactulose:proton symport"
source_database: "EcoCyc"
source_id: "RXN0-7215"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# lactulose:proton symport

`reaction.ecocyc.RXN0-7215`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7215`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CPD-3561 -> PROTON + CPD-3561; direction=REVERSIBLE EcoCyc reaction equation: PROTON + CPD-3561 -> PROTON + CPD-3561; direction=REVERSIBLE.

## Biological Role

Catalyzed by lacY (protein.P02920). Substrates: H+ (molecule.C00080), lactulose (molecule.ecocyc.CPD-3561). Products: H+ (molecule.C00080), lactulose (molecule.ecocyc.CPD-3561).

## Annotation

PROTON + CPD-3561 -> PROTON + CPD-3561; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P02920|protein.P02920]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-3561|molecule.ecocyc.CPD-3561]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3561|molecule.ecocyc.CPD-3561]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7215`

## Notes

PROTON + CPD-3561 -> PROTON + CPD-3561; direction=REVERSIBLE
