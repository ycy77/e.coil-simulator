---
entity_id: "reaction.ecocyc.RXN1-42"
entity_type: "reaction"
name: "RXN1-42"
source_database: "EcoCyc"
source_id: "RXN1-42"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN1-42

`reaction.ecocyc.RXN1-42`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN1-42`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CPD-650 + Poly-Hydroxybutyrate -> Poly-Hydroxybutyrate + CO-A; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-650 + Poly-Hydroxybutyrate -> Poly-Hydroxybutyrate + CO-A; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ydcS (protein.P76108). Substrates: (R)-3-Hydroxybutanoyl-CoA (molecule.C03561), Poly-beta-hydroxybutyrate (molecule.C06143). Products: CoA (molecule.C00010), Poly-beta-hydroxybutyrate (molecule.C06143).

## Annotation

CPD-650 + Poly-Hydroxybutyrate -> Poly-Hydroxybutyrate + CO-A; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76108|protein.P76108]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06143|molecule.C06143]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03561|molecule.C03561]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06143|molecule.C06143]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN1-42`

## Notes

CPD-650 + Poly-Hydroxybutyrate -> Poly-Hydroxybutyrate + CO-A; direction=LEFT-TO-RIGHT
