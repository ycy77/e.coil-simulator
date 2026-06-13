---
entity_id: "reaction.ecocyc.NADPYROPHOSPHAT-RXN"
entity_type: "reaction"
name: "NADPYROPHOSPHAT-RXN"
source_database: "EcoCyc"
source_id: "NADPYROPHOSPHAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "NAD+ diphosphatase"
---

# NADPYROPHOSPHAT-RXN

`reaction.ecocyc.NADPYROPHOSPHAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NADPYROPHOSPHAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction initiates pyridine ring cycling in the PNC VI pathway by the enzymatic degradation of NAD. EcoCyc reaction equation: WATER + NAD -> PROTON + NICOTINAMIDE_NUCLEOTIDE + AMP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction initiates pyridine ring cycling in the PNC VI pathway by the enzymatic degradation of NAD.

## Biological Role

Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003). Products: AMP (molecule.C00020), H+ (molecule.C00080), Nicotinamide D-ribonucleotide (molecule.C00455).

## Enriched Pathways

- `ecocyc.PWY-7761` NAD salvage pathway II (PNC IV cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)

## Annotation

This reaction initiates pyridine ring cycling in the PNC VI pathway by the enzymatic degradation of NAD.

## Pathways

- `ecocyc.PWY-7761` NAD salvage pathway II (PNC IV cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00455|molecule.C00455]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NADPYROPHOSPHAT-RXN`

## Notes

WATER + NAD -> PROTON + NICOTINAMIDE_NUCLEOTIDE + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
