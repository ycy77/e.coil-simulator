---
entity_id: "reaction.ecocyc.4OHBENZOATE-OCTAPRENYLTRANSFER-RXN"
entity_type: "reaction"
name: "4OHBENZOATE-OCTAPRENYLTRANSFER-RXN"
source_database: "EcoCyc"
source_id: "4OHBENZOATE-OCTAPRENYLTRANSFER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 4OHBENZOATE-OCTAPRENYLTRANSFER-RXN

`reaction.ecocyc.4OHBENZOATE-OCTAPRENYLTRANSFER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:4OHBENZOATE-OCTAPRENYLTRANSFER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in ubiquinone biosynthesis. EcoCyc reaction equation: OCTAPRENYL-DIPHOSPHATE + 4-hydroxybenzoate -> PPI + 3-OCTAPRENYL-4-HYDROXYBENZOATE; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second step in ubiquinone biosynthesis.

## Biological Role

Catalyzed by ubiA (protein.P0AGK1). Substrates: 4-Hydroxybenzoate (molecule.C00156), all-trans-Octaprenyl diphosphate (molecule.C04146). Products: Diphosphate (molecule.C00013), 4-hydroxy-3-(all-trans-octaprenyl)benzoate (molecule.ecocyc.3-OCTAPRENYL-4-HYDROXYBENZOATE).

## Enriched Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)
- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Annotation

This is the second step in ubiquinone biosynthesis.

## Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)
- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.ecocyc.CPD0-1088|molecule.ecocyc.CPD0-1088]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P0AGK1|protein.P0AGK1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.3-OCTAPRENYL-4-HYDROXYBENZOATE|molecule.ecocyc.3-OCTAPRENYL-4-HYDROXYBENZOATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00156|molecule.C00156]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04146|molecule.C04146]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C04483|molecule.C04483]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-3563|molecule.ecocyc.CPD-3563]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7988|molecule.ecocyc.CPD-7988]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:4OHBENZOATE-OCTAPRENYLTRANSFER-RXN`

## Notes

OCTAPRENYL-DIPHOSPHATE + 4-hydroxybenzoate -> PPI + 3-OCTAPRENYL-4-HYDROXYBENZOATE; direction=PHYSIOL-LEFT-TO-RIGHT
