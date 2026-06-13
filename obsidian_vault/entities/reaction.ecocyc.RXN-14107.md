---
entity_id: "reaction.ecocyc.RXN-14107"
entity_type: "reaction"
name: "menaquinol-cytochrome c reductase"
source_database: "EcoCyc"
source_id: "RXN-14107"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "menaquinone:cytochrome c reductase"
---

# menaquinol-cytochrome c reductase

`reaction.ecocyc.RXN-14107`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14107`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Menaquinols + Cytochromes-C-Oxidized + PROTON -> Menaquinones + Cytochromes-C-Reduced + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Menaquinols + Cytochromes-C-Oxidized + PROTON -> Menaquinones + Cytochromes-C-Reduced + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Menaquinol (molecule.C05819). Products: H+ (molecule.C00080), Menaquinone (molecule.C00828).

## Annotation

Menaquinols + Cytochromes-C-Oxidized + PROTON -> Menaquinones + Cytochromes-C-Reduced + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14107`

## Notes

Menaquinols + Cytochromes-C-Oxidized + PROTON -> Menaquinones + Cytochromes-C-Reduced + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
