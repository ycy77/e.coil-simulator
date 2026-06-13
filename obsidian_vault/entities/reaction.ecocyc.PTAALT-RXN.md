---
entity_id: "reaction.ecocyc.PTAALT-RXN"
entity_type: "reaction"
name: "PTAALT-RXN"
source_database: "EcoCyc"
source_id: "PTAALT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PTAALT-RXN

`reaction.ecocyc.PTAALT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PTAALT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is an alternative substrate reaction of E.C. 2.3.1.8. EcoCyc reaction equation: PROPIONYL-COA + Pi -> PROPIONYL-P + CO-A; direction=LEFT-TO-RIGHT. This is an alternative substrate reaction of E.C. 2.3.1.8.

## Biological Role

Catalyzed by phosphate acetyltransferase (complex.ecocyc.PHOSACETYLTRANS-CPLX). Substrates: Propanoyl-CoA (molecule.C00100), phosphate (molecule.ecocyc.Pi). Products: CoA (molecule.C00010), Propanoyl phosphate (molecule.C02876).

## Enriched Pathways

- `ecocyc.PWY-5437` L-threonine degradation I (EcoCyc)

## Annotation

This is an alternative substrate reaction of E.C. 2.3.1.8.

## Pathways

- `ecocyc.PWY-5437` L-threonine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.PHOSACETYLTRANS-CPLX|complex.ecocyc.PHOSACETYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02876|molecule.C02876]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00100|molecule.C00100]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PTAALT-RXN`

## Notes

PROPIONYL-COA + Pi -> PROPIONYL-P + CO-A; direction=LEFT-TO-RIGHT
