---
entity_id: "reaction.ecocyc.RXN-22647"
entity_type: "reaction"
name: "RXN-22647"
source_database: "EcoCyc"
source_id: "RXN-22647"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22647

`reaction.ecocyc.RXN-22647`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22647`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HypCD-Dimer-Fe-CO2 + ATP + Donor-H1 -> HypCD-Dimer-Fe-CO + ADP + Pi + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HypCD-Dimer-Fe-CO2 + ATP + Donor-H1 -> HypCD-Dimer-Fe-CO + ADP + Pi + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hypD (protein.P24192). Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-8319` NiFe(CO)(CN)2 cofactor biosynthesis (EcoCyc)

## Annotation

HypCD-Dimer-Fe-CO2 + ATP + Donor-H1 -> HypCD-Dimer-Fe-CO + ADP + Pi + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8319` NiFe(CO)(CN)2 cofactor biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P24192|protein.P24192]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22647`

## Notes

HypCD-Dimer-Fe-CO2 + ATP + Donor-H1 -> HypCD-Dimer-Fe-CO + ADP + Pi + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
