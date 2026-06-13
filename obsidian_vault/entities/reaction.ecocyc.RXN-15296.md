---
entity_id: "reaction.ecocyc.RXN-15296"
entity_type: "reaction"
name: "RXN-15296"
source_database: "EcoCyc"
source_id: "RXN-15296"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15296

`reaction.ecocyc.RXN-15296`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15296`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-21686 -> CPD-16501; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-21686 -> CPD-16501; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by sulfoquinovose isomerase (complex.ecocyc.CPLX0-7683). Substrates: 6-sulfo-β-D-quinovose (molecule.ecocyc.CPD-21686). Products: 6-Deoxy-6-sulfo-D-fructose (molecule.C20830).

## Enriched Pathways

- `ecocyc.PWY-7446` sulfoquinovose degradation I (EcoCyc)

## Annotation

CPD-21686 -> CPD-16501; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7446` sulfoquinovose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7683|complex.ecocyc.CPLX0-7683]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C20830|molecule.C20830]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21686|molecule.ecocyc.CPD-21686]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15296`

## Notes

CPD-21686 -> CPD-16501; direction=LEFT-TO-RIGHT
