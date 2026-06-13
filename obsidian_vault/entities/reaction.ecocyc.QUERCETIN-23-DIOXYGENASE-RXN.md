---
entity_id: "reaction.ecocyc.QUERCETIN-23-DIOXYGENASE-RXN"
entity_type: "reaction"
name: "QUERCETIN-23-DIOXYGENASE-RXN"
source_database: "EcoCyc"
source_id: "QUERCETIN-23-DIOXYGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# QUERCETIN-23-DIOXYGENASE-RXN

`reaction.ecocyc.QUERCETIN-23-DIOXYGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:QUERCETIN-23-DIOXYGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-520 + OXYGEN-MOLECULE -> 2-PROTOCATECHUOYLPHLOROGLUCINOLCARBOXYLA + CARBON-MONOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-520 + OXYGEN-MOLECULE -> 2-PROTOCATECHUOYLPHLOROGLUCINOLCARBOXYLA + CARBON-MONOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yhhW (protein.P46852). Substrates: Oxygen (molecule.C00007), Quercetin (molecule.C00389). Products: CO (molecule.C00237), 2-protocatechuoylphloroglucinolcarboxylate (molecule.ecocyc.2-PROTOCATECHUOYLPHLOROGLUCINOLCARBOXYLA).

## Annotation

CPD-520 + OXYGEN-MOLECULE -> 2-PROTOCATECHUOYLPHLOROGLUCINOLCARBOXYLA + CARBON-MONOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P46852|protein.P46852]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00237|molecule.C00237]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-PROTOCATECHUOYLPHLOROGLUCINOLCARBOXYLA|molecule.ecocyc.2-PROTOCATECHUOYLPHLOROGLUCINOLCARBOXYLA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00389|molecule.C00389]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.DIETHYLDITHIOCARBAMATE|molecule.ecocyc.DIETHYLDITHIOCARBAMATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.KOJIC-ACID|molecule.ecocyc.KOJIC-ACID]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:QUERCETIN-23-DIOXYGENASE-RXN`

## Notes

CPD-520 + OXYGEN-MOLECULE -> 2-PROTOCATECHUOYLPHLOROGLUCINOLCARBOXYLA + CARBON-MONOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
