---
entity_id: "reaction.ecocyc.3.1.11.2-RXN"
entity_type: "reaction"
name: "3.1.11.2-RXN"
source_database: "EcoCyc"
source_id: "3.1.11.2-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.1.11.2-RXN

`reaction.ecocyc.3.1.11.2-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.11.2-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The RXN-20426 "phosphatase" activity of Exonuclease III removes a terminal 3'-phosphoryl group prior to initiating the exodeoxyribonuclease reaction EcoCyc reaction equation: 3-Hydroxy-Terminated-DNAs + WATER -> 3-Hydroxy-Terminated-DNAs + Deoxy-Ribonucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT. The RXN-20426 "phosphatase" activity of Exonuclease III removes a terminal 3'-phosphoryl group prior to initiating the exodeoxyribonuclease reaction

## Biological Role

Catalyzed by xthA (protein.P09030). Substrates: H2O (molecule.C00001). Products: a 2'-deoxyribonucleoside 5'-monophosphate (molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates).

## Annotation

The RXN-20426 "phosphatase" activity of Exonuclease III removes a terminal 3'-phosphoryl group prior to initiating the exodeoxyribonuclease reaction

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P09030|protein.P09030]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates|molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.1.11.2-RXN`

## Notes

3-Hydroxy-Terminated-DNAs + WATER -> 3-Hydroxy-Terminated-DNAs + Deoxy-Ribonucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT
