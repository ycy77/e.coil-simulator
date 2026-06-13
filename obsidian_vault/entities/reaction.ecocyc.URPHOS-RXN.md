---
entity_id: "reaction.ecocyc.URPHOS-RXN"
entity_type: "reaction"
name: "URPHOS-RXN"
source_database: "EcoCyc"
source_id: "URPHOS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# URPHOS-RXN

`reaction.ecocyc.URPHOS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:URPHOS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the pyrimidine salvage pathway and degradation of pyrimidine nucleosides as carbon sources. EcoCyc reaction equation: Pi + URIDINE -> RIBOSE-1P + URACIL; direction=REVERSIBLE. This reaction is part of the pyrimidine salvage pathway and degradation of pyrimidine nucleosides as carbon sources.

## Biological Role

Catalyzed by nucleoside phosphorylase PpnP (complex.ecocyc.CPLX0-8619), uridine phosphorylase (complex.ecocyc.URPHOS-CPLX). Substrates: Uridine (molecule.C00299), phosphate (molecule.ecocyc.Pi). Products: Uracil (molecule.C00106), alpha-D-Ribose 1-phosphate (molecule.C00620).

## Enriched Pathways

- `ecocyc.PWY0-1295` pyrimidine ribonucleosides degradation (EcoCyc)
- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Annotation

This reaction is part of the pyrimidine salvage pathway and degradation of pyrimidine nucleosides as carbon sources.

## Pathways

- `ecocyc.PWY0-1295` pyrimidine ribonucleosides degradation (EcoCyc)
- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8619|complex.ecocyc.CPLX0-8619]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.URPHOS-CPLX|complex.ecocyc.URPHOS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00620|molecule.C00620]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00299|molecule.C00299]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00620|molecule.C00620]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Acyclonucleoside-Analogues|molecule.ecocyc.Acyclonucleoside-Analogues]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Benzylacylouridines|molecule.ecocyc.Benzylacylouridines]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:URPHOS-RXN`

## Notes

Pi + URIDINE -> RIBOSE-1P + URACIL; direction=REVERSIBLE
