---
entity_id: "reaction.ecocyc.DEOXYRIBOSE-P-ALD-RXN"
entity_type: "reaction"
name: "DEOXYRIBOSE-P-ALD-RXN"
source_database: "EcoCyc"
source_id: "DEOXYRIBOSE-P-ALD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DEOXYRIBOSE-P-ALD-RXN

`reaction.ecocyc.DEOXYRIBOSE-P-ALD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DEOXYRIBOSE-P-ALD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of deoxyribonucleotide catabolism. EcoCyc reaction equation: DEOXY-RIBOSE-5P -> ACETALD + GAP; direction=REVERSIBLE. This reaction is part of deoxyribonucleotide catabolism.

## Biological Role

Catalyzed by deoC (protein.P0A6L0). Substrates: 2-Deoxy-D-ribose 5-phosphate (molecule.C00673). Products: Acetaldehyde (molecule.C00084), D-Glyceraldehyde 3-phosphate (molecule.C00118).

## Enriched Pathways

- `ecocyc.PWY-7180` 2-deoxy-α-D-ribose 1-phosphate degradation (EcoCyc)

## Annotation

This reaction is part of deoxyribonucleotide catabolism.

## Pathways

- `ecocyc.PWY-7180` 2-deoxy-α-D-ribose 1-phosphate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A6L0|protein.P0A6L0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00673|molecule.C00673]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00479|molecule.C00479]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1476|molecule.ecocyc.CPD0-1476]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.OCTANOL|molecule.ecocyc.OCTANOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DEOXYRIBOSE-P-ALD-RXN`

## Notes

DEOXY-RIBOSE-5P -> ACETALD + GAP; direction=REVERSIBLE
