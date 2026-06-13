---
entity_id: "reaction.ecocyc.RXN-12073"
entity_type: "reaction"
name: "RXN-12073"
source_database: "EcoCyc"
source_id: "RXN-12073"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12073

`reaction.ecocyc.RXN-12073`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12073`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10796 + OXYGEN-MOLECULE -> CPD0-2184 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-10796 + OXYGEN-MOLECULE -> CPD0-2184 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-carboxyethylcatechol 2,3-dioxygenase (complex.ecocyc.DHPDIOXYGEN-CPLX). Substrates: Oxygen (molecule.C00007), trans-2,3-Dihydroxycinnamate (molecule.C12623). Products: H+ (molecule.C00080), 2-Hydroxy-6-ketononatrienedioate (molecule.C12624).

## Enriched Pathways

- `ecocyc.PWY-6690` cinnamate and 3-hydroxycinnamate degradation to 2-hydroxypentadienoate (EcoCyc)

## Annotation

CPD-10796 + OXYGEN-MOLECULE -> CPD0-2184 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6690` cinnamate and 3-hydroxycinnamate degradation to 2-hydroxypentadienoate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.DHPDIOXYGEN-CPLX|complex.ecocyc.DHPDIOXYGEN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C12624|molecule.C12624]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C12623|molecule.C12623]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12073`

## Notes

CPD-10796 + OXYGEN-MOLECULE -> CPD0-2184 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
