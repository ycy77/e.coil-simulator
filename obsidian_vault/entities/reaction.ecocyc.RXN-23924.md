---
entity_id: "reaction.ecocyc.RXN-23924"
entity_type: "reaction"
name: "RXN-23924"
source_database: "EcoCyc"
source_id: "RXN-23924"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23924

`reaction.ecocyc.RXN-23924`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23924`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HOMO-CYS + ATP -> CPD-22841 + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HOMO-CYS + ATP -> CPD-22841 + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lysine—tRNA ligase (complex.ecocyc.LYSU-CPLX), methionine—tRNA ligase (complex.ecocyc.METG-CPLX), ileS (protein.P00956), valS (protein.P07118). Substrates: ATP (molecule.C00002), L-Homocysteine (molecule.C00155). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-homocysteine thiolactone (molecule.ecocyc.CPD-22841).

## Annotation

HOMO-CYS + ATP -> CPD-22841 + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.LYSU-CPLX|complex.ecocyc.LYSU-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.METG-CPLX|complex.ecocyc.METG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P00956|protein.P00956]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P07118|protein.P07118]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22841|molecule.ecocyc.CPD-22841]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00155|molecule.C00155]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23924`

## Notes

HOMO-CYS + ATP -> CPD-22841 + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
