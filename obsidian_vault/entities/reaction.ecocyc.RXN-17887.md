---
entity_id: "reaction.ecocyc.RXN-17887"
entity_type: "reaction"
name: "RXN-17887"
source_database: "EcoCyc"
source_id: "RXN-17887"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17887

`reaction.ecocyc.RXN-17887`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17887`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-nitrosothiol-L-alanine + GLUTATHIONE -> PROT-CYS + S-NITROSOGLUTATHIONE; direction=REVERSIBLE EcoCyc reaction equation: Protein-nitrosothiol-L-alanine + GLUTATHIONE -> PROT-CYS + S-NITROSOGLUTATHIONE; direction=REVERSIBLE.

## Biological Role

Substrates: Glutathione (molecule.C00051), a [protein] 3-nitrosothio-L-alanine (molecule.ecocyc.Protein-nitrosothiol-L-alanine). Products: a [protein]-L-cysteine (molecule.ecocyc.PROT-CYS), S-nitrosoglutathione (molecule.ecocyc.S-NITROSOGLUTATHIONE).

## Annotation

Protein-nitrosothiol-L-alanine + GLUTATHIONE -> PROT-CYS + S-NITROSOGLUTATHIONE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.PROT-CYS|molecule.ecocyc.PROT-CYS]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.S-NITROSOGLUTATHIONE|molecule.ecocyc.S-NITROSOGLUTATHIONE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-nitrosothiol-L-alanine|molecule.ecocyc.Protein-nitrosothiol-L-alanine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17887`

## Notes

Protein-nitrosothiol-L-alanine + GLUTATHIONE -> PROT-CYS + S-NITROSOGLUTATHIONE; direction=REVERSIBLE
