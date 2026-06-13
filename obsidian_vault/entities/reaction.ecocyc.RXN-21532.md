---
entity_id: "reaction.ecocyc.RXN-21532"
entity_type: "reaction"
name: "RXN-21532"
source_database: "EcoCyc"
source_id: "RXN-21532"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21532

`reaction.ecocyc.RXN-21532`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21532`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-23690 -> DIHYDROXY-ACETONE-PHOSPHATE + CPD-23427; direction=REVERSIBLE EcoCyc reaction equation: CPD-23690 -> DIHYDROXY-ACETONE-PHOSPHATE + CPD-23427; direction=REVERSIBLE.

## Biological Role

Catalyzed by L-glycero-L-galacto-octuluronate-1-phosphate aldolase (complex.ecocyc.CPLX0-8547). Substrates: L-glycero-L-galacto-octuluronate-1-phosphate (molecule.ecocyc.CPD-23690). Products: Glycerone phosphate (molecule.C00111), aldehydo-L-arabinuronate (molecule.ecocyc.CPD-23427).

## Annotation

CPD-23690 -> DIHYDROXY-ACETONE-PHOSPHATE + CPD-23427; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8547|complex.ecocyc.CPLX0-8547]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-23427|molecule.ecocyc.CPD-23427]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-23690|molecule.ecocyc.CPD-23690]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21532`

## Notes

CPD-23690 -> DIHYDROXY-ACETONE-PHOSPHATE + CPD-23427; direction=REVERSIBLE
