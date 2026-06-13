---
entity_id: "reaction.ecocyc.RXN0-7188"
entity_type: "reaction"
name: "RXN0-7188"
source_database: "EcoCyc"
source_id: "RXN0-7188"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7188

`reaction.ecocyc.RXN0-7188`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7188`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Free methionine is readily oxidized to methionine sulfoxide by many reactive oxygen species, including the two-electron acceptor hydrogen peroxide, as shown here.Oxidation of L-methionine produces varying amounts of the two diastereoisomeric sulfoxides of L-methionine EcoCyc reaction equation: MET + HYDROGEN-PEROXIDE -> CPD-8990 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT. Free methionine is readily oxidized to methionine sulfoxide by many reactive oxygen species, including the two-electron acceptor hydrogen peroxide, as shown here.Oxidation of L-methionine produces varying amounts of the two diastereoisomeric sulfoxides of L-methionine

## Biological Role

Substrates: Hydrogen peroxide (molecule.C00027), L-Methionine (molecule.C00073). Products: H2O (molecule.C00001), L-methionine-(R)-S-oxide (molecule.ecocyc.CPD-8990).

## Annotation

Free methionine is readily oxidized to methionine sulfoxide by many reactive oxygen species, including the two-electron acceptor hydrogen peroxide, as shown here.Oxidation of L-methionine produces varying amounts of the two diastereoisomeric sulfoxides of L-methionine

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-8990|molecule.ecocyc.CPD-8990]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7188`

## Notes

MET + HYDROGEN-PEROXIDE -> CPD-8990 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
