---
entity_id: "reaction.ecocyc.NMNNUCLEOSID-RXN"
entity_type: "reaction"
name: "NMNNUCLEOSID-RXN"
source_database: "EcoCyc"
source_id: "NMNNUCLEOSID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NMNNUCLEOSID-RXN

`reaction.ecocyc.NMNNUCLEOSID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NMNNUCLEOSID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in NAD recycling. EcoCyc reaction equation: WATER + NICOTINAMIDE_NUCLEOTIDE -> CPD-15317 + NIACINAMIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is involved in NAD recycling.

## Biological Role

Catalyzed by NMNNUCLEOSID-MONOMER (protein.ecocyc.NMNNUCLEOSID-MONOMER). Substrates: H2O (molecule.C00001), Nicotinamide D-ribonucleotide (molecule.C00455). Products: H+ (molecule.C00080), Nicotinamide (molecule.C00153), D-ribofuranose 5-phosphate (molecule.ecocyc.CPD-15317).

## Enriched Pathways

- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)

## Annotation

This reaction is involved in NAD recycling.

## Pathways

- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.ecocyc.NMNNUCLEOSID-MONOMER|protein.ecocyc.NMNNUCLEOSID-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00153|molecule.C00153]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15317|molecule.ecocyc.CPD-15317]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00455|molecule.C00455]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NMNNUCLEOSID-RXN`

## Notes

WATER + NICOTINAMIDE_NUCLEOTIDE -> CPD-15317 + NIACINAMIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
