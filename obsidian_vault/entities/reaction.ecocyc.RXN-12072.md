---
entity_id: "reaction.ecocyc.RXN-12072"
entity_type: "reaction"
name: "RXN-12072"
source_database: "EcoCyc"
source_id: "RXN-12072"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12072

`reaction.ecocyc.RXN-12072`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12072`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-674 + NADH + OXYGEN-MOLECULE + PROTON -> CPD-13034 + NAD; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-674 + NADH + OXYGEN-MOLECULE + PROTON -> CPD-13034 + NAD; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by putative 3-phenylpropionate/cinnamate dioxygenase (complex.ecocyc.HCAMULTI-CPLX). Substrates: NADH (molecule.C00004), Oxygen (molecule.C00007), H+ (molecule.C00080), trans-Cinnamate (molecule.C00423). Products: NAD+ (molecule.C00003), (2E)-3-(5,6-dihydroxycyclohexa-1,3-dien-1-yl)prop-2-enoate (molecule.ecocyc.CPD-13034).

## Enriched Pathways

- `ecocyc.PWY-6690` cinnamate and 3-hydroxycinnamate degradation to 2-hydroxypentadienoate (EcoCyc)

## Annotation

CPD-674 + NADH + OXYGEN-MOLECULE + PROTON -> CPD-13034 + NAD; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6690` cinnamate and 3-hydroxycinnamate degradation to 2-hydroxypentadienoate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.HCAMULTI-CPLX|complex.ecocyc.HCAMULTI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-13034|molecule.ecocyc.CPD-13034]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00423|molecule.C00423]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12072`

## Notes

CPD-674 + NADH + OXYGEN-MOLECULE + PROTON -> CPD-13034 + NAD; direction=PHYSIOL-LEFT-TO-RIGHT
