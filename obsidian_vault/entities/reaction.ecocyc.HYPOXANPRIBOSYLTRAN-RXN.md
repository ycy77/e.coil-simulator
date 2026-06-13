---
entity_id: "reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN"
entity_type: "reaction"
name: "HYPOXANPRIBOSYLTRAN-RXN"
source_database: "EcoCyc"
source_id: "HYPOXANPRIBOSYLTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HYPOXANPRIBOSYLTRAN-RXN

`reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HYPOXANPRIBOSYLTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is in the purine salvage pathway. EcoCyc reaction equation: PPI + IMP -> PRPP + HYPOXANTHINE; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction is in the purine salvage pathway.

## Biological Role

Catalyzed by hypoxanthine phosphoribosyltransferase (complex.ecocyc.CPLX0-7685), xanthine-guanine phosphoribosyltransferase (complex.ecocyc.GPT-CPLX). Substrates: Diphosphate (molecule.C00013), IMP (molecule.C00130). Products: 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119), Hypoxanthine (molecule.C00262).

## Enriched Pathways

- `ecocyc.PWY-6609` adenine and adenosine salvage III (EcoCyc)

## Annotation

This reaction is in the purine salvage pathway.

## Pathways

- `ecocyc.PWY-6609` adenine and adenosine salvage III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7685|complex.ecocyc.CPLX0-7685]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.GPT-CPLX|complex.ecocyc.GPT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00262|molecule.C00262]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BA_2|molecule.ecocyc.BA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:HYPOXANPRIBOSYLTRAN-RXN`

## Notes

PPI + IMP -> PRPP + HYPOXANTHINE; direction=PHYSIOL-RIGHT-TO-LEFT
