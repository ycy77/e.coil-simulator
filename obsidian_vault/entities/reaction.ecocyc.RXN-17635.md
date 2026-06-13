---
entity_id: "reaction.ecocyc.RXN-17635"
entity_type: "reaction"
name: "RXN-17635"
source_database: "EcoCyc"
source_id: "RXN-17635"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17635

`reaction.ecocyc.RXN-17635`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17635`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-Arginine-Aminocarbinol -> Protein-Arginine-Imidazolidine + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Protein-Arginine-Aminocarbinol -> Protein-Arginine-Imidazolidine + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: an Nω-(1-hydroxy-2-oxopropyl)-[protein]-L-arginine (molecule.ecocyc.Protein-Arginine-Aminocarbinol). Products: H+ (molecule.C00080), a [protein]-L-lysine-N-2-(4,5-dihydro-4-methyl-1H-imidazol-4,5-diol) (molecule.ecocyc.Protein-Arginine-Imidazolidine).

## Annotation

Protein-Arginine-Aminocarbinol -> Protein-Arginine-Imidazolidine + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-Arginine-Imidazolidine|molecule.ecocyc.Protein-Arginine-Imidazolidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-Arginine-Aminocarbinol|molecule.ecocyc.Protein-Arginine-Aminocarbinol]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17635`

## Notes

Protein-Arginine-Aminocarbinol -> Protein-Arginine-Imidazolidine + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
