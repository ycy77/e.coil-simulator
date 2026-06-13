---
entity_id: "reaction.ecocyc.GLYC3PDEHYDROGBIOSYN-RXN"
entity_type: "reaction"
name: "GLYC3PDEHYDROGBIOSYN-RXN"
source_database: "EcoCyc"
source_id: "GLYC3PDEHYDROGBIOSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYC3PDEHYDROGBIOSYN-RXN

`reaction.ecocyc.GLYC3PDEHYDROGBIOSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYC3PDEHYDROGBIOSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in the biosynthesis of phospholipids. EcoCyc reaction equation: NAD-P-OR-NOP + GLYCEROL-3P -> NADH-P-OR-NOP + DIHYDROXY-ACETONE-PHOSPHATE + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction is involved in the biosynthesis of phospholipids.

## Biological Role

Catalyzed by glycerol-3-phosphate dehydrogenase, biosynthetic (complex.ecocyc.GLYC3PDEHYDROGBIOSYN-CPLX). Substrates: sn-Glycerol 3-phosphate (molecule.C00093), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), Glycerone phosphate (molecule.C00111), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Enriched Pathways

- `ecocyc.PWY-5667` CDP-diacylglycerol biosynthesis I (EcoCyc)
- `ecocyc.PWY0-1319` CDP-diacylglycerol biosynthesis II (EcoCyc)

## Annotation

This reaction is involved in the biosynthesis of phospholipids.

## Pathways

- `ecocyc.PWY-5667` CDP-diacylglycerol biosynthesis I (EcoCyc)
- `ecocyc.PWY0-1319` CDP-diacylglycerol biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.GLYC3PDEHYDROGBIOSYN-CPLX|complex.ecocyc.GLYC3PDEHYDROGBIOSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00154|molecule.C00154]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C02843|molecule.C02843]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYC3PDEHYDROGBIOSYN-RXN`

## Notes

NAD-P-OR-NOP + GLYCEROL-3P -> NADH-P-OR-NOP + DIHYDROXY-ACETONE-PHOSPHATE + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
