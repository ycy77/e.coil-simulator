---
entity_id: "reaction.ecocyc.2.1.1.72-RXN"
entity_type: "reaction"
name: "2.1.1.72-RXN"
source_database: "EcoCyc"
source_id: "2.1.1.72-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "RESTRICTION-MODIFICATION SYSTEM"
  - "MODIFICATION METHYLASE"
  - "N-6 ADENINE-SPECIFIC DNA METHYLASE"
---

# 2.1.1.72-RXN

`reaction.ecocyc.2.1.1.72-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.1.1.72-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SEE THE REBASE DATABASE (FROM RICH ROBERTS) FOR A COMPLETE LIST OF THESE ENZYMES. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + DNA-Adenines -> ADENOSYL-HOMO-CYS + DNA-Containing-N6-Methyladenine + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. SEE THE REBASE DATABASE (FROM RICH ROBERTS) FOR A COMPLETE LIST OF THESE ENZYMES.

## Biological Role

Catalyzed by dam (protein.P0AEE8), yhdJ (protein.P28638). Substrates: S-Adenosyl-L-methionine (molecule.C00019), an adenine in DNA (molecule.ecocyc.DNA-Adenines). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N6-methyladenine in DNA (molecule.ecocyc.DNA-Containing-N6-Methyladenine).

## Annotation

SEE THE REBASE DATABASE (FROM RICH ROBERTS) FOR A COMPLETE LIST OF THESE ENZYMES.

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0AEE8|protein.P0AEE8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P28638|protein.P28638]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DNA-Containing-N6-Methyladenine|molecule.ecocyc.DNA-Containing-N6-Methyladenine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DNA-Adenines|molecule.ecocyc.DNA-Adenines]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.SINEFUNGIN|molecule.ecocyc.SINEFUNGIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2.1.1.72-RXN`

## Notes

S-ADENOSYLMETHIONINE + DNA-Adenines -> ADENOSYL-HOMO-CYS + DNA-Containing-N6-Methyladenine + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
