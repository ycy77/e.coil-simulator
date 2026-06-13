---
entity_id: "reaction.ecocyc.25-DIOXOVALERATE-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "25-DIOXOVALERATE-DEHYDROGENASE-RXN"
source_database: "EcoCyc"
source_id: "25-DIOXOVALERATE-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 25-DIOXOVALERATE-DEHYDROGENASE-RXN

`reaction.ecocyc.25-DIOXOVALERATE-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:25-DIOXOVALERATE-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-654 + WATER + NADP -> 2-KETOGLUTARATE + NADPH + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-654 + WATER + NADP -> 2-KETOGLUTARATE + NADPH + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), 2,5-Dioxopentanoate (molecule.C00433). Products: NADPH (molecule.C00005), 2-Oxoglutarate (molecule.C00026), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-6760` D-xylose degradation III (EcoCyc)

## Annotation

CPD-654 + WATER + NADP -> 2-KETOGLUTARATE + NADPH + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6760` D-xylose degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00433|molecule.C00433]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:25-DIOXOVALERATE-DEHYDROGENASE-RXN`

## Notes

CPD-654 + WATER + NADP -> 2-KETOGLUTARATE + NADPH + PROTON; direction=LEFT-TO-RIGHT
