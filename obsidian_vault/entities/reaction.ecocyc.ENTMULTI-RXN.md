---
entity_id: "reaction.ecocyc.ENTMULTI-RXN"
entity_type: "reaction"
name: "ENTMULTI-RXN"
source_database: "EcoCyc"
source_id: "ENTMULTI-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ENTMULTI-RXN

`reaction.ecocyc.ENTMULTI-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ENTMULTI-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + SER + 2-3-DIHYDROXYBENZOATE -> PROTON + PPI + AMP + ENTEROBACTIN; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + SER + 2-3-DIHYDROXYBENZOATE -> PROTON + PPI + AMP + ENTEROBACTIN; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by enterobactin synthase (complex.ecocyc.ENTMULTI-CPLX). Substrates: ATP (molecule.C00002), L-Serine (molecule.C00065), 2,3-Dihydroxybenzoate (molecule.C00196). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), Enterochelin (molecule.C05821).

## Annotation

ATP + SER + 2-3-DIHYDROXYBENZOATE -> PROTON + PPI + AMP + ENTEROBACTIN; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ENTMULTI-CPLX|complex.ecocyc.ENTMULTI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05821|molecule.C05821]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00196|molecule.C00196]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ENTMULTI-RXN`

## Notes

ATP + SER + 2-3-DIHYDROXYBENZOATE -> PROTON + PPI + AMP + ENTEROBACTIN; direction=PHYSIOL-LEFT-TO-RIGHT
