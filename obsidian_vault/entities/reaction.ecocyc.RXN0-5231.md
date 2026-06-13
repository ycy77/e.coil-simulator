---
entity_id: "reaction.ecocyc.RXN0-5231"
entity_type: "reaction"
name: "RXN0-5231"
source_database: "EcoCyc"
source_id: "RXN0-5231"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5231

`reaction.ecocyc.RXN0-5231`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5231`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N-terminal-L-Serine-Ribosomal-Protein-L12 + ACETYL-COA -> N-terminal-N-Ac-L-Serine-L7 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: N-terminal-L-Serine-Ribosomal-Protein-L12 + ACETYL-COA -> N-terminal-N-Ac-L-Serine-L7 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rimL (protein.P13857). Substrates: Acetyl-CoA (molecule.C00024), an N-terminal-L-seryl-[ribosomal protein L12] (molecule.ecocyc.N-terminal-L-Serine-Ribosomal-Protein-L12). Products: CoA (molecule.C00010), H+ (molecule.C00080), an N-terminal Nα-acetyl-L-seryl-[ribosomal protein L7] (molecule.ecocyc.N-terminal-N-Ac-L-Serine-L7).

## Annotation

N-terminal-L-Serine-Ribosomal-Protein-L12 + ACETYL-COA -> N-terminal-N-Ac-L-Serine-L7 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P13857|protein.P13857]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N-terminal-N-Ac-L-Serine-L7|molecule.ecocyc.N-terminal-N-Ac-L-Serine-L7]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N-terminal-L-Serine-Ribosomal-Protein-L12|molecule.ecocyc.N-terminal-L-Serine-Ribosomal-Protein-L12]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5231`

## Notes

N-terminal-L-Serine-Ribosomal-Protein-L12 + ACETYL-COA -> N-terminal-N-Ac-L-Serine-L7 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
