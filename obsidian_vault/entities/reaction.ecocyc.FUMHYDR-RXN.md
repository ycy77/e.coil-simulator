---
entity_id: "reaction.ecocyc.FUMHYDR-RXN"
entity_type: "reaction"
name: "FUMHYDR-RXN"
source_database: "EcoCyc"
source_id: "FUMHYDR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "malate dehydration"
---

# FUMHYDR-RXN

`reaction.ecocyc.FUMHYDR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FUMHYDR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MAL -> FUM + WATER; direction=REVERSIBLE EcoCyc reaction equation: MAL -> FUM + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by fumarase A (complex.ecocyc.FUMARASE-A), fumarase B (complex.ecocyc.FUMARASE-B), fumarase C (complex.ecocyc.FUMARASE-C), fumD (protein.P0ACX5), fumE (protein.P11663). Substrates: (S)-Malate (molecule.C00149). Products: H2O (molecule.C00001), Fumarate (molecule.C00122).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Annotation

MAL -> FUM + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (16)

- `catalyzes` <-- [[complex.ecocyc.FUMARASE-A|complex.ecocyc.FUMARASE-A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.FUMARASE-B|complex.ecocyc.FUMARASE-B]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.FUMARASE-C|complex.ecocyc.FUMARASE-C]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ACX5|protein.P0ACX5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P11663|protein.P11663]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C20679|molecule.C20679]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.AG|molecule.ecocyc.AG_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2489|molecule.ecocyc.CPD0-2489]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.SUPER-OXIDE|molecule.ecocyc.SUPER-OXIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:FUMHYDR-RXN`

## Notes

MAL -> FUM + WATER; direction=REVERSIBLE
