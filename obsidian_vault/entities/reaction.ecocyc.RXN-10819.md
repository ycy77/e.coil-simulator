---
entity_id: "reaction.ecocyc.RXN-10819"
entity_type: "reaction"
name: "RXN-10819"
source_database: "EcoCyc"
source_id: "RXN-10819"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10819

`reaction.ecocyc.RXN-10819`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10819`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CO-A + PHENYLACETATE + ATP -> CPD-207 + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CO-A + PHENYLACETATE + ATP -> CPD-207 + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by paaK (protein.P76085). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), Phenylacetic acid (molecule.C07086). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), Phenylacetyl-CoA (molecule.C00582).

## Enriched Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Annotation

CO-A + PHENYLACETATE + ATP -> CPD-207 + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P76085|protein.P76085]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00582|molecule.C00582]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C07086|molecule.C07086]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10819`

## Notes

CO-A + PHENYLACETATE + ATP -> CPD-207 + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
