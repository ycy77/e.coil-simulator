---
entity_id: "reaction.ecocyc.TRANS-RXN-237"
entity_type: "reaction"
name: "TRANS-RXN-237"
source_database: "EcoCyc"
source_id: "TRANS-RXN-237"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-237

`reaction.ecocyc.TRANS-RXN-237`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-237`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

CPD-21359 + ATP + WATER -> CPD-21359 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-21359 + ATP + WATER -> CPD-21359 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lipopolysaccharide transport system (complex.ecocyc.CPLX0-7992). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359). Products: ADP (molecule.C00008), H+ (molecule.C00080), lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-21359 + ATP + WATER -> CPD-21359 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7992|complex.ecocyc.CPLX0-7992]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-237`

## Notes

CPD-21359 + ATP + WATER -> CPD-21359 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
