---
entity_id: "reaction.ecocyc.ADPSUGPPHOSPHAT-RXN"
entity_type: "reaction"
name: "ADPSUGPPHOSPHAT-RXN"
source_database: "EcoCyc"
source_id: "ADPSUGPPHOSPHAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADPSUGPPHOSPHAT-RXN

`reaction.ecocyc.ADPSUGPPHOSPHAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADPSUGPPHOSPHAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is a part of the breakdown of ADP-sugars. EcoCyc reaction equation: ADP-SUGARS + WATER -> AMP + Alpha-D-aldose-1-phosphates + PROTON; direction=LEFT-TO-RIGHT. This reaction is a part of the breakdown of ADP-sugars.

## Biological Role

Catalyzed by ADP-sugar diphosphatase NudE (complex.ecocyc.CPLX0-1221), ADP-sugar pyrophosphatase (complex.ecocyc.CPLX0-3721). Substrates: H2O (molecule.C00001), an ADP-sugar (molecule.ecocyc.ADP-SUGARS). Products: AMP (molecule.C00020), H+ (molecule.C00080), an α-D-aldose 1-phosphate (molecule.ecocyc.Alpha-D-aldose-1-phosphates).

## Annotation

This reaction is a part of the breakdown of ADP-sugars.

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.GLUCOSE-16-DIPHOSPHATE|molecule.ecocyc.GLUCOSE-16-DIPHOSPHATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-1221|complex.ecocyc.CPLX0-1221]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3721|complex.ecocyc.CPLX0-3721]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Alpha-D-aldose-1-phosphates|molecule.ecocyc.Alpha-D-aldose-1-phosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.ADP-SUGARS|molecule.ecocyc.ADP-SUGARS]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ADPSUGPPHOSPHAT-RXN`

## Notes

ADP-SUGARS + WATER -> AMP + Alpha-D-aldose-1-phosphates + PROTON; direction=LEFT-TO-RIGHT
