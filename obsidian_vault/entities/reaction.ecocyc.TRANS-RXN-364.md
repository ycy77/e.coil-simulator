---
entity_id: "reaction.ecocyc.TRANS-RXN-364"
entity_type: "reaction"
name: "carbonylcyanide m-chlorophenylhydrazone export"
source_database: "EcoCyc"
source_id: "TRANS-RXN-364"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# carbonylcyanide m-chlorophenylhydrazone export

`reaction.ecocyc.TRANS-RXN-364`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-364`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

CPD-7970 + PROTON -> CPD-7970 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-7970 + PROTON -> CPD-7970 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multidrug efflux pump EmrAB-TolC (complex.ecocyc.CPLX0-2121). Substrates: H+ (molecule.C00080), carbonylcyanide m-chlorophenylhydrazone (molecule.ecocyc.CPD-7970). Products: H+ (molecule.C00080), carbonylcyanide m-chlorophenylhydrazone (molecule.ecocyc.CPD-7970).

## Annotation

CPD-7970 + PROTON -> CPD-7970 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2121|complex.ecocyc.CPLX0-2121]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-364`

## Notes

CPD-7970 + PROTON -> CPD-7970 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
