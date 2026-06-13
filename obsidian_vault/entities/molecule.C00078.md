---
entity_id: "molecule.C00078"
entity_type: "small_molecule"
name: "L-Tryptophan"
source_database: "KEGG"
source_id: "C00078"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Tryptophan"
  - "Tryptophan"
  - "(S)-alpha-Amino-beta-(3-indolyl)-propionic acid"
---

# L-Tryptophan

`molecule.C00078`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00078`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Tryptophan; Tryptophan; (S)-alpha-Amino-beta-(3-indolyl)-propionic acid

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Annotation

KEGG compound: L-Tryptophan; Tryptophan; (S)-alpha-Amino-beta-(3-indolyl)-propionic acid

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Outgoing Edges (17)

- `is_component_of` --> [[complex.ecocyc.CPLX-125|complex.ecocyc.CPLX-125]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00674|reaction.R00674]] `KEGG` `database` - C00065 + C00463 <=> C00078 + C00001
- `is_product_of` --> [[reaction.ecocyc.RXN0-2382|reaction.ecocyc.RXN0-2382]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-301|reaction.ecocyc.RXN0-301]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-76|reaction.ecocyc.TRANS-RXN-76]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRYPSYN-RXN|reaction.ecocyc.TRYPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00673|reaction.R00673]] `KEGG` `database` - C00078 + C00001 <=> C00463 + C00022 + C00014
- `is_substrate_of` --> [[reaction.R03664|reaction.R03664]] `KEGG` `database` - C00002 + C00078 + C01652 <=> C00020 + C00013 + C03512
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15578|reaction.ecocyc.RXN-15578]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19475|reaction.ecocyc.RXN-19475]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-287|reaction.ecocyc.RXN0-287]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-76|reaction.ecocyc.TRANS-RXN-76]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRYPTOPHAN--TRNA-LIGASE-RXN|reaction.ecocyc.TRYPTOPHAN--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRYPTOPHAN-RXN|reaction.ecocyc.TRYPTOPHAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ANTHRANSYN-RXN|reaction.ecocyc.ANTHRANSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DAHPSYN-RXN|reaction.ecocyc.DAHPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTAMINESYN-RXN|reaction.ecocyc.GLUTAMINESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P15993|protein.P15993]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00078`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
