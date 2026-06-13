---
entity_id: "reaction.ecocyc.TRANS-RXN-282"
entity_type: "reaction"
name: "L-valine:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-282"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-valine:proton antiport

`reaction.ecocyc.TRANS-RXN-282`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-282`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

VAL + PROTON -> VAL + PROTON; direction=REVERSIBLE EcoCyc reaction equation: VAL + PROTON -> VAL + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by yjeH (protein.P39277). Substrates: H+ (molecule.C00080), L-Valine (molecule.C00183). Products: H+ (molecule.C00080), L-Valine (molecule.C00183).

## Annotation

VAL + PROTON -> VAL + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P39277|protein.P39277]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-282`

## Notes

VAL + PROTON -> VAL + PROTON; direction=REVERSIBLE
