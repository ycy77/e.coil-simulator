---
entity_id: "reaction.ecocyc.RXN-18388"
entity_type: "reaction"
name: "RXN-18388"
source_database: "EcoCyc"
source_id: "RXN-18388"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18388

`reaction.ecocyc.RXN-18388`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18388`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Sulfurylated-ThiI + Uracil-tRNAs + ATP + Reduced-ferredoxins + PROTON -> tRNA-4-thiouridine + Sulfur-Carrier-Proteins-ThiI + AMP + PPI + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Sulfurylated-ThiI + Uracil-tRNAs + ATP + Reduced-ferredoxins + PROTON -> tRNA-4-thiouridine + Sulfur-Carrier-Proteins-ThiI + AMP + PPI + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by thiI (protein.P77718). Substrates: ATP (molecule.C00002), H+ (molecule.C00080), a uracil in tRNA (molecule.ecocyc.Uracil-tRNAs). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), a 4-thiouridine8 in tRNA (molecule.ecocyc.tRNA-4-thiouridine).

## Enriched Pathways

- `ecocyc.PWY-8618` tRNA-uridine 4-thiolation II (EcoCyc)

## Annotation

Sulfurylated-ThiI + Uracil-tRNAs + ATP + Reduced-ferredoxins + PROTON -> tRNA-4-thiouridine + Sulfur-Carrier-Proteins-ThiI + AMP + PPI + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8618` tRNA-uridine 4-thiolation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P77718|protein.P77718]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNA-4-thiouridine|molecule.ecocyc.tRNA-4-thiouridine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Uracil-tRNAs|molecule.ecocyc.Uracil-tRNAs]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1363|molecule.ecocyc.CPD0-1363]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-18388`

## Notes

Sulfurylated-ThiI + Uracil-tRNAs + ATP + Reduced-ferredoxins + PROTON -> tRNA-4-thiouridine + Sulfur-Carrier-Proteins-ThiI + AMP + PPI + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT
