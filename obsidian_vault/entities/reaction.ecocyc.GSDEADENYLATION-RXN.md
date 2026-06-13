---
entity_id: "reaction.ecocyc.GSDEADENYLATION-RXN"
entity_type: "reaction"
name: "GSDEADENYLATION-RXN"
source_database: "EcoCyc"
source_id: "GSDEADENYLATION-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GSDEADENYLATION-RXN

`reaction.ecocyc.GSDEADENYLATION-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GSDEADENYLATION-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL

## Enriched Summary

This reaction deadenylylates glutamine synthetase returning it to its active form. EcoCyc reaction equation: Glutamine-synthetase-adenylyl-Tyr + Pi -> Glutamine-synthetase-Tyr + ADP; direction=LEFT-TO-RIGHT. This reaction deadenylylates glutamine synthetase returning it to its active form.

## Biological Role

Catalyzed by glnE (protein.P30870). Substrates: a [glutamine synthetase]-O4-(5'-adenylyl)-L-tyrosine (molecule.ecocyc.Glutamine-synthetase-adenylyl-Tyr), phosphate (molecule.ecocyc.Pi). Products: ADP (molecule.C00008), a [glutamine-synthetase]-L-tyrosine (molecule.ecocyc.Glutamine-synthetase-Tyr).

## Annotation

This reaction deadenylylates glutamine synthetase returning it to its active form.

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `activates` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.ARSENATE|molecule.ecocyc.ARSENATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P30870|protein.P30870]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Glutamine-synthetase-Tyr|molecule.ecocyc.Glutamine-synthetase-Tyr]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Glutamine-synthetase-adenylyl-Tyr|molecule.ecocyc.Glutamine-synthetase-adenylyl-Tyr]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GSDEADENYLATION-RXN`

## Notes

Glutamine-synthetase-adenylyl-Tyr + Pi -> Glutamine-synthetase-Tyr + ADP; direction=LEFT-TO-RIGHT
