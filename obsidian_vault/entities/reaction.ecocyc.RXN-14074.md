---
entity_id: "reaction.ecocyc.RXN-14074"
entity_type: "reaction"
name: "RXN-14074"
source_database: "EcoCyc"
source_id: "RXN-14074"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14074

`reaction.ecocyc.RXN-14074`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14074`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP + AMP -> GDP + ADP; direction=REVERSIBLE EcoCyc reaction equation: GTP + AMP -> GDP + ADP; direction=REVERSIBLE.

## Biological Role

Catalyzed by adk (protein.P69441). Substrates: AMP (molecule.C00020), GTP (molecule.C00044). Products: ADP (molecule.C00008), GDP (molecule.C00035).

## Annotation

GTP + AMP -> GDP + ADP; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P69441|protein.P69441]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14074`

## Notes

GTP + AMP -> GDP + ADP; direction=REVERSIBLE
