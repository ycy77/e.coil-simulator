---
entity_id: "reaction.ecocyc.RXN-19922"
entity_type: "reaction"
name: "RXN-19922"
source_database: "EcoCyc"
source_id: "RXN-19922"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19922

`reaction.ecocyc.RXN-19922`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19922`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + GLUTATHIONE -> S-METHYLGLUTATHIONE + ADENOSYL-HOMO-CYS + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + GLUTATHIONE -> S-METHYLGLUTATHIONE + ADENOSYL-HOMO-CYS + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cheR (protein.P07364). Substrates: S-Adenosyl-L-methionine (molecule.C00019), Glutathione (molecule.C00051). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), S-methylglutathione (molecule.ecocyc.S-METHYLGLUTATHIONE).

## Annotation

S-ADENOSYLMETHIONINE + GLUTATHIONE -> S-METHYLGLUTATHIONE + ADENOSYL-HOMO-CYS + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P07364|protein.P07364]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.S-METHYLGLUTATHIONE|molecule.ecocyc.S-METHYLGLUTATHIONE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19922`

## Notes

S-ADENOSYLMETHIONINE + GLUTATHIONE -> S-METHYLGLUTATHIONE + ADENOSYL-HOMO-CYS + PROTON; direction=LEFT-TO-RIGHT
