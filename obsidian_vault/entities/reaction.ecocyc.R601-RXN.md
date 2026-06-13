---
entity_id: "reaction.ecocyc.R601-RXN"
entity_type: "reaction"
name: "R601-RXN"
source_database: "EcoCyc"
source_id: "R601-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# R601-RXN

`reaction.ecocyc.R601-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:R601-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Menaquinols + FUM -> Menaquinones + SUC; direction=REVERSIBLE EcoCyc reaction equation: Menaquinols + FUM -> Menaquinones + SUC; direction=REVERSIBLE.

## Biological Role

Catalyzed by fumarate reductase (complex.ecocyc.FUMARATE-REDUCTASE). Substrates: Fumarate (molecule.C00122), Menaquinol (molecule.C05819). Products: Succinate (molecule.C00042), Menaquinone (molecule.C00828).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY0-1336` NADH to fumarate electron transfer (EcoCyc)
- `ecocyc.PWY0-1576` hydrogen to fumarate electron transfer (EcoCyc)
- `ecocyc.PWY0-1582` glycerol-3-phosphate to fumarate electron transfer (EcoCyc)

## Annotation

Menaquinols + FUM -> Menaquinones + SUC; direction=REVERSIBLE

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY0-1336` NADH to fumarate electron transfer (EcoCyc)
- `ecocyc.PWY0-1576` hydrogen to fumarate electron transfer (EcoCyc)
- `ecocyc.PWY0-1582` glycerol-3-phosphate to fumarate electron transfer (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.FUMARATE-REDUCTASE|complex.ecocyc.FUMARATE-REDUCTASE]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00383|molecule.C00383]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C02575|molecule.C02575]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.2-Alkyl-Dinitrophenol-Derivatives|molecule.ecocyc.2-Alkyl-Dinitrophenol-Derivatives]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7975|molecule.ecocyc.CPD-7975]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Ubiquinol-Analogues|molecule.ecocyc.Ubiquinol-Analogues]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:R601-RXN`

## Notes

Menaquinols + FUM -> Menaquinones + SUC; direction=REVERSIBLE
