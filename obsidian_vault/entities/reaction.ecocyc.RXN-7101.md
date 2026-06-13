---
entity_id: "reaction.ecocyc.RXN-7101"
entity_type: "reaction"
name: "RXN-7101"
source_database: "EcoCyc"
source_id: "RXN-7101"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-7101

`reaction.ecocyc.RXN-7101`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-7101`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

BCCP-biotin-L-lysine -> biotin-L-lysine-in-BCCP-dimers; direction=LEFT-TO-RIGHT EcoCyc reaction equation: BCCP-biotin-L-lysine -> biotin-L-lysine-in-BCCP-dimers; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: a [biotin carboxyl-carrier protein]-N6-biotinyl-L-lysine (molecule.ecocyc.BCCP-biotin-L-lysine). Products: a [biotin carboxyl-carrier-protein dimer]-N6-biotinyl-L-lysine (molecule.ecocyc.biotin-L-lysine-in-BCCP-dimers).

## Enriched Pathways

- `ecocyc.PWY0-1264` malonyl-CoA biosynthesis via biotin-carboxyl carrier protein (EcoCyc)

## Annotation

BCCP-biotin-L-lysine -> biotin-L-lysine-in-BCCP-dimers; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1264` malonyl-CoA biosynthesis via biotin-carboxyl carrier protein (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.biotin-L-lysine-in-BCCP-dimers|molecule.ecocyc.biotin-L-lysine-in-BCCP-dimers]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.BCCP-biotin-L-lysine|molecule.ecocyc.BCCP-biotin-L-lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-7101`

## Notes

BCCP-biotin-L-lysine -> biotin-L-lysine-in-BCCP-dimers; direction=LEFT-TO-RIGHT
