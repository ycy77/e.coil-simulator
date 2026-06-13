---
entity_id: "reaction.ecocyc.DMBPPRIBOSYLTRANS-RXN"
entity_type: "reaction"
name: "DMBPPRIBOSYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "DMBPPRIBOSYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DMBPPRIBOSYLTRANS-RXN

`reaction.ecocyc.DMBPPRIBOSYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DMBPPRIBOSYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes the lower ligand of adenosylcobalamin. EcoCyc reaction equation: NICOTINATE_NUCLEOTIDE + DIMETHYLBENZIMIDAZOLE -> PROTON + NIACINE + ALPHA-RIBAZOLE-5-P; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction synthesizes the lower ligand of adenosylcobalamin.

## Biological Role

Catalyzed by nicotinate-nucleotide—dimethylbenzimidazole phosphoribosyltransferase (complex.ecocyc.DMBPPRIBOSYLTRANS-CPLX). Substrates: Nicotinate D-ribonucleotide (molecule.C01185), Dimethylbenzimidazole (molecule.C03114). Products: H+ (molecule.C00080), Nicotinate (molecule.C00253), N1-(5-Phospho-alpha-D-ribosyl)-5,6-dimethylbenzimidazole (molecule.C04778).

## Enriched Pathways

- `ecocyc.COBALSYN-PWY` superpathway of adenosylcobalamin salvage from cobinamide I (EcoCyc)
- `ecocyc.PWY-5509` adenosylcobalamin biosynthesis from adenosylcobinamide-GDP I (EcoCyc)

## Annotation

This reaction synthesizes the lower ligand of adenosylcobalamin.

## Pathways

- `ecocyc.COBALSYN-PWY` superpathway of adenosylcobalamin salvage from cobinamide I (EcoCyc)
- `ecocyc.PWY-5509` adenosylcobalamin biosynthesis from adenosylcobinamide-GDP I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.DMBPPRIBOSYLTRANS-CPLX|complex.ecocyc.DMBPPRIBOSYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00253|molecule.C00253]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04778|molecule.C04778]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01185|molecule.C01185]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03114|molecule.C03114]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DMBPPRIBOSYLTRANS-RXN`

## Notes

NICOTINATE_NUCLEOTIDE + DIMETHYLBENZIMIDAZOLE -> PROTON + NIACINE + ALPHA-RIBAZOLE-5-P; direction=PHYSIOL-LEFT-TO-RIGHT
