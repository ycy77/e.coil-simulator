---
entity_id: "reaction.ecocyc.RXN-17652"
entity_type: "reaction"
name: "RXN-17652"
source_database: "EcoCyc"
source_id: "RXN-17652"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17652

`reaction.ecocyc.RXN-17652`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17652`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ETR-Quinones + Protein-L-methionine + WATER -> ETR-Quinols + Protein-L-methionine-S-S-oxides; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: ETR-Quinones + Protein-L-methionine + WATER -> ETR-Quinols + Protein-L-methionine-S-S-oxides; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by periplasmic protein-L-methionine sulfoxide reducing system (complex.ecocyc.CPLX0-8213). Substrates: H2O (molecule.C00001), a [protein]-L-methionine (molecule.ecocyc.Protein-L-methionine). Products: a protein-L-methionine-(S)-S-oxide (molecule.ecocyc.Protein-L-methionine-S-S-oxides).

## Annotation

ETR-Quinones + Protein-L-methionine + WATER -> ETR-Quinols + Protein-L-methionine-S-S-oxides; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8213|complex.ecocyc.CPLX0-8213]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Protein-L-methionine-S-S-oxides|molecule.ecocyc.Protein-L-methionine-S-S-oxides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-L-methionine|molecule.ecocyc.Protein-L-methionine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17652`

## Notes

ETR-Quinones + Protein-L-methionine + WATER -> ETR-Quinols + Protein-L-methionine-S-S-oxides; direction=PHYSIOL-RIGHT-TO-LEFT
