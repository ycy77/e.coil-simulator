---
entity_id: "reaction.ecocyc.MALATE-DEHYDROGENASE-NADP_-RXN"
entity_type: "reaction"
name: "MALATE-DEHYDROGENASE-NADP+-RXN"
source_database: "EcoCyc"
source_id: "MALATE-DEHYDROGENASE-NADP+-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MALATE-DEHYDROGENASE-NADP+-RXN

`reaction.ecocyc.MALATE-DEHYDROGENASE-NADP_-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MALATE-DEHYDROGENASE-NADP+-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MAL + NADP -> PROTON + NADPH + OXALACETIC_ACID; direction=REVERSIBLE EcoCyc reaction equation: MAL + NADP -> PROTON + NADPH + OXALACETIC_ACID; direction=REVERSIBLE.

## Biological Role

Substrates: NADP+ (molecule.C00006), (S)-Malate (molecule.C00149). Products: NADPH (molecule.C00005), Oxaloacetate (molecule.C00036), H+ (molecule.C00080).

## Annotation

MAL + NADP -> PROTON + NADPH + OXALACETIC_ACID; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MALATE-DEHYDROGENASE-NADP+-RXN`

## Notes

MAL + NADP -> PROTON + NADPH + OXALACETIC_ACID; direction=REVERSIBLE
