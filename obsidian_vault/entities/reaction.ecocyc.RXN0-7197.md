---
entity_id: "reaction.ecocyc.RXN0-7197"
entity_type: "reaction"
name: "RXN0-7197"
source_database: "EcoCyc"
source_id: "RXN0-7197"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7197

`reaction.ecocyc.RXN0-7197`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7197`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Cysteine-Desulfurase-persulfide + Carboxyadenylated-MPT-synthases + YnjE-Proteins -> Cysteine-Desulfurase-L-cysteine + MoeB-YnjE-acyl-disulfide + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-Cysteine-Desulfurase-persulfide + Carboxyadenylated-MPT-synthases + YnjE-Proteins -> Cysteine-Desulfurase-L-cysteine + MoeB-YnjE-acyl-disulfide + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: an [L-cysteine desulfurase]-S-sulfanyl-L-cysteine (molecule.ecocyc.L-Cysteine-Desulfurase-persulfide). Products: AMP (molecule.C00020), H+ (molecule.C00080), an [L-cysteine desulfurase]-L-cysteine (molecule.ecocyc.Cysteine-Desulfurase-L-cysteine).

## Annotation

L-Cysteine-Desulfurase-persulfide + Carboxyadenylated-MPT-synthases + YnjE-Proteins -> Cysteine-Desulfurase-L-cysteine + MoeB-YnjE-acyl-disulfide + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Cysteine-Desulfurase-L-cysteine|molecule.ecocyc.Cysteine-Desulfurase-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.L-Cysteine-Desulfurase-persulfide|molecule.ecocyc.L-Cysteine-Desulfurase-persulfide]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7197`

## Notes

L-Cysteine-Desulfurase-persulfide + Carboxyadenylated-MPT-synthases + YnjE-Proteins -> Cysteine-Desulfurase-L-cysteine + MoeB-YnjE-acyl-disulfide + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
