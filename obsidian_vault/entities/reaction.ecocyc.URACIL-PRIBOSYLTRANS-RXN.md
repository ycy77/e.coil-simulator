---
entity_id: "reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN"
entity_type: "reaction"
name: "URACIL-PRIBOSYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "URACIL-PRIBOSYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# URACIL-PRIBOSYLTRANS-RXN

`reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:URACIL-PRIBOSYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the pyrimidine salvage pathway. EcoCyc reaction equation: PPI + UMP -> PRPP + URACIL; direction=RIGHT-TO-LEFT. This reaction is part of the pyrimidine salvage pathway.

## Biological Role

Catalyzed by uracil phosphoribosyltransferase (complex.ecocyc.URACIL-PRIBOSYLTRANS-CPLX). Substrates: Diphosphate (molecule.C00013), UMP (molecule.C00105). Products: Uracil (molecule.C00106), 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119).

## Enriched Pathways

- `ecocyc.PWY-7183` pyrimidine nucleobases salvage I (EcoCyc)
- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Annotation

This reaction is part of the pyrimidine salvage pathway.

## Pathways

- `ecocyc.PWY-7183` pyrimidine nucleobases salvage I (EcoCyc)
- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.URACIL-PRIBOSYLTRANS-CPLX|complex.ecocyc.URACIL-PRIBOSYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1327|molecule.ecocyc.CPD0-1327]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Uridine-Nucleotides|molecule.ecocyc.Uridine-Nucleotides]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:URACIL-PRIBOSYLTRANS-RXN`

## Notes

PPI + UMP -> PRPP + URACIL; direction=RIGHT-TO-LEFT
