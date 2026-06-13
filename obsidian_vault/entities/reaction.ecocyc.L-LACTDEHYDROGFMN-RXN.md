---
entity_id: "reaction.ecocyc.L-LACTDEHYDROGFMN-RXN"
entity_type: "reaction"
name: "lactate oxidation"
source_database: "EcoCyc"
source_id: "L-LACTDEHYDROGFMN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# lactate oxidation

`reaction.ecocyc.L-LACTDEHYDROGFMN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:L-LACTDEHYDROGFMN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This reaction is a primary dehydrogenase in the respiratory chain of E. coli. EcoCyc reaction equation: ETR-Quinones + L-LACTATE -> ETR-Quinols + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is a primary dehydrogenase in the respiratory chain of E. coli.

## Biological Role

Catalyzed by lldD (protein.P33232). Substrates: (S)-Lactate (molecule.C00186). Products: Pyruvate (molecule.C00022).

## Enriched Pathways

- `ecocyc.PWY0-1317` L-lactaldehyde degradation (aerobic) (EcoCyc)

## Annotation

This reaction is a primary dehydrogenase in the respiratory chain of E. coli.

## Pathways

- `ecocyc.PWY0-1317` L-lactaldehyde degradation (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `activates` <-- [[molecule.C00865|molecule.C00865]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P33232|protein.P33232]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00186|molecule.C00186]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1604|molecule.ecocyc.CPD0-1604]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:L-LACTDEHYDROGFMN-RXN`

## Notes

ETR-Quinones + L-LACTATE -> ETR-Quinols + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT
