---
entity_id: "reaction.ecocyc.GUANINE-DEAMINASE-RXN"
entity_type: "reaction"
name: "GUANINE-DEAMINASE-RXN"
source_database: "EcoCyc"
source_id: "GUANINE-DEAMINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "GUANINE AMINASE"
  - "GUANASE"
---

# GUANINE-DEAMINASE-RXN

`reaction.ecocyc.GUANINE-DEAMINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GUANINE-DEAMINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + WATER + GUANINE -> XANTHINE + AMMONIUM; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + WATER + GUANINE -> XANTHINE + AMMONIUM; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by guaD (protein.P76641). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Guanine (molecule.C00242). Products: Xanthine (molecule.C00385), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY-6608` guanosine nucleotides degradation III (EcoCyc)

## Annotation

PROTON + WATER + GUANINE -> XANTHINE + AMMONIUM; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6608` guanosine nucleotides degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P76641|protein.P76641]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00385|molecule.C00385]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00242|molecule.C00242]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GUANINE-DEAMINASE-RXN`

## Notes

PROTON + WATER + GUANINE -> XANTHINE + AMMONIUM; direction=LEFT-TO-RIGHT
