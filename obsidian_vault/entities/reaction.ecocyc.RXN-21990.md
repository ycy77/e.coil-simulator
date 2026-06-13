---
entity_id: "reaction.ecocyc.RXN-21990"
entity_type: "reaction"
name: "RXN-21990"
source_database: "EcoCyc"
source_id: "RXN-21990"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21990

`reaction.ecocyc.RXN-21990`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21990`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PREPHENATE + 23S-rRNA-cytosine-2501 + Acceptor + PROTON -> PHENYL-PYRUVATE + 5-Hydroxy-23S-rRNA-Cytosines2501 + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PREPHENATE + 23S-rRNA-cytosine-2501 + Acceptor + PROTON -> PHENYL-PYRUVATE + 5-Hydroxy-23S-rRNA-Cytosines2501 + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rlhA (protein.P76104). Substrates: H+ (molecule.C00080), Prephenate (molecule.C00254), a cytosine2501 in 23S rRNA (molecule.ecocyc.23S-rRNA-cytosine-2501). Products: CO2 (molecule.C00011), Phenylpyruvate (molecule.C00166), a 5-hydroxycytosine2501 in 23S rRNA (molecule.ecocyc.5-Hydroxy-23S-rRNA-Cytosines2501).

## Annotation

PREPHENATE + 23S-rRNA-cytosine-2501 + Acceptor + PROTON -> PHENYL-PYRUVATE + 5-Hydroxy-23S-rRNA-Cytosines2501 + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P76104|protein.P76104]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00166|molecule.C00166]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-Hydroxy-23S-rRNA-Cytosines2501|molecule.ecocyc.5-Hydroxy-23S-rRNA-Cytosines2501]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00254|molecule.C00254]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-cytosine-2501|molecule.ecocyc.23S-rRNA-cytosine-2501]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21990`

## Notes

PREPHENATE + 23S-rRNA-cytosine-2501 + Acceptor + PROTON -> PHENYL-PYRUVATE + 5-Hydroxy-23S-rRNA-Cytosines2501 + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT
