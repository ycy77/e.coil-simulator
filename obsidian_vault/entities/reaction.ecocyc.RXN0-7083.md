---
entity_id: "reaction.ecocyc.RXN0-7083"
entity_type: "reaction"
name: "RXN0-7083"
source_database: "EcoCyc"
source_id: "RXN0-7083"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7083

`reaction.ecocyc.RXN0-7083`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7083`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA-2-thiouridine34 + METHYLENE-THF-GLU-N + AMMONIUM + GTP + WATER + Acceptor -> tRNA-Containing-5AminoMe-2-ThioUrdines + DIHYDROFOLATE-GLU-N + GDP + Pi + Donor-H2 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: tRNA-2-thiouridine34 + METHYLENE-THF-GLU-N + AMMONIUM + GTP + WATER + Acceptor -> tRNA-Containing-5AminoMe-2-ThioUrdines + DIHYDROFOLATE-GLU-N + GDP + Pi + Donor-H2 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 5-carboxymethylaminomethyluridine-tRNA synthase [multifunctional] (complex.ecocyc.CPLX0-7609). Substrates: H2O (molecule.C00001), GTP (molecule.C00044), ammonium (molecule.ecocyc.AMMONIUM), a 5,10-methylenetetrahydrofolate (molecule.ecocyc.METHYLENE-THF-GLU-N), a 2-thiouridine34 in tRNA (molecule.ecocyc.tRNA-2-thiouridine34). Products: GDP (molecule.C00035), H+ (molecule.C00080), a 7,8-dihydrofolate (molecule.ecocyc.DIHYDROFOLATE-GLU-N), phosphate (molecule.ecocyc.Pi), a 5-(aminomethyl)-2-thiouridine34 in tRNA (molecule.ecocyc.tRNA-Containing-5AminoMe-2-ThioUrdines).

## Annotation

tRNA-2-thiouridine34 + METHYLENE-THF-GLU-N + AMMONIUM + GTP + WATER + Acceptor -> tRNA-Containing-5AminoMe-2-ThioUrdines + DIHYDROFOLATE-GLU-N + GDP + Pi + Donor-H2 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7609|complex.ecocyc.CPLX0-7609]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DIHYDROFOLATE-GLU-N|molecule.ecocyc.DIHYDROFOLATE-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNA-Containing-5AminoMe-2-ThioUrdines|molecule.ecocyc.tRNA-Containing-5AminoMe-2-ThioUrdines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.METHYLENE-THF-GLU-N|molecule.ecocyc.METHYLENE-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-2-thiouridine34|molecule.ecocyc.tRNA-2-thiouridine34]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7083`

## Notes

tRNA-2-thiouridine34 + METHYLENE-THF-GLU-N + AMMONIUM + GTP + WATER + Acceptor -> tRNA-Containing-5AminoMe-2-ThioUrdines + DIHYDROFOLATE-GLU-N + GDP + Pi + Donor-H2 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
