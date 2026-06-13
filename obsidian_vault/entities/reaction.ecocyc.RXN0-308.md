---
entity_id: "reaction.ecocyc.RXN0-308"
entity_type: "reaction"
name: "RXN0-308"
source_database: "EcoCyc"
source_id: "RXN0-308"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-308

`reaction.ecocyc.RXN0-308`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-308`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cysteine-Desulfurase-L-cysteine + CYS -> L-Cysteine-Desulfurase-persulfide + L-ALPHA-ALANINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Cysteine-Desulfurase-L-cysteine + CYS -> L-Cysteine-Desulfurase-persulfide + L-ALPHA-ALANINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cysteine desulfurase IscS (complex.ecocyc.CPLX0-248). Substrates: L-Cysteine (molecule.C00097), an [L-cysteine desulfurase]-L-cysteine (molecule.ecocyc.Cysteine-Desulfurase-L-cysteine). Products: L-Alanine (molecule.C00041), an [L-cysteine desulfurase]-S-sulfanyl-L-cysteine (molecule.ecocyc.L-Cysteine-Desulfurase-persulfide).

## Annotation

Cysteine-Desulfurase-L-cysteine + CYS -> L-Cysteine-Desulfurase-persulfide + L-ALPHA-ALANINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-248|complex.ecocyc.CPLX0-248]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-Cysteine-Desulfurase-persulfide|molecule.ecocyc.L-Cysteine-Desulfurase-persulfide]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Cysteine-Desulfurase-L-cysteine|molecule.ecocyc.Cysteine-Desulfurase-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-308`

## Notes

Cysteine-Desulfurase-L-cysteine + CYS -> L-Cysteine-Desulfurase-persulfide + L-ALPHA-ALANINE; direction=LEFT-TO-RIGHT
