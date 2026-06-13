---
entity_id: "reaction.ecocyc.RXN-21565"
entity_type: "reaction"
name: "RXN-21565"
source_database: "EcoCyc"
source_id: "RXN-21565"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21565

`reaction.ecocyc.RXN-21565`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21565`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Cysteine-Desulfurase-persulfide + Mo-bis-MGD-Chaperone-L-cysteine -> Cysteine-Desulfurase-L-cysteine + Mo-bis-MGD-Chaperone-Cys-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-Cysteine-Desulfurase-persulfide + Mo-bis-MGD-Chaperone-L-cysteine -> Cysteine-Desulfurase-L-cysteine + Mo-bis-MGD-Chaperone-Cys-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: an [L-cysteine desulfurase]-S-sulfanyl-L-cysteine (molecule.ecocyc.L-Cysteine-Desulfurase-persulfide), a [bis(guanylyl molybdopterin) cofactor chaperone]-L-cysteine (molecule.ecocyc.Mo-bis-MGD-Chaperone-L-cysteine). Products: an [L-cysteine desulfurase]-L-cysteine (molecule.ecocyc.Cysteine-Desulfurase-L-cysteine), a [bis(guanylyl molybdopterin) cofactor chaperone]-S-sulfanyl-L-cysteine (molecule.ecocyc.Mo-bis-MGD-Chaperone-Cys-Persulfide).

## Annotation

L-Cysteine-Desulfurase-persulfide + Mo-bis-MGD-Chaperone-L-cysteine -> Cysteine-Desulfurase-L-cysteine + Mo-bis-MGD-Chaperone-Cys-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.Cysteine-Desulfurase-L-cysteine|molecule.ecocyc.Cysteine-Desulfurase-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Mo-bis-MGD-Chaperone-Cys-Persulfide|molecule.ecocyc.Mo-bis-MGD-Chaperone-Cys-Persulfide]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.L-Cysteine-Desulfurase-persulfide|molecule.ecocyc.L-Cysteine-Desulfurase-persulfide]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Mo-bis-MGD-Chaperone-L-cysteine|molecule.ecocyc.Mo-bis-MGD-Chaperone-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21565`

## Notes

L-Cysteine-Desulfurase-persulfide + Mo-bis-MGD-Chaperone-L-cysteine -> Cysteine-Desulfurase-L-cysteine + Mo-bis-MGD-Chaperone-Cys-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT
