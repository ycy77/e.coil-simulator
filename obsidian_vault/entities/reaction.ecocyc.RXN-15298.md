---
entity_id: "reaction.ecocyc.RXN-15298"
entity_type: "reaction"
name: "RXN-15298"
source_database: "EcoCyc"
source_id: "RXN-15298"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15298

`reaction.ecocyc.RXN-15298`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15298`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-16502 -> CPD-18718 + DIHYDROXY-ACETONE-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-16502 -> CPD-18718 + DIHYDROXY-ACETONE-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yihT (protein.P32141). Substrates: 6-Deoxy-6-sulfo-D-fructose 1-phosphate (molecule.C20831). Products: Glycerone phosphate (molecule.C00111), (2S)-3-Sulfolactaldehyde (molecule.C21181).

## Enriched Pathways

- `ecocyc.PWY-7446` sulfoquinovose degradation I (EcoCyc)

## Annotation

CPD-16502 -> CPD-18718 + DIHYDROXY-ACETONE-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7446` sulfoquinovose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P32141|protein.P32141]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C21181|molecule.C21181]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C20831|molecule.C20831]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15298`

## Notes

CPD-16502 -> CPD-18718 + DIHYDROXY-ACETONE-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT
