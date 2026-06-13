---
entity_id: "reaction.ecocyc.RXN0-7346"
entity_type: "reaction"
name: "RXN0-7346"
source_database: "EcoCyc"
source_id: "RXN0-7346"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7346

`reaction.ecocyc.RXN0-7346`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7346`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A-5-prime-NAD-capped-RNA + WATER -> 5-prime-phospho-adenosine-RNA + NICOTINAMIDE_NUCLEOTIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: A-5-prime-NAD-capped-RNA + WATER -> 5-prime-phospho-adenosine-RNA + NICOTINAMIDE_NUCLEOTIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by RNA decapping hydrolase (complex.ecocyc.CPLX0-7974). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), Nicotinamide D-ribonucleotide (molecule.C00455).

## Annotation

A-5-prime-NAD-capped-RNA + WATER -> 5-prime-phospho-adenosine-RNA + NICOTINAMIDE_NUCLEOTIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7974|complex.ecocyc.CPLX0-7974]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00455|molecule.C00455]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7346`

## Notes

A-5-prime-NAD-capped-RNA + WATER -> 5-prime-phospho-adenosine-RNA + NICOTINAMIDE_NUCLEOTIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
