---
entity_id: "reaction.ecocyc.RXN-18707"
entity_type: "reaction"
name: "RXN-18707"
source_database: "EcoCyc"
source_id: "RXN-18707"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18707

`reaction.ecocyc.RXN-18707`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18707`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Cysteine-Desulfurase-persulfide + TusA-L-cysteine -> Cysteine-Desulfurase-L-cysteine + TusA-Persulfides; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-Cysteine-Desulfurase-persulfide + TusA-L-cysteine -> Cysteine-Desulfurase-L-cysteine + TusA-Persulfides; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: an [L-cysteine desulfurase]-S-sulfanyl-L-cysteine (molecule.ecocyc.L-Cysteine-Desulfurase-persulfide), a [TusA]-L-cysteine (molecule.ecocyc.TusA-L-cysteine). Products: an [L-cysteine desulfurase]-L-cysteine (molecule.ecocyc.Cysteine-Desulfurase-L-cysteine), a [TusA sulfur-carrier protein]-S-sulfanyl-L-cysteine (molecule.ecocyc.TusA-Persulfides).

## Annotation

L-Cysteine-Desulfurase-persulfide + TusA-L-cysteine -> Cysteine-Desulfurase-L-cysteine + TusA-Persulfides; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.Cysteine-Desulfurase-L-cysteine|molecule.ecocyc.Cysteine-Desulfurase-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.TusA-Persulfides|molecule.ecocyc.TusA-Persulfides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.L-Cysteine-Desulfurase-persulfide|molecule.ecocyc.L-Cysteine-Desulfurase-persulfide]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.TusA-L-cysteine|molecule.ecocyc.TusA-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18707`

## Notes

L-Cysteine-Desulfurase-persulfide + TusA-L-cysteine -> Cysteine-Desulfurase-L-cysteine + TusA-Persulfides; direction=PHYSIOL-LEFT-TO-RIGHT
