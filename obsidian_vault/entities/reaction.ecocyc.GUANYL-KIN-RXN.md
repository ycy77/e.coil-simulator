---
entity_id: "reaction.ecocyc.GUANYL-KIN-RXN"
entity_type: "reaction"
name: "GUANYL-KIN-RXN"
source_database: "EcoCyc"
source_id: "GUANYL-KIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GUANYL-KIN-RXN

`reaction.ecocyc.GUANYL-KIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GUANYL-KIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction recycles GMP. EcoCyc reaction equation: GMP + ATP -> GDP + ADP; direction=REVERSIBLE. This reaction recycles GMP.

## Biological Role

Catalyzed by guanylate kinase (complex.ecocyc.GUANYL-KIN-CPLX). Substrates: ATP (molecule.C00002), GMP (molecule.C00144). Products: ADP (molecule.C00008), GDP (molecule.C00035).

## Enriched Pathways

- `ecocyc.PWY-7221` guanosine ribonucleotides de novo biosynthesis (EcoCyc)

## Annotation

This reaction recycles GMP.

## Pathways

- `ecocyc.PWY-7221` guanosine ribonucleotides de novo biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.GUANYL-KIN-CPLX|complex.ecocyc.GUANYL-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00286|molecule.C00286]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00387|molecule.C00387]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1468|molecule.ecocyc.CPD0-1468]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GUANYL-KIN-RXN`

## Notes

GMP + ATP -> GDP + ADP; direction=REVERSIBLE
