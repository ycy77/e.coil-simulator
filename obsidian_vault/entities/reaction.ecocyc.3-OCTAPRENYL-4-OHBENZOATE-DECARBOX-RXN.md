---
entity_id: "reaction.ecocyc.3-OCTAPRENYL-4-OHBENZOATE-DECARBOX-RXN"
entity_type: "reaction"
name: "3-OCTAPRENYL-4-OHBENZOATE-DECARBOX-RXN"
source_database: "EcoCyc"
source_id: "3-OCTAPRENYL-4-OHBENZOATE-DECARBOX-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-OCTAPRENYL-4-OHBENZOATE-DECARBOX-RXN

`reaction.ecocyc.3-OCTAPRENYL-4-OHBENZOATE-DECARBOX-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3-OCTAPRENYL-4-OHBENZOATE-DECARBOX-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third step in ubiquinone biosynthesis. EcoCyc reaction equation: PROTON + 3-OCTAPRENYL-4-HYDROXYBENZOATE -> 2-OCTAPRENYLPHENOL + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT. This is the third step in ubiquinone biosynthesis.

## Biological Role

Catalyzed by 3-octaprenyl-4-hydroxybenzoate decarboxylase (complex.ecocyc.CPLX0-301). Substrates: H+ (molecule.C00080), 4-hydroxy-3-(all-trans-octaprenyl)benzoate (molecule.ecocyc.3-OCTAPRENYL-4-HYDROXYBENZOATE). Products: CO2 (molecule.C00011), 2-(all-trans-octaprenyl)phenol (molecule.ecocyc.2-OCTAPRENYLPHENOL).

## Enriched Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)
- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Annotation

This is the third step in ubiquinone biosynthesis.

## Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)
- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.C00132|molecule.C00132]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.DITHIOTHREITOL|molecule.ecocyc.DITHIOTHREITOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-301|complex.ecocyc.CPLX0-301]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-OCTAPRENYLPHENOL|molecule.ecocyc.2-OCTAPRENYLPHENOL]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.3-OCTAPRENYL-4-HYDROXYBENZOATE|molecule.ecocyc.3-OCTAPRENYL-4-HYDROXYBENZOATE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3-OCTAPRENYL-4-OHBENZOATE-DECARBOX-RXN`

## Notes

PROTON + 3-OCTAPRENYL-4-HYDROXYBENZOATE -> 2-OCTAPRENYLPHENOL + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
