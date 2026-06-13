---
entity_id: "reaction.ecocyc.UDP-NACMURALGLDAPAALIG-RXN"
entity_type: "reaction"
name: "UDP-N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-2,6-diaminopimelate ligase"
source_database: "EcoCyc"
source_id: "UDP-NACMURALGLDAPAALIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDP-N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-2,6-diaminopimelate ligase

`reaction.ecocyc.UDP-NACMURALGLDAPAALIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDP-NACMURALGLDAPAALIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the sixth and final cytoplasmic step in petidoglycan biosynthesis. EcoCyc reaction equation: D-ALA-D-ALA + UDP-AAGM-DIAMINOHEPTANEDIOATE + ATP -> PROTON + C1 + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the sixth and final cytoplasmic step in petidoglycan biosynthesis.

## Biological Role

Catalyzed by murF (protein.P11880). Substrates: ATP (molecule.C00002), D-Alanyl-D-alanine (molecule.C00993), UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate (molecule.C04877). Products: ADP (molecule.C00008), H+ (molecule.C00080), UDP-N-acetylmuramoyl-L-alanyl-D-glutamyl-6-carboxy-L-lysyl-D-alanyl-D-alanine (molecule.C04882), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Annotation

This is the sixth and final cytoplasmic step in petidoglycan biosynthesis.

## Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P11880|protein.P11880]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04882|molecule.C04882]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00993|molecule.C00993]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04877|molecule.C04877]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.DDP-NAcMur-Peptides|molecule.ecocyc.DDP-NAcMur-Peptides]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.UDP-NAcMur-Peptides|molecule.ecocyc.UDP-NAcMur-Peptides]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:UDP-NACMURALGLDAPAALIG-RXN`

## Notes

D-ALA-D-ALA + UDP-AAGM-DIAMINOHEPTANEDIOATE + ATP -> PROTON + C1 + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
