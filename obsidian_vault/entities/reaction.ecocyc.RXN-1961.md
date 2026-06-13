---
entity_id: "reaction.ecocyc.RXN-1961"
entity_type: "reaction"
name: "RXN-1961"
source_database: "EcoCyc"
source_id: "RXN-1961"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "mesJ"
  - "yacA"
  - "L-lysine:[tRN<sup>Ile2</sup>]-cytidine<sup>34</sup> ligase (AMP-forming)"
---

# RXN-1961

`reaction.ecocyc.RXN-1961`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-1961`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cytidine-34-tRNAIle2 + LYS + ATP -> Lysidine-tRNA-Ile2 + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Cytidine-34-tRNAIle2 + LYS + ATP -> Lysidine-tRNA-Ile2 + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tilS (protein.P52097). Substrates: ATP (molecule.C00002), L-Lysine (molecule.C00047), a cytidine34 in tRNAIle2 (molecule.ecocyc.Cytidine-34-tRNAIle2). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), a lysidine34 in tRNAIle2 (molecule.ecocyc.Lysidine-tRNA-Ile2).

## Annotation

Cytidine-34-tRNAIle2 + LYS + ATP -> Lysidine-tRNA-Ile2 + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P52097|protein.P52097]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Lysidine-tRNA-Ile2|molecule.ecocyc.Lysidine-tRNA-Ile2]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Cytidine-34-tRNAIle2|molecule.ecocyc.Cytidine-34-tRNAIle2]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-1961`

## Notes

Cytidine-34-tRNAIle2 + LYS + ATP -> Lysidine-tRNA-Ile2 + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
