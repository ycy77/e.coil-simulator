---
entity_id: "reaction.ecocyc.GLUTAMINESYN-RXN"
entity_type: "reaction"
name: "GLUTAMINESYN-RXN"
source_database: "EcoCyc"
source_id: "GLUTAMINESYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUTAMINESYN-RXN

`reaction.ecocyc.GLUTAMINESYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTAMINESYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

AMMONIUM + GLT + ATP -> PROTON + GLN + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: AMMONIUM + GLT + ATP -> PROTON + GLN + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glutamine synthetase (complex.ecocyc.GLUTAMINESYN-OLIGOMER). Substrates: ATP (molecule.C00002), L-Glutamate (molecule.C00025), ammonium (molecule.ecocyc.AMMONIUM). Products: ADP (molecule.C00008), L-Glutamine (molecule.C00064), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.AMMASSIM-PWY` ammonia assimilation cycle III (EcoCyc)
- `ecocyc.GLNSYN-PWY` L-glutamine biosynthesis I (EcoCyc)
- `ecocyc.PWY-8291` L-aspartate degradation II (aerobic) (EcoCyc)
- `ecocyc.PWY-8294` L-aspartate degradation III (anaerobic) (EcoCyc)

## Annotation

AMMONIUM + GLT + ATP -> PROTON + GLN + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.AMMASSIM-PWY` ammonia assimilation cycle III (EcoCyc)
- `ecocyc.GLNSYN-PWY` L-glutamine biosynthesis I (EcoCyc)
- `ecocyc.PWY-8291` L-aspartate degradation II (aerobic) (EcoCyc)
- `ecocyc.PWY-8294` L-aspartate degradation III (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (24)

- `catalyzes` <-- [[complex.ecocyc.GLUTAMINESYN-OLIGOMER|complex.ecocyc.GLUTAMINESYN-OLIGOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00078|molecule.C00078]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00135|molecule.C00135]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00169|molecule.C00169]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00352|molecule.C00352]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C04650|molecule.C04650]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9035|molecule.ecocyc.CPD-9035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1245|molecule.ecocyc.CPD0-1245]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1246|molecule.ecocyc.CPD0-1246]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1248|molecule.ecocyc.CPD0-1248]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1249|molecule.ecocyc.CPD0-1249]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1650|molecule.ecocyc.CPD0-1650]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUTAMINESYN-RXN`

## Notes

AMMONIUM + GLT + ATP -> PROTON + GLN + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
