---
entity_id: "reaction.ecocyc.RXN-20019"
entity_type: "reaction"
name: "RXN-20019"
source_database: "EcoCyc"
source_id: "RXN-20019"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20019

`reaction.ecocyc.RXN-20019`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20019`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

PROTEIN-S-HYDROXY-CYSTEINE -> PROT-CYS; direction=REVERSIBLE EcoCyc reaction equation: PROTEIN-S-HYDROXY-CYSTEINE -> PROT-CYS; direction=REVERSIBLE.

## Biological Role

Catalyzed by protein sulfenic acid reductase and chaperone DsbG (complex.ecocyc.DSBG-CPLX). Substrates: a [protein]-S-hydroxy-L-cysteine (molecule.ecocyc.PROTEIN-S-HYDROXY-CYSTEINE). Products: a [protein]-L-cysteine (molecule.ecocyc.PROT-CYS).

## Annotation

PROTEIN-S-HYDROXY-CYSTEINE -> PROT-CYS; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.DSBG-CPLX|complex.ecocyc.DSBG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.PROT-CYS|molecule.ecocyc.PROT-CYS]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.PROTEIN-S-HYDROXY-CYSTEINE|molecule.ecocyc.PROTEIN-S-HYDROXY-CYSTEINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20019`

## Notes

PROTEIN-S-HYDROXY-CYSTEINE -> PROT-CYS; direction=REVERSIBLE
