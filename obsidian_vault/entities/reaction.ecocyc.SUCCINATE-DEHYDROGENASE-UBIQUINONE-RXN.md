---
entity_id: "reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN"
entity_type: "reaction"
name: "SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN"
source_database: "EcoCyc"
source_id: "SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "SUCCINIC DEHYDROGENASE"
---

# SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN

`reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Ubiquinones + SUC -> Ubiquinols + FUM; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Ubiquinones + SUC -> Ubiquinols + FUM; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by succinate:quinone oxidoreductase (complex.ecocyc.CPLX0-8160). Substrates: Succinate (molecule.C00042), a ubiquinone (molecule.ecocyc.Ubiquinones). Products: Fumarate (molecule.C00122), Ubiquinol (molecule.C00390).

## Enriched Pathways

- `ecocyc.PWY0-1329` succinate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1353` succinate to cytochrome bd oxidase electron transfer (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Annotation

Ubiquinones + SUC -> Ubiquinols + FUM; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1329` succinate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1353` succinate to cytochrome bd oxidase electron transfer (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8160|complex.ecocyc.CPLX0-8160]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00383|molecule.C00383]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C02575|molecule.C02575]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.2-Alkyl-Dinitrophenol-Derivatives|molecule.ecocyc.2-Alkyl-Dinitrophenol-Derivatives]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1366|molecule.ecocyc.CPD0-1366]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1367|molecule.ecocyc.CPD0-1367]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN`

## Notes

Ubiquinones + SUC -> Ubiquinols + FUM; direction=PHYSIOL-LEFT-TO-RIGHT
