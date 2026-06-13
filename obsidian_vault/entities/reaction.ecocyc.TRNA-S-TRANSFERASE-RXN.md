---
entity_id: "reaction.ecocyc.TRNA-S-TRANSFERASE-RXN"
entity_type: "reaction"
name: "TRNA-S-TRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "TRNA-S-TRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRNA-S-TRANSFERASE-RXN

`reaction.ecocyc.TRNA-S-TRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRNA-S-TRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Cysteine-Desulfurase-persulfide + Cytosine-32-In-tRNAs + ATP + Reduced-ferredoxins + PROTON -> Cysteine-Desulfurase-L-cysteine + 2-Thiocytosine-32-In-tRNAs + AMP + PPI + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-Cysteine-Desulfurase-persulfide + Cytosine-32-In-tRNAs + ATP + Reduced-ferredoxins + PROTON -> Cysteine-Desulfurase-L-cysteine + 2-Thiocytosine-32-In-tRNAs + AMP + PPI + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tRNA cytosine32 2-sulfurtransferase TtcA (complex.ecocyc.CPLX0-8124). Substrates: ATP (molecule.C00002), H+ (molecule.C00080), a cytosine32 in tRNA (molecule.ecocyc.Cytosine-32-In-tRNAs), an [L-cysteine desulfurase]-S-sulfanyl-L-cysteine (molecule.ecocyc.L-Cysteine-Desulfurase-persulfide). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), a 2-thiocytosine32 in tRNA (molecule.ecocyc.2-Thiocytosine-32-In-tRNAs), an [L-cysteine desulfurase]-L-cysteine (molecule.ecocyc.Cysteine-Desulfurase-L-cysteine).

## Annotation

L-Cysteine-Desulfurase-persulfide + Cytosine-32-In-tRNAs + ATP + Reduced-ferredoxins + PROTON -> Cysteine-Desulfurase-L-cysteine + 2-Thiocytosine-32-In-tRNAs + AMP + PPI + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `activates` <-- [[complex.ecocyc.CPLX0-248|complex.ecocyc.CPLX0-248]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.DITHIOTHREITOL|molecule.ecocyc.DITHIOTHREITOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8124|complex.ecocyc.CPLX0-8124]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-Thiocytosine-32-In-tRNAs|molecule.ecocyc.2-Thiocytosine-32-In-tRNAs]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Cysteine-Desulfurase-L-cysteine|molecule.ecocyc.Cysteine-Desulfurase-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Cytosine-32-In-tRNAs|molecule.ecocyc.Cytosine-32-In-tRNAs]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.L-Cysteine-Desulfurase-persulfide|molecule.ecocyc.L-Cysteine-Desulfurase-persulfide]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRNA-S-TRANSFERASE-RXN`

## Notes

L-Cysteine-Desulfurase-persulfide + Cytosine-32-In-tRNAs + ATP + Reduced-ferredoxins + PROTON -> Cysteine-Desulfurase-L-cysteine + 2-Thiocytosine-32-In-tRNAs + AMP + PPI + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT
