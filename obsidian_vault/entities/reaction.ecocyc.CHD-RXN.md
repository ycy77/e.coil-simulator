---
entity_id: "reaction.ecocyc.CHD-RXN"
entity_type: "reaction"
name: "CHD-RXN"
source_database: "EcoCyc"
source_id: "CHD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CHD-RXN

`reaction.ecocyc.CHD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CHD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in the betaine biosynthetic pathway. EcoCyc reaction equation: CHOLINE + Acceptor -> BETAINE_ALDEHYDE + Donor-H2; direction=REVERSIBLE. This is the first reaction in the betaine biosynthetic pathway.

## Biological Role

Catalyzed by betA (protein.P17444). Substrates: Choline (molecule.C00114). Products: Betaine aldehyde (molecule.C00576).

## Enriched Pathways

- `ecocyc.BETSYN-PWY` glycine betaine biosynthesis I (Gram-negative bacteria) (EcoCyc)

## Annotation

This is the first reaction in the betaine biosynthetic pathway.

## Pathways

- `ecocyc.BETSYN-PWY` glycine betaine biosynthesis I (Gram-negative bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P17444|protein.P17444]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00576|molecule.C00576]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00114|molecule.C00114]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CHD-RXN`

## Notes

CHOLINE + Acceptor -> BETAINE_ALDEHYDE + Donor-H2; direction=REVERSIBLE
