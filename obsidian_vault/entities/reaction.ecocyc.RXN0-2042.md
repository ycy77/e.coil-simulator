---
entity_id: "reaction.ecocyc.RXN0-2042"
entity_type: "reaction"
name: "RXN0-2042"
source_database: "EcoCyc"
source_id: "RXN0-2042"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2042

`reaction.ecocyc.RXN0-2042`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2042`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-207 + OXYGEN-MOLECULE + NADPH + PROTON -> CPD0-2362 + NADP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-207 + OXYGEN-MOLECULE + NADPH + PROTON -> CPD0-2362 + NADP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phenylacetyl-CoA 1,2-epoxidase (complex.ecocyc.CPLX0-1762). Substrates: NADPH (molecule.C00005), Oxygen (molecule.C00007), H+ (molecule.C00080), Phenylacetyl-CoA (molecule.C00582). Products: H2O (molecule.C00001), NADP+ (molecule.C00006), 2-(1,2-Epoxy-1,2-dihydrophenyl)acetyl-CoA (molecule.C20062).

## Enriched Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Annotation

CPD-207 + OXYGEN-MOLECULE + NADPH + PROTON -> CPD0-2362 + NADP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1762|complex.ecocyc.CPLX0-1762]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20062|molecule.C20062]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00582|molecule.C00582]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2042`

## Notes

CPD-207 + OXYGEN-MOLECULE + NADPH + PROTON -> CPD0-2362 + NADP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
