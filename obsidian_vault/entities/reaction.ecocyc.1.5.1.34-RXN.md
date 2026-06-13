---
entity_id: "reaction.ecocyc.1.5.1.34-RXN"
entity_type: "reaction"
name: "1.5.1.34-RXN"
source_database: "EcoCyc"
source_id: "1.5.1.34-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.5.1.34-RXN

`reaction.ecocyc.1.5.1.34-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.5.1.34-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of central intermediary metabolism. It regenerates a cofactor, dihydrobiopterin. This cofactor is used by many organisms, but not E. coli, in the hydroxylation of aromatic amino acids. EcoCyc reaction equation: TETRA-H-BIOPTERIN + NAD-P-OR-NOP -> 6-7-Dihydrobiopterins + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction is part of central intermediary metabolism. It regenerates a cofactor, dihydrobiopterin. This cofactor is used by many organisms, but not E. coli, in the hydroxylation of aromatic amino acids.

## Biological Role

Catalyzed by NAD(P)H-dependent nitroreductase NfsB (complex.ecocyc.DIHYDROPTERIREDUCT-CPLX), hmp (protein.P24232). Substrates: Tetrahydrobiopterin (molecule.C00272), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), 6,7-dihydrobiopterin (molecule.ecocyc.6-7-Dihydrobiopterins), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Annotation

This reaction is part of central intermediary metabolism. It regenerates a cofactor, dihydrobiopterin. This cofactor is used by many organisms, but not E. coli, in the hydroxylation of aromatic amino acids.

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.DIHYDROPTERIREDUCT-CPLX|complex.ecocyc.DIHYDROPTERIREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P24232|protein.P24232]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.6-7-Dihydrobiopterins|molecule.ecocyc.6-7-Dihydrobiopterins]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00272|molecule.C00272]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01937|molecule.C01937]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:1.5.1.34-RXN`

## Notes

TETRA-H-BIOPTERIN + NAD-P-OR-NOP -> 6-7-Dihydrobiopterins + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
