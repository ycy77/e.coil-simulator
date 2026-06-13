---
entity_id: "reaction.ecocyc.NUCLEOSIDE-DIP-KIN-RXN"
entity_type: "reaction"
name: "NUCLEOSIDE-DIP-KIN-RXN"
source_database: "EcoCyc"
source_id: "NUCLEOSIDE-DIP-KIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NUCLEOSIDE-DIP-KIN-RXN

`reaction.ecocyc.NUCLEOSIDE-DIP-KIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NUCLEOSIDE-DIP-KIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction has a major role in the synthesis of nucleoside triphosphates other than ATP. EcoCyc reaction equation: Nucleoside-Diphosphates + ATP -> Nucleoside-Triphosphates + ADP; direction=LEFT-TO-RIGHT. This reaction has a major role in the synthesis of nucleoside triphosphates other than ATP.

## Biological Role

Catalyzed by nucleoside diphosphate kinase (complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX). Substrates: ATP (molecule.C00002), a nucleoside diphosphate (molecule.ecocyc.Nucleoside-Diphosphates). Products: ADP (molecule.C00008), a nucleoside triphosphate (molecule.ecocyc.Nucleoside-Triphosphates).

## Annotation

This reaction has a major role in the synthesis of nucleoside triphosphates other than ATP.

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX|complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Nucleoside-Triphosphates|molecule.ecocyc.Nucleoside-Triphosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Nucleoside-Diphosphates|molecule.ecocyc.Nucleoside-Diphosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:NUCLEOSIDE-DIP-KIN-RXN`

## Notes

Nucleoside-Diphosphates + ATP -> Nucleoside-Triphosphates + ADP; direction=LEFT-TO-RIGHT
