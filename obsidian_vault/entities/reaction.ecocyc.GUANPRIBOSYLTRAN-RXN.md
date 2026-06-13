---
entity_id: "reaction.ecocyc.GUANPRIBOSYLTRAN-RXN"
entity_type: "reaction"
name: "GUANPRIBOSYLTRAN-RXN"
source_database: "EcoCyc"
source_id: "GUANPRIBOSYLTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GUANPRIBOSYLTRAN-RXN

`reaction.ecocyc.GUANPRIBOSYLTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GUANPRIBOSYLTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction salvages guanine for guanine nucleotide synthesis. EcoCyc reaction equation: GMP + PPI -> GUANINE + PRPP; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction salvages guanine for guanine nucleotide synthesis.

## Biological Role

Catalyzed by hypoxanthine phosphoribosyltransferase (complex.ecocyc.CPLX0-7685), xanthine-guanine phosphoribosyltransferase (complex.ecocyc.GPT-CPLX). Substrates: Diphosphate (molecule.C00013), GMP (molecule.C00144). Products: 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119), Guanine (molecule.C00242).

## Enriched Pathways

- `ecocyc.PWY-6620` guanine and guanosine salvage I (EcoCyc)

## Annotation

This reaction salvages guanine for guanine nucleotide synthesis.

## Pathways

- `ecocyc.PWY-6620` guanine and guanosine salvage I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7685|complex.ecocyc.CPLX0-7685]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.GPT-CPLX|complex.ecocyc.GPT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00242|molecule.C00242]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5721|molecule.ecocyc.CPD-5721]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GUANPRIBOSYLTRAN-RXN`

## Notes

GMP + PPI -> GUANINE + PRPP; direction=PHYSIOL-RIGHT-TO-LEFT
