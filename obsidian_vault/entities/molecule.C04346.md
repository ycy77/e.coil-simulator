---
entity_id: "molecule.C04346"
entity_type: "small_molecule"
name: "dTDP-4-amino-4,6-dideoxy-D-galactose"
source_database: "KEGG"
source_id: "C04346"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dTDP-4-amino-4,6-dideoxy-D-galactose"
  - "dTDP-4-amino-4,6-dideoxy-alpha-D-galactose"
---

# dTDP-4-amino-4,6-dideoxy-D-galactose

`molecule.C04346`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04346`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dTDP-4-amino-4,6-dideoxy-D-galactose; dTDP-4-amino-4,6-dideoxy-alpha-D-galactose EcoCyc common name: dTDP-4-amino-4,6-dideoxy-α-D-galactose.

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: dTDP-4-amino-4,6-dideoxy-D-galactose; dTDP-4-amino-4,6-dideoxy-alpha-D-galactose

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.R04438|reaction.R04438]] `KEGG` `database` - C04346 + C00026 <=> C11907 + C00025
- `is_substrate_of` --> [[reaction.ecocyc.RFFTRANS-RXN|reaction.ecocyc.RFFTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TDPFUCACTRANS-RXN|reaction.ecocyc.TDPFUCACTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04346`
- `EcoCyc:CPD-14020`
- `CHEBI:57596`
- `PUBCHEM:46878407`
- `canonicalized_from:molecule.ecocyc.CPD-14020`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.CPD-14020: EcoCyc:CPD-14020
