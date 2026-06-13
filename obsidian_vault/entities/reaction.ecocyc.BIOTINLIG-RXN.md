---
entity_id: "reaction.ecocyc.BIOTINLIG-RXN"
entity_type: "reaction"
name: "BIOTINLIG-RXN"
source_database: "EcoCyc"
source_id: "BIOTINLIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# BIOTINLIG-RXN

`reaction.ecocyc.BIOTINLIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BIOTINLIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The kinetics of the BirA-mediated ligation of biotin (from BirA-biotinyl-5'-AMP) to biotin carboxyl carrier protein monomer have been determined . EcoCyc reaction equation: BCCP-L-lysine + BIOTIN + ATP -> PPI + AMP + BCCP-biotin-L-lysine + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. The kinetics of the BirA-mediated ligation of biotin (from BirA-biotinyl-5'-AMP) to biotin carboxyl carrier protein monomer have been determined .

## Biological Role

Catalyzed by birA (protein.P06709). Substrates: ATP (molecule.C00002), Biotin (molecule.C00120), a [biotin carboxyl-carrier protein]-L-lysine (molecule.ecocyc.BCCP-L-lysine). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), a [biotin carboxyl-carrier protein]-N6-biotinyl-L-lysine (molecule.ecocyc.BCCP-biotin-L-lysine).

## Enriched Pathways

- `ecocyc.PWY0-1264` malonyl-CoA biosynthesis via biotin-carboxyl carrier protein (EcoCyc)

## Annotation

The kinetics of the BirA-mediated ligation of biotin (from BirA-biotinyl-5'-AMP) to biotin carboxyl carrier protein monomer have been determined .

## Pathways

- `ecocyc.PWY0-1264` malonyl-CoA biosynthesis via biotin-carboxyl carrier protein (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P06709|protein.P06709]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.BCCP-biotin-L-lysine|molecule.ecocyc.BCCP-biotin-L-lysine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00120|molecule.C00120]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.BCCP-L-lysine|molecule.ecocyc.BCCP-L-lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:BIOTINLIG-RXN`

## Notes

BCCP-L-lysine + BIOTIN + ATP -> PPI + AMP + BCCP-biotin-L-lysine + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
