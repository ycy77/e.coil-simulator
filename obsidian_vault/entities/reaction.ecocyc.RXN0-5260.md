---
entity_id: "reaction.ecocyc.RXN0-5260"
entity_type: "reaction"
name: "sn-glycerol 3-phosphate:ubiquinone oxidoreductase"
source_database: "EcoCyc"
source_id: "RXN0-5260"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# sn-glycerol 3-phosphate:ubiquinone oxidoreductase

`reaction.ecocyc.RXN0-5260`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5260`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Ubiquinones + GLYCEROL-3P -> Ubiquinols + DIHYDROXY-ACETONE-PHOSPHATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Ubiquinones + GLYCEROL-3P -> Ubiquinols + DIHYDROXY-ACETONE-PHOSPHATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aerobic glycerol 3-phosphate dehydrogenase (complex.ecocyc.AERGLYC3PDEHYDROG-CPLX). Substrates: sn-Glycerol 3-phosphate (molecule.C00093), a ubiquinone (molecule.ecocyc.Ubiquinones). Products: Glycerone phosphate (molecule.C00111), Ubiquinol (molecule.C00390).

## Enriched Pathways

- `ecocyc.PWY-4261` glycerol degradation I (EcoCyc)
- `ecocyc.PWY-6952` glycerophosphodiester degradation (EcoCyc)
- `ecocyc.PWY0-1561` glycerol-3-phosphate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1584` sn-glycerol 3-phosphate anaerobic respiration (EcoCyc)

## Annotation

Ubiquinones + GLYCEROL-3P -> Ubiquinols + DIHYDROXY-ACETONE-PHOSPHATE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-4261` glycerol degradation I (EcoCyc)
- `ecocyc.PWY-6952` glycerophosphodiester degradation (EcoCyc)
- `ecocyc.PWY0-1561` glycerol-3-phosphate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1584` sn-glycerol 3-phosphate anaerobic respiration (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `activates` <-- [[protein.C1P605|protein.C1P605]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.AERGLYC3PDEHYDROG-CPLX|complex.ecocyc.AERGLYC3PDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00197|molecule.C00197]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00631|molecule.C00631]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00988|molecule.C00988]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5260`

## Notes

Ubiquinones + GLYCEROL-3P -> Ubiquinols + DIHYDROXY-ACETONE-PHOSPHATE; direction=LEFT-TO-RIGHT
