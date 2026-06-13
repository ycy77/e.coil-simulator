---
entity_id: "reaction.ecocyc.RXN0-299"
entity_type: "reaction"
name: "RXN0-299"
source_database: "EcoCyc"
source_id: "RXN0-299"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-299

`reaction.ecocyc.RXN0-299`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-299`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TAURINE + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> PROTON + CPD-1772 + SO3 + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TAURINE + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> PROTON + CPD-1772 + SO3 + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by α-ketoglutarate-dependent taurine dioxygenase (complex.ecocyc.CPLX0-227). Substrates: Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), Taurine (molecule.C00245). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), H+ (molecule.C00080), Sulfite (molecule.C00094), Aminoacetaldehyde (molecule.C06735).

## Enriched Pathways

- `ecocyc.PWY0-981` taurine degradation IV (EcoCyc)

## Annotation

TAURINE + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> PROTON + CPD-1772 + SO3 + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-981` taurine degradation IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (16)

- `activates` <-- [[molecule.C00072|molecule.C00072]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-227|complex.ecocyc.CPLX0-227]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06735|molecule.C06735]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00245|molecule.C00245]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-20893|molecule.ecocyc.CPD-20893]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-299`

## Notes

TAURINE + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> PROTON + CPD-1772 + SO3 + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
