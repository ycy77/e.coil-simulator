---
entity_id: "reaction.ecocyc.RXN-25310"
entity_type: "reaction"
name: "RXN-25310"
source_database: "EcoCyc"
source_id: "RXN-25310"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "BIOTIN SYNTHASE"
---

# RXN-25310

`reaction.ecocyc.RXN-25310`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25310`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The fourth and final step in the biosynthesis of biotin. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Sulfurated-Sulfur-Acceptors + DETHIOBIOTIN + Reduced-flavodoxins -> Unsulfurated-Sulfur-Acceptors + CPD-5662 + CH33ADO + MET + Oxidized-flavodoxins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. The fourth and final step in the biosynthesis of biotin.

## Biological Role

Catalyzed by biotin synthase (complex.ecocyc.BIOTIN-SYN-CPLX). Substrates: S-Adenosyl-L-methionine (molecule.C00019), Dethiobiotin (molecule.C01909). Products: L-Methionine (molecule.C00073), H+ (molecule.C00080), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO), 4,5-secobiotin (molecule.ecocyc.CPD-5662).

## Enriched Pathways

- `ecocyc.PWY0-1507` biotin biosynthesis from 8-amino-7-oxononanoate I (EcoCyc)

## Annotation

The fourth and final step in the biosynthesis of biotin.

## Pathways

- `ecocyc.PWY0-1507` biotin biosynthesis from 8-amino-7-oxononanoate I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.BIOTIN-SYN-CPLX|complex.ecocyc.BIOTIN-SYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-5662|molecule.ecocyc.CPD-5662]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01909|molecule.C01909]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.SINEFUNGIN|molecule.ecocyc.SINEFUNGIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-25310`

## Notes

S-ADENOSYLMETHIONINE + Sulfurated-Sulfur-Acceptors + DETHIOBIOTIN + Reduced-flavodoxins -> Unsulfurated-Sulfur-Acceptors + CPD-5662 + CH33ADO + MET + Oxidized-flavodoxins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
