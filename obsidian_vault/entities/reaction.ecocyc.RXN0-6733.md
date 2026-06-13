---
entity_id: "reaction.ecocyc.RXN0-6733"
entity_type: "reaction"
name: "RXN0-6733"
source_database: "EcoCyc"
source_id: "RXN0-6733"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6733

`reaction.ecocyc.RXN0-6733`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6733`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2479 + WATER -> CPD0-2480 + PPI + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2479 + WATER -> CPD0-2480 + PPI + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phnM (protein.P16689). Substrates: H2O (molecule.C00001), alpha-D-Ribose 1-methylphosphonate 5-triphosphate (molecule.C20422). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), alpha-D-Ribose 1-methylphosphonate 5-phosphate (molecule.C20423).

## Enriched Pathways

- `ecocyc.PWY0-1533` methylphosphonate degradation I (EcoCyc)

## Annotation

CPD0-2479 + WATER -> CPD0-2480 + PPI + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1533` methylphosphonate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P16689|protein.P16689]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20423|molecule.C20423]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20422|molecule.C20422]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6733`

## Notes

CPD0-2479 + WATER -> CPD0-2480 + PPI + PROTON; direction=LEFT-TO-RIGHT
