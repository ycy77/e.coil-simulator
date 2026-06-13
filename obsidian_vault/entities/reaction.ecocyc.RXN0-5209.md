---
entity_id: "reaction.ecocyc.RXN0-5209"
entity_type: "reaction"
name: "RXN0-5209"
source_database: "EcoCyc"
source_id: "RXN0-5209"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5209

`reaction.ecocyc.RXN0-5209`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5209`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + ATP + ADP -> ADENOSINE5TRIPHOSPHO5ADENOSINE + PPI; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + ATP + ADP -> ADENOSINE5TRIPHOSPHO5ADENOSINE + PPI; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lysine—tRNA ligase (complex.ecocyc.LYSU-CPLX). Substrates: ATP (molecule.C00002), ADP (molecule.C00008), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), P1,P3-Bis(5'-adenosyl) triphosphate (molecule.C06197).

## Annotation

PROTON + ATP + ADP -> ADENOSINE5TRIPHOSPHO5ADENOSINE + PPI; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.LYSU-CPLX|complex.ecocyc.LYSU-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06197|molecule.C06197]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5209`

## Notes

PROTON + ATP + ADP -> ADENOSINE5TRIPHOSPHO5ADENOSINE + PPI; direction=LEFT-TO-RIGHT
