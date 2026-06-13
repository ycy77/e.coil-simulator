---
entity_id: "reaction.ecocyc.RXN0-6371"
entity_type: "reaction"
name: "RXN0-6371"
source_database: "EcoCyc"
source_id: "RXN0-6371"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6371

`reaction.ecocyc.RXN0-6371`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6371`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

Aldoses + Acceptor + WATER -> Aldonic-Acids + Donor-H2 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Aldoses + Acceptor + WATER -> Aldonic-Acids + Donor-H2 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yliI (protein.P75804). Substrates: H2O (molecule.C00001), an aldose (molecule.ecocyc.Aldoses). Products: H+ (molecule.C00080), an aldonate (molecule.ecocyc.Aldonic-Acids).

## Annotation

Aldoses + Acceptor + WATER -> Aldonic-Acids + Donor-H2 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75804|protein.P75804]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Aldonic-Acids|molecule.ecocyc.Aldonic-Acids]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Aldoses|molecule.ecocyc.Aldoses]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6371`

## Notes

Aldoses + Acceptor + WATER -> Aldonic-Acids + Donor-H2 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
