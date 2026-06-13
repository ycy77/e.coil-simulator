---
entity_id: "reaction.ecocyc.NACGLCTRANS-RXN"
entity_type: "reaction"
name: "UDP-N-acetyl-D-glucosamine:N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-2,6-diaminopimelyl-D-alanyl-D-alanine-diphosphoundecaprenol 4-β-N-acetylglucosaminlytransferase"
source_database: "EcoCyc"
source_id: "NACGLCTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDP-N-acetyl-D-glucosamine:N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-2,6-diaminopimelyl-D-alanyl-D-alanine-diphosphoundecaprenol 4-β-N-acetylglucosaminlytransferase

`reaction.ecocyc.NACGLCTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NACGLCTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the final step of peptidoglycan subunit assembly. EcoCyc reaction equation: C5 + UDP-N-ACETYL-D-GLUCOSAMINE -> PROTON + C6 + UDP; direction=REVERSIBLE. This is the final step of peptidoglycan subunit assembly.

## Biological Role

Catalyzed by murG (protein.P17443). Substrates: UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043), Undecaprenyl-diphospho-N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanyl-D-alanine (molecule.C05897). Products: UDP (molecule.C00015), H+ (molecule.C00080), Undecaprenyl-diphospho-N-acetylmuramoyl-(N-acetylglucosamine)-L-alanyl-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanyl-D-alanine (molecule.C05898).

## Enriched Pathways

- `ecocyc.PEPTIDOGLYCANSYN-PWY` peptidoglycan biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Annotation

This is the final step of peptidoglycan subunit assembly.

## Pathways

- `ecocyc.PEPTIDOGLYCANSYN-PWY` peptidoglycan biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P17443|protein.P17443]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05898|molecule.C05898]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00043|molecule.C00043]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05897|molecule.C05897]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NACGLCTRANS-RXN`

## Notes

C5 + UDP-N-ACETYL-D-GLUCOSAMINE -> PROTON + C6 + UDP; direction=REVERSIBLE
