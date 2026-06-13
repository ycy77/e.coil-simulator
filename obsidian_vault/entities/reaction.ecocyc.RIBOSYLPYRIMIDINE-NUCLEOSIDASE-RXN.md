---
entity_id: "reaction.ecocyc.RIBOSYLPYRIMIDINE-NUCLEOSIDASE-RXN"
entity_type: "reaction"
name: "RIBOSYLPYRIMIDINE-NUCLEOSIDASE-RXN"
source_database: "EcoCyc"
source_id: "RIBOSYLPYRIMIDINE-NUCLEOSIDASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBOSYLPYRIMIDINE-NUCLEOSIDASE-RXN

`reaction.ecocyc.RIBOSYLPYRIMIDINE-NUCLEOSIDASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBOSYLPYRIMIDINE-NUCLEOSIDASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pyrimidine-Nucleosides + WATER + PROTON -> Pyrimidine-Bases + D-Ribofuranose; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Pyrimidine-Nucleosides + WATER + PROTON -> Pyrimidine-Bases + D-Ribofuranose; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pyrimidine-specific ribonucleoside hydrolase RihB (complex.ecocyc.CPLX0-7904). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), a pyrimidine nucleoside (molecule.ecocyc.Pyrimidine-Nucleosides). Products: D-ribofuranose (molecule.ecocyc.D-Ribofuranose), a pyrimidine base (molecule.ecocyc.Pyrimidine-Bases).

## Annotation

Pyrimidine-Nucleosides + WATER + PROTON -> Pyrimidine-Bases + D-Ribofuranose; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7904|complex.ecocyc.CPLX0-7904]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.D-Ribofuranose|molecule.ecocyc.D-Ribofuranose]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pyrimidine-Bases|molecule.ecocyc.Pyrimidine-Bases]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pyrimidine-Nucleosides|molecule.ecocyc.Pyrimidine-Nucleosides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RIBOSYLPYRIMIDINE-NUCLEOSIDASE-RXN`

## Notes

Pyrimidine-Nucleosides + WATER + PROTON -> Pyrimidine-Bases + D-Ribofuranose; direction=PHYSIOL-LEFT-TO-RIGHT
