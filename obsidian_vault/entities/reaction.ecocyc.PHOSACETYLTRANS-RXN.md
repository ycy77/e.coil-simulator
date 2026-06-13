---
entity_id: "reaction.ecocyc.PHOSACETYLTRANS-RXN"
entity_type: "reaction"
name: "PHOSACETYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "PHOSACETYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Phosphoacylase"
  - "Phosphotransacetylase"
---

# PHOSACETYLTRANS-RXN

`reaction.ecocyc.PHOSACETYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOSACETYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first reaction in the conversion of acetyl-CoA to acetate. EcoCyc reaction equation: Pi + ACETYL-COA -> ACETYL-P + CO-A; direction=REVERSIBLE. The first reaction in the conversion of acetyl-CoA to acetate.

## Biological Role

Catalyzed by phosphate acetyltransferase EutD (complex.ecocyc.CPLX0-7912), phosphate acetyltransferase (complex.ecocyc.PHOSACETYLTRANS-CPLX). Substrates: Acetyl-CoA (molecule.C00024), phosphate (molecule.ecocyc.Pi). Products: CoA (molecule.C00010), Acetyl phosphate (molecule.C00227).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-5485` pyruvate fermentation to acetate IV (EcoCyc)
- `ecocyc.PWY0-1312` acetate and ATP formation from acetyl-CoA I (EcoCyc)
- `ecocyc.PWY0-1477` ethanolamine utilization (EcoCyc)

## Annotation

The first reaction in the conversion of acetyl-CoA to acetate.

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-5485` pyruvate fermentation to acetate IV (EcoCyc)
- `ecocyc.PWY0-1312` acetate and ATP formation from acetyl-CoA I (EcoCyc)
- `ecocyc.PWY0-1477` ethanolamine utilization (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `activates` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7912|complex.ecocyc.CPLX0-7912]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.PHOSACETYLTRANS-CPLX|complex.ecocyc.PHOSACETYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00227|molecule.C00227]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PHOSACETYLTRANS-RXN`

## Notes

Pi + ACETYL-COA -> ACETYL-P + CO-A; direction=REVERSIBLE
