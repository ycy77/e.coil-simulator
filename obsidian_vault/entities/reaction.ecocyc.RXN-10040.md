---
entity_id: "reaction.ecocyc.RXN-10040"
entity_type: "reaction"
name: "RXN-10040"
source_database: "EcoCyc"
source_id: "RXN-10040"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10040

`reaction.ecocyc.RXN-10040`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10040`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10797 + OXYGEN-MOLECULE + NADH + PROTON -> CPD-10796 + WATER + NAD; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-10797 + OXYGEN-MOLECULE + NADH + PROTON -> CPD-10796 + WATER + NAD; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mhpA (protein.P77397). Substrates: NADH (molecule.C00004), Oxygen (molecule.C00007), H+ (molecule.C00080), trans-3-Hydroxycinnamate (molecule.C12621). Products: H2O (molecule.C00001), NAD+ (molecule.C00003), trans-2,3-Dihydroxycinnamate (molecule.C12623).

## Enriched Pathways

- `ecocyc.PWY-6690` cinnamate and 3-hydroxycinnamate degradation to 2-hydroxypentadienoate (EcoCyc)

## Annotation

CPD-10797 + OXYGEN-MOLECULE + NADH + PROTON -> CPD-10796 + WATER + NAD; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6690` cinnamate and 3-hydroxycinnamate degradation to 2-hydroxypentadienoate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P77397|protein.P77397]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C12623|molecule.C12623]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C12621|molecule.C12621]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10040`

## Notes

CPD-10797 + OXYGEN-MOLECULE + NADH + PROTON -> CPD-10796 + WATER + NAD; direction=PHYSIOL-LEFT-TO-RIGHT
