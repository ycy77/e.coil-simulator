---
entity_id: "reaction.ecocyc.1.1.1.271-RXN"
entity_type: "reaction"
name: "1.1.1.271-RXN"
source_database: "EcoCyc"
source_id: "1.1.1.271-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "GDP-4-keto-6-deoxy-D-mannose-3,5-epimerase-4-reductase"
---

# 1.1.1.271-RXN

`reaction.ecocyc.1.1.1.271-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.1.1.271-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-13118 + NADP -> PROTON + NADPH + GDP-4-DEHYDRO-6-DEOXY-D-MANNOSE; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: CPD-13118 + NADP -> PROTON + NADPH + GDP-4-DEHYDRO-6-DEOXY-D-MANNOSE; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by GDP-L-fucose synthase (complex.ecocyc.CPLX0-3881). Substrates: NADP+ (molecule.C00006), GDP-L-fucose (molecule.C00325). Products: NADPH (molecule.C00005), H+ (molecule.C00080), GDP-4-dehydro-6-deoxy-D-mannose (molecule.C01222).

## Annotation

CPD-13118 + NADP -> PROTON + NADPH + GDP-4-DEHYDRO-6-DEOXY-D-MANNOSE; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3881|complex.ecocyc.CPLX0-3881]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01222|molecule.C01222]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00325|molecule.C00325]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00325|molecule.C00325]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:1.1.1.271-RXN`

## Notes

CPD-13118 + NADP -> PROTON + NADPH + GDP-4-DEHYDRO-6-DEOXY-D-MANNOSE; direction=PHYSIOL-RIGHT-TO-LEFT
