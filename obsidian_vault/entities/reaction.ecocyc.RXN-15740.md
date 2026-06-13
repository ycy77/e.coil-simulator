---
entity_id: "reaction.ecocyc.RXN-15740"
entity_type: "reaction"
name: "RXN-15740"
source_database: "EcoCyc"
source_id: "RXN-15740"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15740

`reaction.ecocyc.RXN-15740`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15740`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Menaquinones + GLYCEROL-3P -> Menaquinols + DIHYDROXY-ACETONE-PHOSPHATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Menaquinones + GLYCEROL-3P -> Menaquinols + DIHYDROXY-ACETONE-PHOSPHATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by anaerobic glycerol-3-phosphate dehydrogenase (complex.ecocyc.ANGLYC3PDEHYDROG-CPLX). Substrates: sn-Glycerol 3-phosphate (molecule.C00093), Menaquinone (molecule.C00828). Products: Glycerone phosphate (molecule.C00111), Menaquinol (molecule.C05819).

## Enriched Pathways

- `ecocyc.PWY-4261` glycerol degradation I (EcoCyc)
- `ecocyc.PWY-6952` glycerophosphodiester degradation (EcoCyc)
- `ecocyc.PWY0-1581` nitrate reduction IX (dissimilatory) (EcoCyc)
- `ecocyc.PWY0-1582` glycerol-3-phosphate to fumarate electron transfer (EcoCyc)
- `ecocyc.PWY0-1591` glycerol-3-phosphate to hydrogen peroxide electron transport (EcoCyc)

## Annotation

Menaquinones + GLYCEROL-3P -> Menaquinols + DIHYDROXY-ACETONE-PHOSPHATE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-4261` glycerol degradation I (EcoCyc)
- `ecocyc.PWY-6952` glycerophosphodiester degradation (EcoCyc)
- `ecocyc.PWY0-1581` nitrate reduction IX (dissimilatory) (EcoCyc)
- `ecocyc.PWY0-1582` glycerol-3-phosphate to fumarate electron transfer (EcoCyc)
- `ecocyc.PWY0-1591` glycerol-3-phosphate to hydrogen peroxide electron transport (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.ANGLYC3PDEHYDROG-CPLX|complex.ecocyc.ANGLYC3PDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-5401|molecule.ecocyc.CPD-5401]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-15740`

## Notes

Menaquinones + GLYCEROL-3P -> Menaquinols + DIHYDROXY-ACETONE-PHOSPHATE; direction=LEFT-TO-RIGHT
