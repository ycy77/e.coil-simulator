---
entity_id: "reaction.ecocyc.TRANS-RXN0-496"
entity_type: "reaction"
name: "enterobactin export"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-496"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# enterobactin export

`reaction.ecocyc.TRANS-RXN0-496`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-496`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ENTEROBACTIN + PROTON -> ENTEROBACTIN + PROTON; direction=REVERSIBLE EcoCyc reaction equation: ENTEROBACTIN + PROTON -> ENTEROBACTIN + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by entS (protein.P24077). Substrates: H+ (molecule.C00080), Enterochelin (molecule.C05821). Products: H+ (molecule.C00080), Enterochelin (molecule.C05821).

## Annotation

ENTEROBACTIN + PROTON -> ENTEROBACTIN + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P24077|protein.P24077]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05821|molecule.C05821]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05821|molecule.C05821]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-496`

## Notes

ENTEROBACTIN + PROTON -> ENTEROBACTIN + PROTON; direction=REVERSIBLE
