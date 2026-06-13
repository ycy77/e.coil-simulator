---
entity_id: "reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN"
entity_type: "reaction"
name: "MALATE-DEHYDROGENASE-ACCEPTOR-RXN"
source_database: "EcoCyc"
source_id: "MALATE-DEHYDROGENASE-ACCEPTOR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MALATE-DEHYDROGENASE-ACCEPTOR-RXN

`reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MALATE-DEHYDROGENASE-ACCEPTOR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ETR-Quinones + MAL -> ETR-Quinols + OXALACETIC_ACID; direction=REVERSIBLE EcoCyc reaction equation: ETR-Quinones + MAL -> ETR-Quinols + OXALACETIC_ACID; direction=REVERSIBLE.

## Biological Role

Catalyzed by mqo (protein.P33940). Substrates: (S)-Malate (molecule.C00149). Products: Oxaloacetate (molecule.C00036).

## Enriched Pathways

- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Annotation

ETR-Quinones + MAL -> ETR-Quinols + OXALACETIC_ACID; direction=REVERSIBLE

## Pathways

- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `activates` <-- [[molecule.C00344|molecule.C00344]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C03892|molecule.C03892]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C05980|molecule.C05980]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.ASOLECTIN|molecule.ecocyc.ASOLECTIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P33940|protein.P33940]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:MALATE-DEHYDROGENASE-ACCEPTOR-RXN`

## Notes

ETR-Quinones + MAL -> ETR-Quinols + OXALACETIC_ACID; direction=REVERSIBLE
