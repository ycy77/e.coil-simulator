---
entity_id: "reaction.ecocyc.3.2.2.10-RXN"
entity_type: "reaction"
name: "3.2.2.10-RXN"
source_database: "EcoCyc"
source_id: "3.2.2.10-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.2.2.10-RXN

`reaction.ecocyc.3.2.2.10-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.2.2.10-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pyrimidine-ribonucleotides + WATER -> RIBOSE-5P + Pyrimidine-Bases; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Pyrimidine-ribonucleotides + WATER -> RIBOSE-5P + Pyrimidine-Bases; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nucleotide 5'-monophosphate nucleosidase (complex.ecocyc.CPLX0-8262). Substrates: H2O (molecule.C00001), a pyrimidine ribonucleotide (molecule.ecocyc.Pyrimidine-ribonucleotides). Products: D-Ribose 5-phosphate (molecule.C00117), a pyrimidine base (molecule.ecocyc.Pyrimidine-Bases).

## Annotation

Pyrimidine-ribonucleotides + WATER -> RIBOSE-5P + Pyrimidine-Bases; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8262|complex.ecocyc.CPLX0-8262]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00117|molecule.C00117]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pyrimidine-Bases|molecule.ecocyc.Pyrimidine-Bases]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pyrimidine-ribonucleotides|molecule.ecocyc.Pyrimidine-ribonucleotides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.2.2.10-RXN`

## Notes

Pyrimidine-ribonucleotides + WATER -> RIBOSE-5P + Pyrimidine-Bases; direction=PHYSIOL-LEFT-TO-RIGHT
