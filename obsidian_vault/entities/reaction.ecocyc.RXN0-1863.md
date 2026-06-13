---
entity_id: "reaction.ecocyc.RXN0-1863"
entity_type: "reaction"
name: "RXN0-1863"
source_database: "EcoCyc"
source_id: "RXN0-1863"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1863

`reaction.ecocyc.RXN0-1863`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1863`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-4-AMINO-4-DEOXY-L-ARABINOSE + 2-KETOGLUTARATE -> 5-BETA-L-THREO-PENTAPYRANOSYL-4-ULOSE- + GLT; direction=REVERSIBLE EcoCyc reaction equation: UDP-4-AMINO-4-DEOXY-L-ARABINOSE + 2-KETOGLUTARATE -> 5-BETA-L-THREO-PENTAPYRANOSYL-4-ULOSE- + GLT; direction=REVERSIBLE.

## Biological Role

Catalyzed by arnB (protein.P77690). Substrates: 2-Oxoglutarate (molecule.C00026), UDP-L-Ara4N (molecule.C16153). Products: L-Glutamate (molecule.C00025), UDP-L-Ara4O (molecule.C16155).

## Enriched Pathways

- `ecocyc.PWY0-1338` polymyxin resistance (EcoCyc)

## Annotation

UDP-4-AMINO-4-DEOXY-L-ARABINOSE + 2-KETOGLUTARATE -> 5-BETA-L-THREO-PENTAPYRANOSYL-4-ULOSE- + GLT; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1338` polymyxin resistance (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77690|protein.P77690]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16155|molecule.C16155]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16153|molecule.C16153]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1863`

## Notes

UDP-4-AMINO-4-DEOXY-L-ARABINOSE + 2-KETOGLUTARATE -> 5-BETA-L-THREO-PENTAPYRANOSYL-4-ULOSE- + GLT; direction=REVERSIBLE
