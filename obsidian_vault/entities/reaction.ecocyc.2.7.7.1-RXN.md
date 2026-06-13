---
entity_id: "reaction.ecocyc.2.7.7.1-RXN"
entity_type: "reaction"
name: "2.7.7.1-RXN"
source_database: "EcoCyc"
source_id: "2.7.7.1-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "NAD(+) PYROPHOSPHORYLASE"
---

# 2.7.7.1-RXN

`reaction.ecocyc.2.7.7.1-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.7.7.1-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SEE ALSO EC 2.7.7.18. EcoCyc reaction equation: PROTON + NICOTINAMIDE_NUCLEOTIDE + ATP -> NAD + PPI; direction=PHYSIOL-LEFT-TO-RIGHT. SEE ALSO EC 2.7.7.18.

## Biological Role

Catalyzed by DNA-binding transcriptional repressor/NMN adenylyltransferase NadR (complex.ecocyc.CPLX0-7975). Substrates: ATP (molecule.C00002), H+ (molecule.C00080), Nicotinamide D-ribonucleotide (molecule.C00455). Products: NAD+ (molecule.C00003), Diphosphate (molecule.C00013).

## Enriched Pathways

- `ecocyc.PWY3O-4106` NAD salvage pathway IV (from nicotinamide riboside) (EcoCyc)

## Annotation

SEE ALSO EC 2.7.7.18.

## Pathways

- `ecocyc.PWY3O-4106` NAD salvage pathway IV (from nicotinamide riboside) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7975|complex.ecocyc.CPLX0-7975]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00455|molecule.C00455]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.7.7.1-RXN`

## Notes

PROTON + NICOTINAMIDE_NUCLEOTIDE + ATP -> NAD + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
