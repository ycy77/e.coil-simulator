---
entity_id: "reaction.ecocyc.SPERMACTRAN-RXN"
entity_type: "reaction"
name: "SPERMACTRAN-RXN"
source_database: "EcoCyc"
source_id: "SPERMACTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SPERMACTRAN-RXN

`reaction.ecocyc.SPERMACTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SPERMACTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this specific E.C. 2.3.1.57 reaction, spermidine is acetylated in response to cell stress. EcoCyc reaction equation: ACETYL-COA + SPERMIDINE -> CPD-568 + PROTON + CO-A; direction=LEFT-TO-RIGHT. In this specific E.C. 2.3.1.57 reaction, spermidine is acetylated in response to cell stress.

## Biological Role

Catalyzed by spermidine N-acetyltransferase (complex.ecocyc.SPERMACTRAN-CPLX). Substrates: Acetyl-CoA (molecule.C00024), Spermidine (molecule.C00315). Products: CoA (molecule.C00010), H+ (molecule.C00080), N1-acetylspermidine (molecule.ecocyc.CPD-568).

## Annotation

In this specific E.C. 2.3.1.57 reaction, spermidine is acetylated in response to cell stress.

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.SPERMACTRAN-CPLX|complex.ecocyc.SPERMACTRAN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-568|molecule.ecocyc.CPD-568]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1684|molecule.ecocyc.CPD0-1684]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1685|molecule.ecocyc.CPD0-1685]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:SPERMACTRAN-RXN`

## Notes

ACETYL-COA + SPERMIDINE -> CPD-568 + PROTON + CO-A; direction=LEFT-TO-RIGHT
