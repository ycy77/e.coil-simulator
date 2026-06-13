---
entity_id: "reaction.ecocyc.RXN-14382"
entity_type: "reaction"
name: "RXN-14382"
source_database: "EcoCyc"
source_id: "RXN-14382"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14382

`reaction.ecocyc.RXN-14382`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14382`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Cysteine-Desulfurase-persulfide + Sulfur-Carrier-Proteins-ThiI -> Cysteine-Desulfurase-L-cysteine + Sulfurylated-ThiI; direction= EcoCyc reaction equation: L-Cysteine-Desulfurase-persulfide + Sulfur-Carrier-Proteins-ThiI -> Cysteine-Desulfurase-L-cysteine + Sulfurylated-ThiI; direction=.

## Biological Role

Catalyzed by cysteine desulfurase IscS (complex.ecocyc.CPLX0-248). Substrates: an [L-cysteine desulfurase]-S-sulfanyl-L-cysteine (molecule.ecocyc.L-Cysteine-Desulfurase-persulfide). Products: an [L-cysteine desulfurase]-L-cysteine (molecule.ecocyc.Cysteine-Desulfurase-L-cysteine).

## Annotation

L-Cysteine-Desulfurase-persulfide + Sulfur-Carrier-Proteins-ThiI -> Cysteine-Desulfurase-L-cysteine + Sulfurylated-ThiI; direction=

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-248|complex.ecocyc.CPLX0-248]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Cysteine-Desulfurase-L-cysteine|molecule.ecocyc.Cysteine-Desulfurase-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.L-Cysteine-Desulfurase-persulfide|molecule.ecocyc.L-Cysteine-Desulfurase-persulfide]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14382`

## Notes

L-Cysteine-Desulfurase-persulfide + Sulfur-Carrier-Proteins-ThiI -> Cysteine-Desulfurase-L-cysteine + Sulfurylated-ThiI; direction=
