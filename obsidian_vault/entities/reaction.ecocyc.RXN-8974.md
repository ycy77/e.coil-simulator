---
entity_id: "reaction.ecocyc.RXN-8974"
entity_type: "reaction"
name: "RXN-8974"
source_database: "EcoCyc"
source_id: "RXN-8974"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8974

`reaction.ecocyc.RXN-8974`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8974`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-HYDROXY-PROPIONATE + NADP -> MALONATE-S-ALD + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: 3-HYDROXY-PROPIONATE + NADP -> MALONATE-S-ALD + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by 3-hydroxy acid dehydrogenase YdfG (complex.ecocyc.CPLX0-1962), rutE (protein.P75894). Substrates: NADP+ (molecule.C00006), 3-Hydroxypropanoate (molecule.C01013). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 3-Oxopropanoate (molecule.C00222).

## Enriched Pathways

- `ecocyc.PWY0-1471` uracil degradation III (EcoCyc)

## Annotation

3-HYDROXY-PROPIONATE + NADP -> MALONATE-S-ALD + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY0-1471` uracil degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1962|complex.ecocyc.CPLX0-1962]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75894|protein.P75894]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00222|molecule.C00222]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01013|molecule.C01013]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8974`

## Notes

3-HYDROXY-PROPIONATE + NADP -> MALONATE-S-ALD + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
