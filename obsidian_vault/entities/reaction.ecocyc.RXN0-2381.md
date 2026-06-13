---
entity_id: "reaction.ecocyc.RXN0-2381"
entity_type: "reaction"
name: "RXN0-2381"
source_database: "EcoCyc"
source_id: "RXN0-2381"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2381

`reaction.ecocyc.RXN0-2381`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2381`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

INDOLE-3-GLYCEROL-P -> INDOLE + GAP; direction=REVERSIBLE EcoCyc reaction equation: INDOLE-3-GLYCEROL-P -> INDOLE + GAP; direction=REVERSIBLE.

## Biological Role

Catalyzed by trpA (protein.P0A877). Substrates: Indoleglycerol phosphate (molecule.C03506). Products: D-Glyceraldehyde 3-phosphate (molecule.C00118), Indole (molecule.C00463).

## Enriched Pathways

- `ecocyc.TRPSYN-PWY` L-tryptophan biosynthesis (EcoCyc)

## Annotation

INDOLE-3-GLYCEROL-P -> INDOLE + GAP; direction=REVERSIBLE

## Pathways

- `ecocyc.TRPSYN-PWY` L-tryptophan biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A877|protein.P0A877]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00463|molecule.C00463]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03506|molecule.C03506]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-12164|molecule.ecocyc.CPD-12164]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-2381`

## Notes

INDOLE-3-GLYCEROL-P -> INDOLE + GAP; direction=REVERSIBLE
