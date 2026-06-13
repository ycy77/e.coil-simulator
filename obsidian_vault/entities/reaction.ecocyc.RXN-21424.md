---
entity_id: "reaction.ecocyc.RXN-21424"
entity_type: "reaction"
name: "RXN-21424"
source_database: "EcoCyc"
source_id: "RXN-21424"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21424

`reaction.ecocyc.RXN-21424`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21424`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Reduced-CcmG-Proteins + CytC-CcmH-Heme-CcmE + ETR-Quinols -> CcmH-CcmG + Cytochromes-c + CcmE-Proteins + ETR-Semiquinones + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Reduced-CcmG-Proteins + CytC-CcmH-Heme-CcmE + ETR-Quinols -> CcmH-CcmG + Cytochromes-c + CcmE-Proteins + ETR-Semiquinones + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dsbE (protein.P0AA86). Products: H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-8147` cytochrome c biogenesis (system I type) (EcoCyc)

## Annotation

Reduced-CcmG-Proteins + CytC-CcmH-Heme-CcmE + ETR-Quinols -> CcmH-CcmG + Cytochromes-c + CcmE-Proteins + ETR-Semiquinones + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8147` cytochrome c biogenesis (system I type) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P0AA86|protein.P0AA86]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:RXN-21424`

## Notes

Reduced-CcmG-Proteins + CytC-CcmH-Heme-CcmE + ETR-Quinols -> CcmH-CcmG + Cytochromes-c + CcmE-Proteins + ETR-Semiquinones + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
