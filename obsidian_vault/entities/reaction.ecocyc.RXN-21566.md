---
entity_id: "reaction.ecocyc.RXN-21566"
entity_type: "reaction"
name: "RXN-21566"
source_database: "EcoCyc"
source_id: "RXN-21566"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21566

`reaction.ecocyc.RXN-21566`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21566`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CYS + Mo-bis-MGD-Chaperone-L-cysteine -> L-ALPHA-ALANINE + Mo-bis-MGD-Chaperone-Cys-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYS + Mo-bis-MGD-Chaperone-L-cysteine -> L-ALPHA-ALANINE + Mo-bis-MGD-Chaperone-Cys-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cysteine desulfurase IscS (complex.ecocyc.CPLX0-248). Substrates: L-Cysteine (molecule.C00097), a [bis(guanylyl molybdopterin) cofactor chaperone]-L-cysteine (molecule.ecocyc.Mo-bis-MGD-Chaperone-L-cysteine). Products: L-Alanine (molecule.C00041), a [bis(guanylyl molybdopterin) cofactor chaperone]-S-sulfanyl-L-cysteine (molecule.ecocyc.Mo-bis-MGD-Chaperone-Cys-Persulfide).

## Enriched Pathways

- `ecocyc.PWY-8164` bis(guanylyl molybdopterin) cofactor sulfurylation (EcoCyc)

## Annotation

CYS + Mo-bis-MGD-Chaperone-L-cysteine -> L-ALPHA-ALANINE + Mo-bis-MGD-Chaperone-Cys-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8164` bis(guanylyl molybdopterin) cofactor sulfurylation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-248|complex.ecocyc.CPLX0-248]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Mo-bis-MGD-Chaperone-Cys-Persulfide|molecule.ecocyc.Mo-bis-MGD-Chaperone-Cys-Persulfide]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Mo-bis-MGD-Chaperone-L-cysteine|molecule.ecocyc.Mo-bis-MGD-Chaperone-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21566`

## Notes

CYS + Mo-bis-MGD-Chaperone-L-cysteine -> L-ALPHA-ALANINE + Mo-bis-MGD-Chaperone-Cys-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT
