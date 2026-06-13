---
entity_id: "reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN"
entity_type: "reaction"
name: "TYROSINE-AMINOTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "TYROSINE-AMINOTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TYROSINE-AMINOTRANSFERASE-RXN

`reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TYROSINE-AMINOTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the final reaction in the biosynthesis of tyrosine. EcoCyc reaction equation: TYR + 2-KETOGLUTARATE -> P-HYDROXY-PHENYLPYRUVATE + GLT; direction=REVERSIBLE. This is the final reaction in the biosynthesis of tyrosine.

## Biological Role

Catalyzed by aspartate aminotransferase (complex.ecocyc.ASPAMINOTRANS-DIMER), tyrosine aminotransferase (complex.ecocyc.TYRB-DIMER). Substrates: 2-Oxoglutarate (molecule.C00026), L-Tyrosine (molecule.C00082). Products: L-Glutamate (molecule.C00025), 3-(4-Hydroxyphenyl)pyruvate (molecule.C01179).

## Enriched Pathways

- `ecocyc.TYRSYN` L-tyrosine biosynthesis I (EcoCyc)

## Annotation

This is the final reaction in the biosynthesis of tyrosine.

## Pathways

- `ecocyc.TYRSYN` L-tyrosine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ASPAMINOTRANS-DIMER|complex.ecocyc.ASPAMINOTRANS-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.TYRB-DIMER|complex.ecocyc.TYRB-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01179|molecule.C01179]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00141|molecule.C00141]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TYROSINE-AMINOTRANSFERASE-RXN`

## Notes

TYR + 2-KETOGLUTARATE -> P-HYDROXY-PHENYLPYRUVATE + GLT; direction=REVERSIBLE
