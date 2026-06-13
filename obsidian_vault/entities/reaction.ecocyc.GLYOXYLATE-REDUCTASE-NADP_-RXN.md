---
entity_id: "reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN"
entity_type: "reaction"
name: "GLYOXYLATE-REDUCTASE-NADP+-RXN"
source_database: "EcoCyc"
source_id: "GLYOXYLATE-REDUCTASE-NADP+-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYOXYLATE-REDUCTASE-NADP+-RXN

`reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYOXYLATE-REDUCTASE-NADP+-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLYCOLLATE + NADP -> PROTON + NADPH + GLYOX; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: GLYCOLLATE + NADP -> PROTON + NADPH + GLYOX; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by glyoxylate reductase [multifunctional] (complex.ecocyc.CPLX0-235), ghrA (protein.P75913). Substrates: NADP+ (molecule.C00006), Glycolate (molecule.C00160). Products: NADPH (molecule.C00005), Glyoxylate (molecule.C00048), H+ (molecule.C00080).

## Annotation

GLYCOLLATE + NADP -> PROTON + NADPH + GLYOX; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-235|complex.ecocyc.CPLX0-235]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75913|protein.P75913]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLYOXYLATE-REDUCTASE-NADP+-RXN`

## Notes

GLYCOLLATE + NADP -> PROTON + NADPH + GLYOX; direction=PHYSIOL-RIGHT-TO-LEFT
