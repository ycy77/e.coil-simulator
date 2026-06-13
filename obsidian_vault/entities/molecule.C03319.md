---
entity_id: "molecule.C03319"
entity_type: "small_molecule"
name: "dTDP-L-rhamnose"
source_database: "KEGG"
source_id: "C03319"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dTDP-L-rhamnose"
  - "dTDP-6-deoxy-L-mannose"
  - "dTDP-6-deoxy-beta-L-mannose"
  - "dTDP-beta-L-rhamnose"
---

# dTDP-L-rhamnose

`molecule.C03319`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03319`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dTDP-L-rhamnose; dTDP-6-deoxy-L-mannose; dTDP-6-deoxy-beta-L-mannose; dTDP-beta-L-rhamnose EcoCyc common name: dTDP-β-L-rhamnose.

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: dTDP-L-rhamnose; dTDP-6-deoxy-L-mannose; dTDP-6-deoxy-beta-L-mannose; dTDP-beta-L-rhamnose

## Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.ecocyc.DTDPDEHYRHAMREDUCT-RXN|reaction.ecocyc.DTDPDEHYRHAMREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5129|reaction.ecocyc.RXN0-5129]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DTDPGLUCOSEPP-RXN|reaction.ecocyc.DTDPGLUCOSEPP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03319`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
