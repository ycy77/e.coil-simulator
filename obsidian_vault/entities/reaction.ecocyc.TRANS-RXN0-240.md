---
entity_id: "reaction.ecocyc.TRANS-RXN0-240"
entity_type: "reaction"
name: "TRANS-RXN0-240"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-240"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-240

`reaction.ecocyc.TRANS-RXN0-240`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-240`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Biotin is transported into E. coli by an energy-dependent mechanism that in strain Y10-1 is inhibited by uncouplers, has pH and temperature optimums of 6.6 and 37 degrees C, respectively, and has a Km and Vmax of 0.14 μM and 6.6 pmol per mg per min., respectively . EcoCyc reaction equation: BIOTIN -> BIOTIN; direction=LEFT-TO-RIGHT. Biotin is transported into E. coli by an energy-dependent mechanism that in strain Y10-1 is inhibited by uncouplers, has pH and temperature optimums of 6.6 and 37 degrees C, respectively, and has a Km and Vmax of 0.14 μM and 6.6 pmol per mg per min., respectively .

## Biological Role

Catalyzed by bioP (protein.P0ADP5). Substrates: Biotin (molecule.C00120). Products: Biotin (molecule.C00120).

## Annotation

Biotin is transported into E. coli by an energy-dependent mechanism that in strain Y10-1 is inhibited by uncouplers, has pH and temperature optimums of 6.6 and 37 degrees C, respectively, and has a Km and Vmax of 0.14 μM and 6.6 pmol per mg per min., respectively .

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0ADP5|protein.P0ADP5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00120|molecule.C00120]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00120|molecule.C00120]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01326|molecule.C01326]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-2841|molecule.ecocyc.CPD-2841]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-8179|molecule.ecocyc.CPD-8179]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETATE|molecule.ecocyc.IODOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-240`

## Notes

BIOTIN -> BIOTIN; direction=LEFT-TO-RIGHT
