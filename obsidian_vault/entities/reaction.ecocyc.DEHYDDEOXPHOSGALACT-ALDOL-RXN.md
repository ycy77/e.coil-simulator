---
entity_id: "reaction.ecocyc.DEHYDDEOXPHOSGALACT-ALDOL-RXN"
entity_type: "reaction"
name: "DEHYDDEOXPHOSGALACT-ALDOL-RXN"
source_database: "EcoCyc"
source_id: "DEHYDDEOXPHOSGALACT-ALDOL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DEHYDDEOXPHOSGALACT-ALDOL-RXN

`reaction.ecocyc.DEHYDDEOXPHOSGALACT-ALDOL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DEHYDDEOXPHOSGALACT-ALDOL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The third step of galactonate catabolism. EcoCyc reaction equation: DEHYDRO-DEOXY-GALACTONATE-PHOSPHATE -> GAP + PYRUVATE; direction=REVERSIBLE. The third step of galactonate catabolism.

## Biological Role

Catalyzed by dgoA (protein.Q6BF16). Substrates: 2-Dehydro-3-deoxy-6-phospho-D-galactonate (molecule.C01286). Products: Pyruvate (molecule.C00022), D-Glyceraldehyde 3-phosphate (molecule.C00118).

## Enriched Pathways

- `ecocyc.GALACTCAT-PWY` D-galactonate degradation (EcoCyc)

## Annotation

The third step of galactonate catabolism.

## Pathways

- `ecocyc.GALACTCAT-PWY` D-galactonate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.Q6BF16|protein.Q6BF16]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01286|molecule.C01286]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DEHYDDEOXPHOSGALACT-ALDOL-RXN`

## Notes

DEHYDRO-DEOXY-GALACTONATE-PHOSPHATE -> GAP + PYRUVATE; direction=REVERSIBLE
