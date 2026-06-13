---
entity_id: "reaction.ecocyc.RXN-19630"
entity_type: "reaction"
name: "RXN-19630"
source_database: "EcoCyc"
source_id: "RXN-19630"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19630

`reaction.ecocyc.RXN-19630`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19630`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-1-PHOSPHATIDYL-ETHANOLAMINE + CELLULOSE -> DIACYLGLYCEROL + phosphoethanolamine-cellulose; direction=REVERSIBLE EcoCyc reaction equation: L-1-PHOSPHATIDYL-ETHANOLAMINE + CELLULOSE -> DIACYLGLYCEROL + phosphoethanolamine-cellulose; direction=REVERSIBLE.

## Biological Role

Catalyzed by bcsG (protein.P37659). Substrates: Phosphatidylethanolamine (molecule.C00350), Cellulose (molecule.C00760). Products: 1,2-Diacyl-sn-glycerol (molecule.C00641), phosphoethanolamine cellulose (molecule.ecocyc.phosphoethanolamine-cellulose).

## Annotation

L-1-PHOSPHATIDYL-ETHANOLAMINE + CELLULOSE -> DIACYLGLYCEROL + phosphoethanolamine-cellulose; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37659|protein.P37659]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00641|molecule.C00641]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.phosphoethanolamine-cellulose|molecule.ecocyc.phosphoethanolamine-cellulose]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00350|molecule.C00350]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00760|molecule.C00760]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19630`

## Notes

L-1-PHOSPHATIDYL-ETHANOLAMINE + CELLULOSE -> DIACYLGLYCEROL + phosphoethanolamine-cellulose; direction=REVERSIBLE
