---
entity_id: "reaction.ecocyc.RXN0-743"
entity_type: "reaction"
name: "RXN0-743"
source_database: "EcoCyc"
source_id: "RXN0-743"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-743

`reaction.ecocyc.RXN0-743`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-743`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Reversible reaction catalyzed by N5-carboxyaminoimidazole ribonucleotide mutase (PurE complex) . EcoCyc reaction equation: CPD0-181 -> PHOSPHORIBOSYL-CARBOXY-AMINOIMIDAZOLE; direction=LEFT-TO-RIGHT. Reversible reaction catalyzed by N5-carboxyaminoimidazole ribonucleotide mutase (PurE complex) .

## Biological Role

Catalyzed by N5-carboxyaminoimidazole ribonucleotide mutase (complex.ecocyc.PURE-CPLX). Substrates: 5-Carboxyamino-1-(5-phospho-D-ribosyl)imidazole (molecule.C15667). Products: 1-(5-Phospho-D-ribosyl)-5-amino-4-imidazolecarboxylate (molecule.C04751).

## Enriched Pathways

- `ecocyc.PWY-6123` inosine-5'-phosphate biosynthesis I (EcoCyc)

## Annotation

Reversible reaction catalyzed by N5-carboxyaminoimidazole ribonucleotide mutase (PurE complex) .

## Pathways

- `ecocyc.PWY-6123` inosine-5'-phosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.PURE-CPLX|complex.ecocyc.PURE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04751|molecule.C04751]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C15667|molecule.C15667]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.NAIR|molecule.ecocyc.NAIR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-743`

## Notes

CPD0-181 -> PHOSPHORIBOSYL-CARBOXY-AMINOIMIDAZOLE; direction=LEFT-TO-RIGHT
