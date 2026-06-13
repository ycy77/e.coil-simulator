---
entity_id: "reaction.ecocyc.4.3.1.15-RXN"
entity_type: "reaction"
name: "4.3.1.15-RXN"
source_database: "EcoCyc"
source_id: "4.3.1.15-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Diaminopropionatase"
---

# 4.3.1.15-RXN

`reaction.ecocyc.4.3.1.15-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:4.3.1.15-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

23-Diaminopropanoate + WATER -> AMMONIUM + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 23-Diaminopropanoate + WATER -> AMMONIUM + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2,3-diaminopropionate ammonia-lyase (complex.ecocyc.CPLX0-1401). Substrates: H2O (molecule.C00001), 2,3-diaminopropanoate (molecule.ecocyc.23-Diaminopropanoate). Products: Pyruvate (molecule.C00022), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

23-Diaminopropanoate + WATER -> AMMONIUM + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1401|complex.ecocyc.CPLX0-1401]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23-Diaminopropanoate|molecule.ecocyc.23-Diaminopropanoate]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:4.3.1.15-RXN`

## Notes

23-Diaminopropanoate + WATER -> AMMONIUM + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT
