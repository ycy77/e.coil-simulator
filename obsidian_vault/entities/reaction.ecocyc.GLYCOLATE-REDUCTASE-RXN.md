---
entity_id: "reaction.ecocyc.GLYCOLATE-REDUCTASE-RXN"
entity_type: "reaction"
name: "GLYCOLATE-REDUCTASE-RXN"
source_database: "EcoCyc"
source_id: "GLYCOLATE-REDUCTASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYCOLATE-REDUCTASE-RXN

`reaction.ecocyc.GLYCOLATE-REDUCTASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYCOLATE-REDUCTASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLYCOLLATE + NAD -> PROTON + NADH + GLYOX; direction=LEFT-TO-RIGHT EcoCyc reaction equation: GLYCOLLATE + NAD -> PROTON + NADH + GLYOX; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: NAD+ (molecule.C00003), Glycolate (molecule.C00160). Products: NADH (molecule.C00004), Glyoxylate (molecule.C00048), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Annotation

GLYCOLLATE + NAD -> PROTON + NADH + GLYOX; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLYCOLATE-REDUCTASE-RXN`

## Notes

GLYCOLLATE + NAD -> PROTON + NADH + GLYOX; direction=LEFT-TO-RIGHT
