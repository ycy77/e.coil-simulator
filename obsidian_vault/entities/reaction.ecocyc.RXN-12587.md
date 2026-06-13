---
entity_id: "reaction.ecocyc.RXN-12587"
entity_type: "reaction"
name: "RXN-12587"
source_database: "EcoCyc"
source_id: "RXN-12587"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12587

`reaction.ecocyc.RXN-12587`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12587`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Cysteine-Desulfurase-persulfide + Unsulfurated-Sulfur-Acceptors -> Cysteine-Desulfurase-L-cysteine + Sulfurated-Sulfur-Acceptors; direction=REVERSIBLE EcoCyc reaction equation: L-Cysteine-Desulfurase-persulfide + Unsulfurated-Sulfur-Acceptors -> Cysteine-Desulfurase-L-cysteine + Sulfurated-Sulfur-Acceptors; direction=REVERSIBLE.

## Biological Role

Catalyzed by cysteine desulfurase IscS (complex.ecocyc.CPLX0-248). Substrates: an [L-cysteine desulfurase]-S-sulfanyl-L-cysteine (molecule.ecocyc.L-Cysteine-Desulfurase-persulfide). Products: an [L-cysteine desulfurase]-L-cysteine (molecule.ecocyc.Cysteine-Desulfurase-L-cysteine).

## Annotation

L-Cysteine-Desulfurase-persulfide + Unsulfurated-Sulfur-Acceptors -> Cysteine-Desulfurase-L-cysteine + Sulfurated-Sulfur-Acceptors; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-248|complex.ecocyc.CPLX0-248]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Cysteine-Desulfurase-L-cysteine|molecule.ecocyc.Cysteine-Desulfurase-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.L-Cysteine-Desulfurase-persulfide|molecule.ecocyc.L-Cysteine-Desulfurase-persulfide]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12587`

## Notes

L-Cysteine-Desulfurase-persulfide + Unsulfurated-Sulfur-Acceptors -> Cysteine-Desulfurase-L-cysteine + Sulfurated-Sulfur-Acceptors; direction=REVERSIBLE
