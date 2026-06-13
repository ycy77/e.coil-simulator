---
entity_id: "reaction.ecocyc.RXN-11361"
entity_type: "reaction"
name: "RXN-11361"
source_database: "EcoCyc"
source_id: "RXN-11361"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11361

`reaction.ecocyc.RXN-11361`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11361`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Adenylates the C-terminus of the small subunit of the molybdopterin synthase. This activation is required to form the thiocarboxylated C-terminus of the active molybdopterin synthase small subunit. The reaction occurs in prokaryotes and eukaryotes. In the human, the reaction is catalysed by the N-terminal domain of the protein MOCS3, which also includes a molybdopterin-synthase sulfurtransferase (EC 2.8.1.c) C-terminal domain. EcoCyc reaction equation: MPT-Synthase-small-subunits + ATP + PROTON -> Carboxyadenylated-MPT-synthases + PPI; direction=LEFT-TO-RIGHT. Adenylates the C-terminus of the small subunit of the molybdopterin synthase. This activation is required to form the thiocarboxylated C-terminus of the active molybdopterin synthase small subunit. The reaction occurs in prokaryotes and eukaryotes. In the human, the reaction is catalysed by the N-terminal domain of the protein MOCS3, which also includes a molybdopterin-synthase sulfurtransferase (EC 2.8.1.c) C-terminal domain.

## Biological Role

Catalyzed by molybdopterin synthase adenylyltransferase/sulfur transferase (complex.ecocyc.CPLX0-12611), molybdopterin synthase adenylyltransferase (complex.ecocyc.CPLX0-8164). Substrates: ATP (molecule.C00002), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013).

## Enriched Pathways

- `ecocyc.PWY-6823` molybdopterin biosynthesis (EcoCyc)

## Annotation

Adenylates the C-terminus of the small subunit of the molybdopterin synthase. This activation is required to form the thiocarboxylated C-terminus of the active molybdopterin synthase small subunit. The reaction occurs in prokaryotes and eukaryotes. In the human, the reaction is catalysed by the N-terminal domain of the protein MOCS3, which also includes a molybdopterin-synthase sulfurtransferase (EC 2.8.1.c) C-terminal domain.

## Pathways

- `ecocyc.PWY-6823` molybdopterin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-12611|complex.ecocyc.CPLX0-12611]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8164|complex.ecocyc.CPLX0-8164]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11361`

## Notes

MPT-Synthase-small-subunits + ATP + PROTON -> Carboxyadenylated-MPT-synthases + PPI; direction=LEFT-TO-RIGHT
