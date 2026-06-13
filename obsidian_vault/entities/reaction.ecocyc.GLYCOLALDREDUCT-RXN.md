---
entity_id: "reaction.ecocyc.GLYCOLALDREDUCT-RXN"
entity_type: "reaction"
name: "GLYCOLALDREDUCT-RXN"
source_database: "EcoCyc"
source_id: "GLYCOLALDREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYCOLALDREDUCT-RXN

`reaction.ecocyc.GLYCOLALDREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYCOLALDREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction in glycolate metabolism. EcoCyc reaction equation: NAD + GLYCOL -> PROTON + GLYCOLALDEHYDE + NADH; direction=REVERSIBLE. This is a reaction in glycolate metabolism.

## Biological Role

Catalyzed by lactaldehyde reductase (complex.ecocyc.LACTALDREDUCT-CPLX). Substrates: NAD+ (molecule.C00003), Ethylene glycol (molecule.C01380). Products: NADH (molecule.C00004), H+ (molecule.C00080), Glycolaldehyde (molecule.C00266).

## Enriched Pathways

- `ecocyc.PWY0-1280` ethylene glycol degradation (EcoCyc)

## Annotation

This is a reaction in glycolate metabolism.

## Pathways

- `ecocyc.PWY0-1280` ethylene glycol degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.LACTALDREDUCT-CPLX|complex.ecocyc.LACTALDREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00266|molecule.C00266]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01380|molecule.C01380]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYCOLALDREDUCT-RXN`

## Notes

NAD + GLYCOL -> PROTON + GLYCOLALDEHYDE + NADH; direction=REVERSIBLE
