---
entity_id: "reaction.ecocyc.RXN-17629"
entity_type: "reaction"
name: "RXN-17629"
source_database: "EcoCyc"
source_id: "RXN-17629"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17629

`reaction.ecocyc.RXN-17629`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17629`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

METHYL-GLYOXAL + Protein-L-Arginines -> Protein-Arginine-Aminocarbinol; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: METHYL-GLYOXAL + Protein-L-Arginines -> Protein-Arginine-Aminocarbinol; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Methylglyoxal (molecule.C00546), a [protein]-L-arginine (molecule.ecocyc.Protein-L-Arginines). Products: an Nω-(1-hydroxy-2-oxopropyl)-[protein]-L-arginine (molecule.ecocyc.Protein-Arginine-Aminocarbinol).

## Annotation

METHYL-GLYOXAL + Protein-L-Arginines -> Protein-Arginine-Aminocarbinol; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.Protein-Arginine-Aminocarbinol|molecule.ecocyc.Protein-Arginine-Aminocarbinol]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00546|molecule.C00546]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-L-Arginines|molecule.ecocyc.Protein-L-Arginines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17629`

## Notes

METHYL-GLYOXAL + Protein-L-Arginines -> Protein-Arginine-Aminocarbinol; direction=PHYSIOL-LEFT-TO-RIGHT
