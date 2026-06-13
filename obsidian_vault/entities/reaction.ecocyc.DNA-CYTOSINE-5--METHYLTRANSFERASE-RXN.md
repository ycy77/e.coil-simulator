---
entity_id: "reaction.ecocyc.DNA-CYTOSINE-5--METHYLTRANSFERASE-RXN"
entity_type: "reaction"
name: "DNA-CYTOSINE-5--METHYLTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "DNA-CYTOSINE-5--METHYLTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DNA-CYTOSINE-5--METHYLTRANSFERASE-RXN

`reaction.ecocyc.DNA-CYTOSINE-5--METHYLTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DNA-CYTOSINE-5--METHYLTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + DNA-Cytosines -> 5-Methylcytosine-DNA + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + DNA-Cytosines -> 5-Methylcytosine-DNA + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dcm (protein.P0AED9). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a cytosine in DNA (molecule.ecocyc.DNA-Cytosines). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 5-methylcytosine in DNA (molecule.ecocyc.5-Methylcytosine-DNA).

## Annotation

S-ADENOSYLMETHIONINE + DNA-Cytosines -> 5-Methylcytosine-DNA + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0AED9|protein.P0AED9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-Methylcytosine-DNA|molecule.ecocyc.5-Methylcytosine-DNA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DNA-Cytosines|molecule.ecocyc.DNA-Cytosines]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.S-TUBERCIDINYLHOMOCYSTEINE|molecule.ecocyc.S-TUBERCIDINYLHOMOCYSTEINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DNA-CYTOSINE-5--METHYLTRANSFERASE-RXN`

## Notes

S-ADENOSYLMETHIONINE + DNA-Cytosines -> 5-Methylcytosine-DNA + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
