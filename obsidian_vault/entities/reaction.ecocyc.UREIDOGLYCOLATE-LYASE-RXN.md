---
entity_id: "reaction.ecocyc.UREIDOGLYCOLATE-LYASE-RXN"
entity_type: "reaction"
name: "UREIDOGLYCOLATE-LYASE-RXN"
source_database: "EcoCyc"
source_id: "UREIDOGLYCOLATE-LYASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UREIDOGLYCOLATE-LYASE-RXN

`reaction.ecocyc.UREIDOGLYCOLATE-LYASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UREIDOGLYCOLATE-LYASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-1091 -> UREA + GLYOX; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-1091 -> UREA + GLYOX; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by allA (protein.P77731). Substrates: (S)-Ureidoglycolate (molecule.C00603). Products: Glyoxylate (molecule.C00048), Urea (molecule.C00086).

## Enriched Pathways

- `ecocyc.PWY-5705` allantoin degradation to glyoxylate III (EcoCyc)

## Annotation

CPD-1091 -> UREA + GLYOX; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5705` allantoin degradation to glyoxylate III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P77731|protein.P77731]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00086|molecule.C00086]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00603|molecule.C00603]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:UREIDOGLYCOLATE-LYASE-RXN`

## Notes

CPD-1091 -> UREA + GLYOX; direction=LEFT-TO-RIGHT
