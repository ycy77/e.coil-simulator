---
entity_id: "reaction.ecocyc.PHOSNACMURPENTATRANS-RXN"
entity_type: "reaction"
name: "UDP-N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-2,6-diaminopimelyl-D-alanyl-D-alanine:undecaprenyl-phosphate transferase"
source_database: "EcoCyc"
source_id: "PHOSNACMURPENTATRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDP-N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-2,6-diaminopimelyl-D-alanyl-D-alanine:undecaprenyl-phosphate transferase

`reaction.ecocyc.PHOSNACMURPENTATRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOSNACMURPENTATRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the first step in the lipid cycle reactions in the biosynthesis of peptidoglycan, transferring P-MurNacetylpentapeptide from UDP to membrane undecaprenylphosphate . EcoCyc reaction equation: C1 + CPD-9646 -> C5 + UMP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the first step in the lipid cycle reactions in the biosynthesis of peptidoglycan, transferring P-MurNacetylpentapeptide from UDP to membrane undecaprenylphosphate .

## Biological Role

Catalyzed by mraY (protein.P0A6W3). Substrates: UDP-N-acetylmuramoyl-L-alanyl-D-glutamyl-6-carboxy-L-lysyl-D-alanyl-D-alanine (molecule.C04882), di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556). Products: UMP (molecule.C00105), Undecaprenyl-diphospho-N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanyl-D-alanine (molecule.C05897).

## Enriched Pathways

- `ecocyc.PEPTIDOGLYCANSYN-PWY` peptidoglycan biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Annotation

This reaction is the first step in the lipid cycle reactions in the biosynthesis of peptidoglycan, transferring P-MurNacetylpentapeptide from UDP to membrane undecaprenylphosphate .

## Pathways

- `ecocyc.PEPTIDOGLYCANSYN-PWY` peptidoglycan biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A6W3|protein.P0A6W3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05897|molecule.C05897]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04882|molecule.C04882]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C17556|molecule.C17556]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.A-MURAYMYCIN|molecule.ecocyc.A-MURAYMYCIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-15249|molecule.ecocyc.CPD-15249]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-28123|molecule.ecocyc.CPD-28123]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5242|molecule.ecocyc.CPD-5242]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PHOSNACMURPENTATRANS-RXN`

## Notes

C1 + CPD-9646 -> C5 + UMP; direction=PHYSIOL-LEFT-TO-RIGHT
