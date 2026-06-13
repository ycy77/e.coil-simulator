---
entity_id: "reaction.ecocyc.PROPKIN-RXN"
entity_type: "reaction"
name: "PROPKIN-RXN"
source_database: "EcoCyc"
source_id: "PROPKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PROPKIN-RXN

`reaction.ecocyc.PROPKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PROPKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the final reaction in the anaerobic L-threonine degradation pathway. Requires MG+2. Both propanoate and acetate can act as a substrate. Involved in the anaerobic degradation of L-threonine in bacteria . Both this enzyme and EC 2.7.2.1, acetate kinase, play important roles in the production of propanoate. Requires MG+2. Both propanoate and acetate can act as a substrate. Involved in the anaerobic degradation of L-threonine in bacteria . Both this enzyme and EC 2.7.2.1, acetate kinase, play important roles in the production of propanoate. EcoCyc reaction equation: ATP + PROPIONATE -> ADP + PROPIONYL-P; direction=REVERSIBLE. This is the final reaction in the anaerobic L-threonine degradation pathway. Requires MG+2. Both propanoate and acetate can act as a substrate. Involved in the anaerobic degradation of L-threonine in bacteria . Both this enzyme and EC 2.7.2.1, acetate kinase, play important roles in the production of propanoate. Requires MG+2. Both propanoate and acetate can act as a substrate. Involved in the anaerobic degradation of L-threonine in bacteria . Both this enzyme and EC 2.7.2.1, acetate kinase, play important roles in the production of propanoate.

## Biological Role

Catalyzed by ackA (protein.P0A6A3), tdcD (protein.P11868). Substrates: ATP (molecule.C00002), Propanoate (molecule.C00163). Products: ADP (molecule.C00008), Propanoyl phosphate (molecule.C02876).

## Enriched Pathways

- `ecocyc.PWY-5437` L-threonine degradation I (EcoCyc)

## Annotation

This is the final reaction in the anaerobic L-threonine degradation pathway. Requires MG+2. Both propanoate and acetate can act as a substrate. Involved in the anaerobic degradation of L-threonine in bacteria . Both this enzyme and EC 2.7.2.1, acetate kinase, play important roles in the production of propanoate. Requires MG+2. Both propanoate and acetate can act as a substrate. Involved in the anaerobic degradation of L-threonine in bacteria . Both this enzyme and EC 2.7.2.1, acetate kinase, play important roles in the production of propanoate.

## Pathways

- `ecocyc.PWY-5437` L-threonine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A6A3|protein.P0A6A3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P11868|protein.P11868]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02876|molecule.C02876]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00163|molecule.C00163]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PROPKIN-RXN`

## Notes

ATP + PROPIONATE -> ADP + PROPIONYL-P; direction=REVERSIBLE
