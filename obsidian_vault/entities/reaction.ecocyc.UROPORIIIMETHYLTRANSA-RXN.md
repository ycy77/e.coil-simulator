---
entity_id: "reaction.ecocyc.UROPORIIIMETHYLTRANSA-RXN"
entity_type: "reaction"
name: "UROPORIIIMETHYLTRANSA-RXN"
source_database: "EcoCyc"
source_id: "UROPORIIIMETHYLTRANSA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UROPORIIIMETHYLTRANSA-RXN

`reaction.ecocyc.UROPORIIIMETHYLTRANSA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UROPORIIIMETHYLTRANSA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is necessary for the synthesis of siroheme, which is an important and novel prosthetic group in the sulfite reductase reaction in the cysteine biosynthesis pathway and also in nitrate reductase. This reaction is a summary of two individual reactions catalyzed by the enzyme, which are: (1) S-adenosyl-L-methionine + uroporphyrinogen III = S-adenosyl-L-homocysteine + precorrin-1 (2) S-adenosyl-L-methionine + precorrin-1 = S-adenosyl-L-homocysteine + precorrin-2 EcoCyc reaction equation: S-ADENOSYLMETHIONINE + UROPORPHYRINOGEN-III -> ADENOSYL-HOMO-CYS + CPD-9038 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is necessary for the synthesis of siroheme, which is an important and novel prosthetic group in the sulfite reductase reaction in the cysteine biosynthesis pathway and also in nitrate reductase. This reaction is a summary of two individual reactions catalyzed by the enzyme, which are: (1) S-adenosyl-L-methionine + uroporphyrinogen III = S-adenosyl-L-homocysteine + precorrin-1 (2) S-adenosyl-L-methionine + precorrin-1 = S-adenosyl-L-homocysteine + precorrin-2

## Biological Role

Catalyzed by siroheme synthase (complex.ecocyc.SIROHEMESYN-CPLX). Substrates: S-Adenosyl-L-methionine (molecule.C00019), Uroporphyrinogen III (molecule.C01051). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), precorrin-1 (molecule.ecocyc.CPD-9038).

## Enriched Pathways

- `ecocyc.PWY-5194` siroheme biosynthesis (EcoCyc)

## Annotation

This reaction is necessary for the synthesis of siroheme, which is an important and novel prosthetic group in the sulfite reductase reaction in the cysteine biosynthesis pathway and also in nitrate reductase. This reaction is a summary of two individual reactions catalyzed by the enzyme, which are: (1) S-adenosyl-L-methionine + uroporphyrinogen III = S-adenosyl-L-homocysteine + precorrin-1 (2) S-adenosyl-L-methionine + precorrin-1 = S-adenosyl-L-homocysteine + precorrin-2

## Pathways

- `ecocyc.PWY-5194` siroheme biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.SIROHEMESYN-CPLX|complex.ecocyc.SIROHEMESYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-9038|molecule.ecocyc.CPD-9038]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01051|molecule.C01051]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:UROPORIIIMETHYLTRANSA-RXN`

## Notes

S-ADENOSYLMETHIONINE + UROPORPHYRINOGEN-III -> ADENOSYL-HOMO-CYS + CPD-9038 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
