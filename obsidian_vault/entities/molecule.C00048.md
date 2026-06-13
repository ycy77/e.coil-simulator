---
entity_id: "molecule.C00048"
entity_type: "small_molecule"
name: "Glyoxylate"
source_database: "KEGG"
source_id: "C00048"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Glyoxylate"
  - "Glyoxalate"
  - "Glyoxylic acid"
---

# Glyoxylate

`molecule.C00048`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00048`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Glyoxylate; Glyoxalate; Glyoxylic acid

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 16 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)

## Annotation

KEGG compound: Glyoxylate; Glyoxalate; Glyoxylic acid

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)

## Outgoing Edges (33)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7606|complex.ecocyc.CPLX0-7606]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.MONOMER0-2201|complex.ecocyc.MONOMER0-2201]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00465|reaction.R00465]] `KEGG` `database` - C00160 + C00006 <=> C00048 + C00005 + C00080
- `is_product_of` --> [[reaction.R00470|reaction.R00470]] `KEGG` `database` - C01127 <=> C00022 + C00048
- `is_product_of` --> [[reaction.R00472|reaction.R00472]] `KEGG` `database` - C00149 + C00010 <=> C00024 + C00001 + C00048
- `is_product_of` --> [[reaction.R00476|reaction.R00476]] `KEGG` `database` - C00160 + C00028 <=> C00048 + C00030
- `is_product_of` --> [[reaction.R00479|reaction.R00479]] `KEGG` `database` - C00311 <=> C00042 + C00048
- `is_product_of` --> [[reaction.R00776|reaction.R00776]] `KEGG` `database` - C00603 <=> C00048 + C00086
- `is_product_of` --> [[reaction.ecocyc.GLYCOLATE-REDUCTASE-RXN|reaction.ecocyc.GLYCOLATE-REDUCTASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLYCOLATEDEHYDRO-RXN|reaction.ecocyc.GLYCOLATEDEHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN|reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-13329|reaction.ecocyc.RXN-13329]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-13990|reaction.ecocyc.RXN-13990]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1982|reaction.ecocyc.RXN0-1982]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7081|reaction.ecocyc.RXN0-7081]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7229|reaction.ecocyc.RXN0-7229]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.UREIDOGLYCOLATE-LYASE-RXN|reaction.ecocyc.UREIDOGLYCOLATE-LYASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00013|reaction.R00013]] `KEGG` `database` - 2 C00048 <=> C01146 + C00011
- `is_substrate_of` --> [[reaction.ecocyc.GLYOCARBOLIG-RXN|reaction.ecocyc.GLYOCARBOLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HYDGLUTSYN-RXN|reaction.ecocyc.HYDGLUTSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MALSYN-RXN|reaction.ecocyc.MALSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17757|reaction.ecocyc.RXN-17757]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1982|reaction.ecocyc.RXN0-1982]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4462|reaction.ecocyc.RXN0-4462]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5239|reaction.ecocyc.RXN0-5239]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ACETOLACTSYN-RXN|reaction.ecocyc.ACETOLACTSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ISOCITDEH-RXN|reaction.ecocyc.ISOCITDEH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSICITDEHASE-RXN|reaction.ecocyc.PHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PYRUVDEH-RXN|reaction.ecocyc.PYRUVDEH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-11319|reaction.ecocyc.RXN-11319]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-13990|reaction.ecocyc.RXN-13990]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THREDEHYD-RXN|reaction.ecocyc.THREDEHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00048`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
