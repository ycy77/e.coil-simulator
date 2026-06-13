---
entity_id: "reaction.ecocyc.ADENPRIBOSYLTRAN-RXN"
entity_type: "reaction"
name: "ADENPRIBOSYLTRAN-RXN"
source_database: "EcoCyc"
source_id: "ADENPRIBOSYLTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADENPRIBOSYLTRAN-RXN

`reaction.ecocyc.ADENPRIBOSYLTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADENPRIBOSYLTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in purine salvage. EcoCyc reaction equation: PPI + AMP -> PRPP + ADENINE; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction is involved in purine salvage.

## Biological Role

Catalyzed by adenine phosphoribosyltransferase (complex.ecocyc.ADENPRIBOSYLTRAN-CPLX). Substrates: Diphosphate (molecule.C00013), AMP (molecule.C00020). Products: 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119), Adenine (molecule.C00147).

## Enriched Pathways

- `ecocyc.PWY-6605` adenine and adenosine salvage II (EcoCyc)
- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)

## Annotation

This reaction is involved in purine salvage.

## Pathways

- `ecocyc.PWY-6605` adenine and adenosine salvage II (EcoCyc)
- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `catalyzes` <-- [[complex.ecocyc.ADENPRIBOSYLTRAN-CPLX|complex.ecocyc.ADENPRIBOSYLTRAN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00206|molecule.C00206]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00360|molecule.C00360]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Ribonucleoside-Triphosphates|molecule.ecocyc.Ribonucleoside-Triphosphates]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ADENPRIBOSYLTRAN-RXN`

## Notes

PPI + AMP -> PRPP + ADENINE; direction=PHYSIOL-RIGHT-TO-LEFT
