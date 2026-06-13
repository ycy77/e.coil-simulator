---
entity_id: "reaction.ecocyc.2.3.1.128-RXN"
entity_type: "reaction"
name: "2.3.1.128-RXN"
source_database: "EcoCyc"
source_id: "2.3.1.128-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.3.1.128-RXN

`reaction.ecocyc.2.3.1.128-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.3.1.128-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A GROUPS OF ENZYMES IN E.COLI WHICH ACETYLATE THE N-TERMINAL ALANINE RESIDUES OF SPECIFIC RIBOSOMAL PROTEINS (CF. EC 2.3.1.88). EcoCyc reaction equation: ACETYL-COA + S18-N-terminal-L-alanine -> Acetylated-S18-N-terminal-L-alanine + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. A GROUPS OF ENZYMES IN E.COLI WHICH ACETYLATE THE N-TERMINAL ALANINE RESIDUES OF SPECIFIC RIBOSOMAL PROTEINS (CF. EC 2.3.1.88).

## Biological Role

Catalyzed by rimI (protein.P0A944). Substrates: Acetyl-CoA (molecule.C00024), an N-terminal L-alanyl-[bS18 protein of 30S ribosome] (molecule.ecocyc.S18-N-terminal-L-alanine). Products: CoA (molecule.C00010), H+ (molecule.C00080), an N-terminal N-acetyl-L-alanyl-[bS18 protein of 30S ribosome] (molecule.ecocyc.Acetylated-S18-N-terminal-L-alanine).

## Annotation

A GROUPS OF ENZYMES IN E.COLI WHICH ACETYLATE THE N-TERMINAL ALANINE RESIDUES OF SPECIFIC RIBOSOMAL PROTEINS (CF. EC 2.3.1.88).

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A944|protein.P0A944]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Acetylated-S18-N-terminal-L-alanine|molecule.ecocyc.Acetylated-S18-N-terminal-L-alanine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.S18-N-terminal-L-alanine|molecule.ecocyc.S18-N-terminal-L-alanine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.3.1.128-RXN`

## Notes

ACETYL-COA + S18-N-terminal-L-alanine -> Acetylated-S18-N-terminal-L-alanine + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
