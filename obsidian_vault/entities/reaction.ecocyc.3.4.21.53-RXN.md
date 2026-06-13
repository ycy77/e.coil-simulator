---
entity_id: "reaction.ecocyc.3.4.21.53-RXN"
entity_type: "reaction"
name: "3.4.21.53-RXN"
source_database: "EcoCyc"
source_id: "3.4.21.53-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.4.21.53-RXN

`reaction.ecocyc.3.4.21.53-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.21.53-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is that of a serine protease with a chymotrypsin-like specificity. EcoCyc reaction equation: General-Protein-Substrates + WATER + ATP -> Peptides-holder + Peptide-Holder-Alternative + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is that of a serine protease with a chymotrypsin-like specificity.

## Biological Role

Catalyzed by Lon protease (complex.ecocyc.CPLX0-2881). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

This reaction is that of a serine protease with a chymotrypsin-like specificity.

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2881|complex.ecocyc.CPLX0-2881]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C05980|molecule.C05980]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIISOPROPYL-FLUOROPHOSPHATE|molecule.ecocyc.DIISOPROPYL-FLUOROPHOSPHATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.4.21.53-RXN`

## Notes

General-Protein-Substrates + WATER + ATP -> Peptides-holder + Peptide-Holder-Alternative + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
