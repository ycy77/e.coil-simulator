---
entity_id: "reaction.ecocyc.RXN-17636"
entity_type: "reaction"
name: "RXN-17636"
source_database: "EcoCyc"
source_id: "RXN-17636"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17636

`reaction.ecocyc.RXN-17636`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17636`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-Arginine-Imidazolidine -> Protein-Arginine-MGH1 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Protein-Arginine-Imidazolidine -> Protein-Arginine-MGH1 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: a [protein]-L-lysine-N-2-(4,5-dihydro-4-methyl-1H-imidazol-4,5-diol) (molecule.ecocyc.Protein-Arginine-Imidazolidine). Products: H2O (molecule.C00001), a [protein]-L-lysine-N-2-(4,5-dihydro-4-methyl-1H-imidazol-5-one) (molecule.ecocyc.Protein-Arginine-MGH1).

## Annotation

Protein-Arginine-Imidazolidine -> Protein-Arginine-MGH1 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-Arginine-MGH1|molecule.ecocyc.Protein-Arginine-MGH1]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-Arginine-Imidazolidine|molecule.ecocyc.Protein-Arginine-Imidazolidine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17636`

## Notes

Protein-Arginine-Imidazolidine -> Protein-Arginine-MGH1 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
