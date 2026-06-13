---
entity_id: "reaction.ecocyc.RXN-8182"
entity_type: "reaction"
name: "RXN-8182"
source_database: "EcoCyc"
source_id: "RXN-8182"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8182

`reaction.ecocyc.RXN-8182`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8182`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-280 + NADP + WATER -> GLUTARATE + NADPH + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-280 + NADP + WATER -> GLUTARATE + NADPH + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by succinate semialdehyde dehydrogenase (NAD(P)+) Sad (complex.ecocyc.CPLX0-7687), succinate-semialdehyde dehydrogenase (NADP+) GabD (complex.ecocyc.CPLX0-7688). Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), 5-Oxopentanoate (molecule.C03273). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Glutarate (molecule.C00489).

## Enriched Pathways

- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Annotation

CPD-280 + NADP + WATER -> GLUTARATE + NADPH + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7687|complex.ecocyc.CPLX0-7687]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7688|complex.ecocyc.CPLX0-7688]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00489|molecule.C00489]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03273|molecule.C03273]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8182`

## Notes

CPD-280 + NADP + WATER -> GLUTARATE + NADPH + PROTON; direction=LEFT-TO-RIGHT
