---
entity_id: "reaction.ecocyc.GST-RXN"
entity_type: "reaction"
name: "GST-RXN"
source_database: "EcoCyc"
source_id: "GST-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GST-RXN

`reaction.ecocyc.GST-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GST-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a specific substrate reaction of E.C. 2.5.1.18. EcoCyc reaction equation: 1-CHLORO-24-DINITROBENZENE + GLUTATHIONE -> PROTON + S-24-DINITROPHENYLGLUTATHIONE + CL-; direction=PHYSIOL-LEFT-TO-RIGHT. This is a specific substrate reaction of E.C. 2.5.1.18.

## Biological Role

Catalyzed by glutathione S-transferase YfcF (complex.ecocyc.CPLX0-8573), glutathione S-transferase GstA (complex.ecocyc.GST-CPLX). Substrates: Glutathione (molecule.C00051), 1-chloro-2,4-dinitrobenzene (molecule.ecocyc.1-CHLORO-24-DINITROBENZENE). Products: H+ (molecule.C00080), chloride (molecule.ecocyc.CL-), 2,4-dinitrophenyl-S-glutathione (molecule.ecocyc.S-24-DINITROPHENYLGLUTATHIONE).

## Annotation

This is a specific substrate reaction of E.C. 2.5.1.18.

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8573|complex.ecocyc.CPLX0-8573]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.GST-CPLX|complex.ecocyc.GST-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CL-|molecule.ecocyc.CL-]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.S-24-DINITROPHENYLGLUTATHIONE|molecule.ecocyc.S-24-DINITROPHENYLGLUTATHIONE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.1-CHLORO-24-DINITROBENZENE|molecule.ecocyc.1-CHLORO-24-DINITROBENZENE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1455|molecule.ecocyc.CPD0-1455]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GST-RXN`

## Notes

1-CHLORO-24-DINITROBENZENE + GLUTATHIONE -> PROTON + S-24-DINITROPHENYLGLUTATHIONE + CL-; direction=PHYSIOL-LEFT-TO-RIGHT
