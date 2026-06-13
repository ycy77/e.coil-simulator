---
entity_id: "reaction.ecocyc.RXN0-6676"
entity_type: "reaction"
name: "RXN0-6676"
source_database: "EcoCyc"
source_id: "RXN0-6676"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6676

`reaction.ecocyc.RXN0-6676`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6676`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-6602 + NADPH + PROTON -> CPD-13314 + NADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-6602 + NADPH + PROTON -> CPD-13314 + NADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by NADPH-dependent curcumin/dihydrocurcumin reductase (complex.ecocyc.CPLX0-7927). Substrates: NADPH (molecule.C00005), H+ (molecule.C00080), curcumin (molecule.ecocyc.CPD-6602). Products: NADP+ (molecule.C00006), dihydrocurcumin (molecule.ecocyc.CPD-13314).

## Enriched Pathways

- `ecocyc.PWY0-1527` curcumin degradation (EcoCyc)

## Annotation

CPD-6602 + NADPH + PROTON -> CPD-13314 + NADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1527` curcumin degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (17)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7927|complex.ecocyc.CPLX0-7927]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-13314|molecule.ecocyc.CPD-13314]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-6602|molecule.ecocyc.CPD-6602]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.AG|molecule.ecocyc.AG_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5541|molecule.ecocyc.CPD-5541]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIISOPROPYL-FLUOROPHOSPHATE|molecule.ecocyc.DIISOPROPYL-FLUOROPHOSPHATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETATE|molecule.ecocyc.IODOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-6676`

## Notes

CPD-6602 + NADPH + PROTON -> CPD-13314 + NADP; direction=LEFT-TO-RIGHT
