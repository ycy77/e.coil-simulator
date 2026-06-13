---
entity_id: "reaction.ecocyc.RXN0-7165"
entity_type: "reaction"
name: "spermidine N8-acetyltransferase"
source_database: "EcoCyc"
source_id: "RXN0-7165"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# spermidine N8-acetyltransferase

`reaction.ecocyc.RXN0-7165`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7165`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this specific E.C. 2.3.1.57 reaction, spermidine is acetylated in response to cell stress. EcoCyc reaction equation: ACETYL-COA + SPERMIDINE -> CPD-3462 + PROTON + CO-A; direction=LEFT-TO-RIGHT. In this specific E.C. 2.3.1.57 reaction, spermidine is acetylated in response to cell stress.

## Biological Role

Catalyzed by spermidine N-acetyltransferase (complex.ecocyc.SPERMACTRAN-CPLX). Substrates: Acetyl-CoA (molecule.C00024), Spermidine (molecule.C00315). Products: CoA (molecule.C00010), H+ (molecule.C00080), N8-acetylspermidine (molecule.ecocyc.CPD-3462).

## Annotation

In this specific E.C. 2.3.1.57 reaction, spermidine is acetylated in response to cell stress.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.SPERMACTRAN-CPLX|complex.ecocyc.SPERMACTRAN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-3462|molecule.ecocyc.CPD-3462]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7165`

## Notes

ACETYL-COA + SPERMIDINE -> CPD-3462 + PROTON + CO-A; direction=LEFT-TO-RIGHT
