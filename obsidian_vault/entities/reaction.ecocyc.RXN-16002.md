---
entity_id: "reaction.ecocyc.RXN-16002"
entity_type: "reaction"
name: "RXN-16002"
source_database: "EcoCyc"
source_id: "RXN-16002"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16002

`reaction.ecocyc.RXN-16002`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16002`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-AMINOMALONATE-SEMIALDEHYDE + PROTON -> CPD-1772 + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 2-AMINOMALONATE-SEMIALDEHYDE + PROTON -> CPD-1772 + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), 3-oxo-L-alanine (molecule.ecocyc.2-AMINOMALONATE-SEMIALDEHYDE). Products: CO2 (molecule.C00011), Aminoacetaldehyde (molecule.C06735).

## Annotation

2-AMINOMALONATE-SEMIALDEHYDE + PROTON -> CPD-1772 + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06735|molecule.C06735]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.2-AMINOMALONATE-SEMIALDEHYDE|molecule.ecocyc.2-AMINOMALONATE-SEMIALDEHYDE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16002`

## Notes

2-AMINOMALONATE-SEMIALDEHYDE + PROTON -> CPD-1772 + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
