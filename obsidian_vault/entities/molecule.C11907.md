---
entity_id: "molecule.C11907"
entity_type: "small_molecule"
name: "dTDP-4-oxo-6-deoxy-D-glucose"
source_database: "KEGG"
source_id: "C11907"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dTDP-4-oxo-6-deoxy-D-glucose"
  - "dTDP-4-dehydro-6-deoxy-D-glucose"
  - "dTDP-4-dehydro-6-deoxy-alpha-D-glucose"
  - "dTDP-4-dehydro-6-deoxy-alpha-D-glucopyranose"
  - "dTDP-4-oxo-6-deoxy-alpha-D-glucose"
  - "dTDP-4-dehydro-6-deoxy-alpha-D-galactose"
  - "dTDP-4-dehydro-6-deoxy-D-galactose"
  - "dTDP-6-deoxy-D-xylo-hexos-4-ulose"
  - "dTDP-6-deoxy-D-xylo-4-hexulose"
  - "4,6-Dideoxy-4-oxo-dTDP-D-glucose"
  - "dTDP-4-keto-6-deoxy-D-glucose"
  - "dTDP-4-keto-6-deoxyglucose"
---

# dTDP-4-oxo-6-deoxy-D-glucose

`molecule.C11907`

## Static

- Type: `small_molecule`
- Source: `KEGG:C11907`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dTDP-4-oxo-6-deoxy-D-glucose; dTDP-4-dehydro-6-deoxy-D-glucose; dTDP-4-dehydro-6-deoxy-alpha-D-glucose; dTDP-4-dehydro-6-deoxy-alpha-D-glucopyranose; dTDP-4-oxo-6-deoxy-alpha-D-glucose; dTDP-4-dehydro-6-deoxy-alpha-D-galactose; dTDP-4-dehydro-6-deoxy-D-galactose; dTDP-6-deoxy-D-xylo-hexos-4-ulose; dTDP-6-deoxy-D-xylo-4-hexulose; 4,6-Dideoxy-4-oxo-dTDP-D-glucose; dTDP-4-keto-6-deoxy-D-glucose; dTDP-4-keto-6-deoxyglucose EcoCyc common name: dTDP-4-dehydro-6-deoxy-α-D-glucopyranose.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: dTDP-4-oxo-6-deoxy-D-glucose; dTDP-4-dehydro-6-deoxy-D-glucose; dTDP-4-dehydro-6-deoxy-alpha-D-glucose; dTDP-4-dehydro-6-deoxy-alpha-D-glucopyranose; dTDP-4-oxo-6-deoxy-alpha-D-glucose; dTDP-4-dehydro-6-deoxy-alpha-D-galactose; dTDP-4-dehydro-6-deoxy-D-galactose; dTDP-6-deoxy-D-xylo-hexos-4-ulose; dTDP-6-deoxy-D-xylo-4-hexulose; 4,6-Dideoxy-4-oxo-dTDP-D-glucose; dTDP-4-keto-6-deoxy-D-glucose; dTDP-4-keto-6-deoxyglucose

## Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R04438|reaction.R04438]] `KEGG` `database` - C04346 + C00026 <=> C11907 + C00025
- `is_product_of` --> [[reaction.ecocyc.DTDPGLUCDEHYDRAT-RXN|reaction.ecocyc.DTDPGLUCDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RFFTRANS-RXN|reaction.ecocyc.RFFTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DTDPDEHYDRHAMEPIM-RXN|reaction.ecocyc.DTDPDEHYDRHAMEPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C11907`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
