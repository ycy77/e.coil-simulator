---
entity_id: "reaction.ecocyc.RXN-21550"
entity_type: "reaction"
name: "RXN-21550"
source_database: "EcoCyc"
source_id: "RXN-21550"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21550

`reaction.ecocyc.RXN-21550`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21550`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Loaded-Mo-bis-MGD-Chaperones + Mo-bis-MGD-Chaperone-Cys-Persulfide + Donor-H2 -> Mo-bis-MGD-Chaperone-L-cysteine + CPD-23449 + WATER + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Loaded-Mo-bis-MGD-Chaperones + Mo-bis-MGD-Chaperone-Cys-Persulfide + Donor-H2 -> Mo-bis-MGD-Chaperone-L-cysteine + CPD-23449 + WATER + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by sulfurtransferase for molybdenum cofactor sulfuration (complex.ecocyc.CPLX0-8175). Substrates: a [bis(guanylyl molybdopterin) cofactor chaperone]-S-sulfanyl-L-cysteine (molecule.ecocyc.Mo-bis-MGD-Chaperone-Cys-Persulfide). Products: H2O (molecule.C00001), sulfo-bis(guanylyl molybdopterin) cofactor (molecule.ecocyc.CPD-23449), a [bis(guanylyl molybdopterin) cofactor chaperone]-L-cysteine (molecule.ecocyc.Mo-bis-MGD-Chaperone-L-cysteine).

## Enriched Pathways

- `ecocyc.PWY-8164` bis(guanylyl molybdopterin) cofactor sulfurylation (EcoCyc)

## Annotation

Loaded-Mo-bis-MGD-Chaperones + Mo-bis-MGD-Chaperone-Cys-Persulfide + Donor-H2 -> Mo-bis-MGD-Chaperone-L-cysteine + CPD-23449 + WATER + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8164` bis(guanylyl molybdopterin) cofactor sulfurylation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8175|complex.ecocyc.CPLX0-8175]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-23449|molecule.ecocyc.CPD-23449]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Mo-bis-MGD-Chaperone-L-cysteine|molecule.ecocyc.Mo-bis-MGD-Chaperone-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Mo-bis-MGD-Chaperone-Cys-Persulfide|molecule.ecocyc.Mo-bis-MGD-Chaperone-Cys-Persulfide]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21550`

## Notes

Loaded-Mo-bis-MGD-Chaperones + Mo-bis-MGD-Chaperone-Cys-Persulfide + Donor-H2 -> Mo-bis-MGD-Chaperone-L-cysteine + CPD-23449 + WATER + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT
