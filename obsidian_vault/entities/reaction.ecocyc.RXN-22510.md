---
entity_id: "reaction.ecocyc.RXN-22510"
entity_type: "reaction"
name: "RXN-22510"
source_database: "EcoCyc"
source_id: "RXN-22510"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22510

`reaction.ecocyc.RXN-22510`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22510`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CPD-24126 + CPD-21359 -> CPD0-2294 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-24126 + CPD-21359 -> CPD0-2294 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaL (protein.P27243). Substrates: lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359), enterobacterial common antigen (molecule.ecocyc.CPD-24126). Products: H+ (molecule.C00080), di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574), enterobacterial common antigen-core oligosaccharide-lipid A (E. coli K-12 core type) (molecule.ecocyc.CPD0-2294).

## Annotation

CPD-24126 + CPD-21359 -> CPD0-2294 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P27243|protein.P27243]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04574|molecule.C04574]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2294|molecule.ecocyc.CPD0-2294]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-24126|molecule.ecocyc.CPD-24126]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22510`

## Notes

CPD-24126 + CPD-21359 -> CPD0-2294 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
