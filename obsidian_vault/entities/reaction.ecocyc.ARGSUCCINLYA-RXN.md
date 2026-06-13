---
entity_id: "reaction.ecocyc.ARGSUCCINLYA-RXN"
entity_type: "reaction"
name: "ARGSUCCINLYA-RXN"
source_database: "EcoCyc"
source_id: "ARGSUCCINLYA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ARGSUCCINLYA-RXN

`reaction.ecocyc.ARGSUCCINLYA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ARGSUCCINLYA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the eighth and final step in arginine biosynthesis. EcoCyc reaction equation: L-ARGININO-SUCCINATE -> ARG + FUM; direction=REVERSIBLE. This is the eighth and final step in arginine biosynthesis.

## Biological Role

Catalyzed by argH (protein.P11447). Substrates: N-(L-Arginino)succinate (molecule.C03406). Products: L-Arginine (molecule.C00062), Fumarate (molecule.C00122).

## Enriched Pathways

- `ecocyc.ARGSYN-PWY` L-arginine biosynthesis I (via L-ornithine) (EcoCyc)

## Annotation

This is the eighth and final step in arginine biosynthesis.

## Pathways

- `ecocyc.ARGSYN-PWY` L-arginine biosynthesis I (via L-ornithine) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P11447|protein.P11447]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03406|molecule.C03406]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Sulfhydryl-Reagents|molecule.ecocyc.Sulfhydryl-Reagents]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ARGSUCCINLYA-RXN`

## Notes

L-ARGININO-SUCCINATE -> ARG + FUM; direction=REVERSIBLE
