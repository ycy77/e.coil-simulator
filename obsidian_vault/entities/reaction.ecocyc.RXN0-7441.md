---
entity_id: "reaction.ecocyc.RXN0-7441"
entity_type: "reaction"
name: "RXN0-7441"
source_database: "EcoCyc"
source_id: "RXN0-7441"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7441

`reaction.ecocyc.RXN0-7441`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7441`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Selenocysteine-Lyase-S-selanyl-L-Cysteine + Selenium-Carrier-Protein-L-Cysteine -> Selenocysteine-Lyase-L-Cysteine + Selenium-Carrier-Protein-S-selanyl-L-Cysteine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Selenocysteine-Lyase-S-selanyl-L-Cysteine + Selenium-Carrier-Protein-L-Cysteine -> Selenocysteine-Lyase-L-Cysteine + Selenium-Carrier-Protein-S-selanyl-L-Cysteine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: a [selenium-carrier protein]-L-cysteine (molecule.ecocyc.Selenium-Carrier-Protein-L-Cysteine), a [selenocysteine lyase]-S-selenopersulfide (molecule.ecocyc.Selenocysteine-Lyase-S-selanyl-L-Cysteine). Products: a [selenium-carrier protein]-S-selenopersulfide (molecule.ecocyc.Selenium-Carrier-Protein-S-selanyl-L-Cysteine), a [selenocysteine lyase]-L-cysteine (molecule.ecocyc.Selenocysteine-Lyase-L-Cysteine).

## Annotation

Selenocysteine-Lyase-S-selanyl-L-Cysteine + Selenium-Carrier-Protein-L-Cysteine -> Selenocysteine-Lyase-L-Cysteine + Selenium-Carrier-Protein-S-selanyl-L-Cysteine; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.Selenium-Carrier-Protein-S-selanyl-L-Cysteine|molecule.ecocyc.Selenium-Carrier-Protein-S-selanyl-L-Cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Selenocysteine-Lyase-L-Cysteine|molecule.ecocyc.Selenocysteine-Lyase-L-Cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Selenium-Carrier-Protein-L-Cysteine|molecule.ecocyc.Selenium-Carrier-Protein-L-Cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Selenocysteine-Lyase-S-selanyl-L-Cysteine|molecule.ecocyc.Selenocysteine-Lyase-S-selanyl-L-Cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7441`

## Notes

Selenocysteine-Lyase-S-selanyl-L-Cysteine + Selenium-Carrier-Protein-L-Cysteine -> Selenocysteine-Lyase-L-Cysteine + Selenium-Carrier-Protein-S-selanyl-L-Cysteine; direction=PHYSIOL-LEFT-TO-RIGHT
