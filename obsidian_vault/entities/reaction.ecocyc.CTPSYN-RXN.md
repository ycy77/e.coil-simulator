---
entity_id: "reaction.ecocyc.CTPSYN-RXN"
entity_type: "reaction"
name: "CTPSYN-RXN"
source_database: "EcoCyc"
source_id: "CTPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CTPSYN-RXN

`reaction.ecocyc.CTPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CTPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is part of pyrimidinenucleotide metabolism. EcoCyc reaction equation: ATP + UTP + GLN + WATER -> PROTON + ADP + Pi + CTP + GLT; direction=PHYSIOL-LEFT-TO-RIGHT. This is part of pyrimidinenucleotide metabolism.

## Biological Role

Catalyzed by CTP synthetase (complex.ecocyc.CTPSYN-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Glutamine (molecule.C00064), UTP (molecule.C00075). Products: ADP (molecule.C00008), L-Glutamate (molecule.C00025), CTP (molecule.C00063), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-7176` UTP and CTP de novo biosynthesis (EcoCyc)

## Annotation

This is part of pyrimidinenucleotide metabolism.

## Pathways

- `ecocyc.PWY-7176` UTP and CTP de novo biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (19)

- `activates` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CTPSYN-CPLX|complex.ecocyc.CTPSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01165|molecule.C01165]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1037|molecule.ecocyc.CPD0-1037]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1038|molecule.ecocyc.CPD0-1038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2635|molecule.ecocyc.CPD0-2635]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CTPSYN-RXN`

## Notes

ATP + UTP + GLN + WATER -> PROTON + ADP + Pi + CTP + GLT; direction=PHYSIOL-LEFT-TO-RIGHT
