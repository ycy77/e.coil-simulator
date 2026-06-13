---
entity_id: "reaction.ecocyc.RXN-21299"
entity_type: "reaction"
name: "RXN-21299"
source_database: "EcoCyc"
source_id: "RXN-21299"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21299

`reaction.ecocyc.RXN-21299`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21299`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

General-Protein-Substrates + WATER + ATP -> Peptides-holder + Peptide-Holder-Alternative + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: General-Protein-Substrates + WATER + ATP -> Peptides-holder + Peptide-Holder-Alternative + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by FtsH/HflKC protease complex (complex.ecocyc.CPLX0-2982). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

General-Protein-Substrates + WATER + ATP -> Peptides-holder + Peptide-Holder-Alternative + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2982|complex.ecocyc.CPLX0-2982]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-4584|molecule.ecocyc.CPD-4584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-21299`

## Notes

General-Protein-Substrates + WATER + ATP -> Peptides-holder + Peptide-Holder-Alternative + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
