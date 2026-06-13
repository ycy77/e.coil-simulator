---
entity_id: "reaction.ecocyc.TRYPSYN-RXN"
entity_type: "reaction"
name: "TRYPSYN-RXN"
source_database: "EcoCyc"
source_id: "TRYPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRYPSYN-RXN

`reaction.ecocyc.TRYPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRYPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

INDOLE-3-GLYCEROL-P + SER -> TRP + WATER + GAP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: INDOLE-3-GLYCEROL-P + SER -> TRP + WATER + GAP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tryptophan synthase (complex.ecocyc.TRYPSYN). Substrates: L-Serine (molecule.C00065), Indoleglycerol phosphate (molecule.C03506). Products: H2O (molecule.C00001), L-Tryptophan (molecule.C00078), D-Glyceraldehyde 3-phosphate (molecule.C00118).

## Annotation

INDOLE-3-GLYCEROL-P + SER -> TRP + WATER + GAP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.TRYPSYN|complex.ecocyc.TRYPSYN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00078|molecule.C00078]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03506|molecule.C03506]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRYPSYN-RXN`

## Notes

INDOLE-3-GLYCEROL-P + SER -> TRP + WATER + GAP; direction=PHYSIOL-LEFT-TO-RIGHT
