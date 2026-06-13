---
entity_id: "reaction.ecocyc.GSADENYLATION-RXN"
entity_type: "reaction"
name: "GSADENYLATION-RXN"
source_database: "EcoCyc"
source_id: "GSADENYLATION-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GSADENYLATION-RXN

`reaction.ecocyc.GSADENYLATION-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GSADENYLATION-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction adenylylates glutamine synthetase, subunits on tyrosine-397, resulting in the inactivation of the synthetase. EcoCyc reaction equation: Glutamine-synthetase-Tyr + ATP -> Glutamine-synthetase-adenylyl-Tyr + PPI; direction=LEFT-TO-RIGHT. This reaction adenylylates glutamine synthetase, subunits on tyrosine-397, resulting in the inactivation of the synthetase.

## Biological Role

Catalyzed by glnE (protein.P30870). Substrates: ATP (molecule.C00002), a [glutamine-synthetase]-L-tyrosine (molecule.ecocyc.Glutamine-synthetase-Tyr). Products: Diphosphate (molecule.C00013), a [glutamine synthetase]-O4-(5'-adenylyl)-L-tyrosine (molecule.ecocyc.Glutamine-synthetase-adenylyl-Tyr).

## Annotation

This reaction adenylylates glutamine synthetase, subunits on tyrosine-397, resulting in the inactivation of the synthetase.

## Outgoing Edges (0)

_None._

## Incoming Edges (19)

- `activates` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P0A9Z1|protein.P0A9Z1]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P30870|protein.P30870]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Glutamine-synthetase-adenylyl-Tyr|molecule.ecocyc.Glutamine-synthetase-adenylyl-Tyr]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Glutamine-synthetase-Tyr|molecule.ecocyc.Glutamine-synthetase-Tyr]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00059|molecule.C00059]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00197|molecule.C00197]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00354|molecule.C00354]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GSADENYLATION-RXN`

## Notes

Glutamine-synthetase-Tyr + ATP -> Glutamine-synthetase-adenylyl-Tyr + PPI; direction=LEFT-TO-RIGHT
