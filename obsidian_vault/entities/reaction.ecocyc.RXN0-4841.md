---
entity_id: "reaction.ecocyc.RXN0-4841"
entity_type: "reaction"
name: "RXN0-4841"
source_database: "EcoCyc"
source_id: "RXN0-4841"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4841

`reaction.ecocyc.RXN0-4841`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4841`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FRUCTOSELYSINE -> PSICOSELYSINE; direction=REVERSIBLE EcoCyc reaction equation: FRUCTOSELYSINE -> PSICOSELYSINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by fructoselysine 3-epimerase (complex.ecocyc.CPLX0-3861). Substrates: Fructoselysine (molecule.C16488). Products: N6-(D-psicosyl)-L-lysine (molecule.ecocyc.PSICOSELYSINE).

## Enriched Pathways

- `ecocyc.PWY0-521` fructoselysine and psicoselysine degradation (EcoCyc)

## Annotation

FRUCTOSELYSINE -> PSICOSELYSINE; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-521` fructoselysine and psicoselysine degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `activates` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3861|complex.ecocyc.CPLX0-3861]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.PSICOSELYSINE|molecule.ecocyc.PSICOSELYSINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C16488|molecule.C16488]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-4841`

## Notes

FRUCTOSELYSINE -> PSICOSELYSINE; direction=REVERSIBLE
