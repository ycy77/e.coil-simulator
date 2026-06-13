---
entity_id: "reaction.ecocyc.RXN0-7438"
entity_type: "reaction"
name: "RXN0-7438"
source_database: "EcoCyc"
source_id: "RXN0-7438"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7438

`reaction.ecocyc.RXN0-7438`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7438`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CYS + SufS-L-cysteine -> SufS-L-cysteine-Persulfide + L-ALPHA-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYS + SufS-L-cysteine -> SufS-L-cysteine-Persulfide + L-ALPHA-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Cysteine (molecule.C00097), a [SufS]-L-cysteine (molecule.ecocyc.SufS-L-cysteine). Products: L-Alanine (molecule.C00041), a [SufS L-cysteine desulfurase]-S-sulfanyl-L-cysteine (molecule.ecocyc.SufS-L-cysteine-Persulfide).

## Annotation

CYS + SufS-L-cysteine -> SufS-L-cysteine-Persulfide + L-ALPHA-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.SufS-L-cysteine-Persulfide|molecule.ecocyc.SufS-L-cysteine-Persulfide]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.SufS-L-cysteine|molecule.ecocyc.SufS-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7438`

## Notes

CYS + SufS-L-cysteine -> SufS-L-cysteine-Persulfide + L-ALPHA-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT
