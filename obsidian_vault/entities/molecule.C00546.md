---
entity_id: "molecule.C00546"
entity_type: "small_molecule"
name: "Methylglyoxal"
source_database: "KEGG"
source_id: "C00546"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Methylglyoxal"
  - "Pyruvaldehyde"
  - "Pyruvic aldehyde"
  - "2-Ketopropionaldehyde"
  - "2-Oxopropanal"
---

# Methylglyoxal

`molecule.C00546`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00546`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Methylglyoxal; Pyruvaldehyde; Pyruvic aldehyde; 2-Ketopropionaldehyde; 2-Oxopropanal Methylglyoxal is the aldehyde form of PYRUVATE. It is both an aldehyde and a ketone, or a ketal. Methylglyoxal is produced in small amounts during glycolysis, by the enzyme METHGLYSYN-CPLX that converts DIHYDROXY-ACETONE-PHOSPHATE to methylglyoxal. It is also a byproduct of fatty acid metabolism (via ACETONE) and of protein metabolism (via AMINO-ACETONE, which is formed by the degradation of THR). METHYL-GLYOXAL Methylglyoxal is highly toxic, and is detoxified by several pathways (see Methylglyoxal-Detoxification).

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 9 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)

## Annotation

KEGG compound: Methylglyoxal; Pyruvaldehyde; Pyruvic aldehyde; 2-Ketopropionaldehyde; 2-Oxopropanal

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)

## Outgoing Edges (16)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7716|complex.ecocyc.CPLX0-7716]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R01016|reaction.R01016]] `KEGG` `database` - C00111 <=> C00546 + C00009
- `is_product_of` --> [[reaction.R09796|reaction.R09796]] `KEGG` `database` - C00256 <=> C00546 + C00001
- `is_product_of` --> [[reaction.ecocyc.1.1.1.283-RXN|reaction.ecocyc.1.1.1.283-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.AMACETOXID-RXN|reaction.ecocyc.AMACETOXID-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLYOXI-RXN|reaction.ecocyc.GLYOXI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLYOXIII-RXN|reaction.ecocyc.GLYOXIII-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.METHGLYSYN-RXN|reaction.ecocyc.METHGLYSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-24129|reaction.ecocyc.RXN-24129]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-4281|reaction.ecocyc.RXN0-4281]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00203|reaction.R00203]] `KEGG` `database` - C00546 + C00003 + C00001 <=> C00022 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17629|reaction.ecocyc.RXN-17629]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17631|reaction.ecocyc.RXN-17631]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17633|reaction.ecocyc.RXN-17633]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5213|reaction.ecocyc.RXN0-5213]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5423|reaction.ecocyc.RXN0-5423]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00546`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
