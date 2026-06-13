---
entity_id: "reaction.ecocyc.ADENINE-DEAMINASE-RXN"
entity_type: "reaction"
name: "ADENINE-DEAMINASE-RXN"
source_database: "EcoCyc"
source_id: "ADENINE-DEAMINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Adenase"
  - "Adenine aminase"
---

# ADENINE-DEAMINASE-RXN

`reaction.ecocyc.ADENINE-DEAMINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADENINE-DEAMINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + WATER + ADENINE -> AMMONIUM + HYPOXANTHINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + WATER + ADENINE -> AMMONIUM + HYPOXANTHINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by adenine deaminase (complex.ecocyc.CPLX0-1683). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Adenine (molecule.C00147). Products: Hypoxanthine (molecule.C00262), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

PROTON + WATER + ADENINE -> AMMONIUM + HYPOXANTHINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1683|complex.ecocyc.CPLX0-1683]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00262|molecule.C00262]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-2383|molecule.ecocyc.CPD0-2383]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ADENINE-DEAMINASE-RXN`

## Notes

PROTON + WATER + ADENINE -> AMMONIUM + HYPOXANTHINE; direction=LEFT-TO-RIGHT
