---
entity_id: "reaction.ecocyc.RXN0-7397"
entity_type: "reaction"
name: "RXN0-7397"
source_database: "EcoCyc"
source_id: "RXN0-7397"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7397

`reaction.ecocyc.RXN0-7397`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7397`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + 5-ppp-RiboNuc-mRNA + PROTON -> A-5-prime-Ap4-capped-RNA + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + 5-ppp-RiboNuc-mRNA + PROTON -> A-5-prime-Ap4-capped-RNA + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lysine—tRNA ligase (complex.ecocyc.LYSU-CPLX). Substrates: ATP (molecule.C00002), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013).

## Annotation

ATP + 5-ppp-RiboNuc-mRNA + PROTON -> A-5-prime-Ap4-capped-RNA + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.LYSU-CPLX|complex.ecocyc.LYSU-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7397`

## Notes

ATP + 5-ppp-RiboNuc-mRNA + PROTON -> A-5-prime-Ap4-capped-RNA + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
