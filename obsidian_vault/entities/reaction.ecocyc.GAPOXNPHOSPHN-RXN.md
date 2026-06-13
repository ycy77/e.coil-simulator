---
entity_id: "reaction.ecocyc.GAPOXNPHOSPHN-RXN"
entity_type: "reaction"
name: "GAPOXNPHOSPHN-RXN"
source_database: "EcoCyc"
source_id: "GAPOXNPHOSPHN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "GAPDH"
  - "TRIOSEPHOSPHATE DEHYDROGENASE"
---

# GAPOXNPHOSPHN-RXN

`reaction.ecocyc.GAPOXNPHOSPHN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GAPOXNPHOSPHN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GAP + Pi + NAD -> PROTON + DPG + NADH; direction=REVERSIBLE EcoCyc reaction equation: GAP + Pi + NAD -> PROTON + DPG + NADH; direction=REVERSIBLE.

## Biological Role

Catalyzed by glyceraldehyde-3-phosphate dehydrogenase (complex.ecocyc.GAPDH-A-CPLX). Substrates: NAD+ (molecule.C00003), D-Glyceraldehyde 3-phosphate (molecule.C00118), phosphate (molecule.ecocyc.Pi). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-Phospho-D-glyceroyl phosphate (molecule.C00236).

## Enriched Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Annotation

GAP + Pi + NAD -> PROTON + DPG + NADH; direction=REVERSIBLE

## Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.ecocyc.ARSENATE|molecule.ecocyc.ARSENATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.GAPDH-A-CPLX|complex.ecocyc.GAPDH-A-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00236|molecule.C00236]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.IODOACETATE|molecule.ecocyc.IODOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GAPOXNPHOSPHN-RXN`

## Notes

GAP + Pi + NAD -> PROTON + DPG + NADH; direction=REVERSIBLE
