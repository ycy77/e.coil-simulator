---
entity_id: "molecule.C00160"
entity_type: "small_molecule"
name: "Glycolate"
source_database: "KEGG"
source_id: "C00160"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Glycolate"
  - "Glycolic acid"
  - "Hydroxyacetic acid"
---

# Glycolate

`molecule.C00160`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00160`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Glycolate; Glycolic acid; Hydroxyacetic acid

## Biological Role

Consumed as substrate in 9 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00361` Chlorocyclohexane and chlorobenzene degradation (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Annotation

KEGG compound: Glycolate; Glycolic acid; Hydroxyacetic acid

## Pathways

- `eco00361` Chlorocyclohexane and chlorobenzene degradation (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Outgoing Edges (19)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-562|complex.ecocyc.MONOMER0-562]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.GLYCOLALD-DEHYDROG-RXN|reaction.ecocyc.GLYCOLALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GPH-RXN|reaction.ecocyc.GPH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14642|reaction.ecocyc.RXN-14642]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17757|reaction.ecocyc.RXN-17757]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5111|reaction.ecocyc.RXN0-5111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7173|reaction.ecocyc.RXN0-7173]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-105|reaction.ecocyc.TRANS-RXN-105]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00465|reaction.R00465]] `KEGG` `database` - C00160 + C00006 <=> C00048 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00476|reaction.R00476]] `KEGG` `database` - C00160 + C00028 <=> C00048 + C00030
- `is_substrate_of` --> [[reaction.ecocyc.GLYCOLATE-REDUCTASE-RXN|reaction.ecocyc.GLYCOLATE-REDUCTASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLYCOLATEDEHYDRO-RXN|reaction.ecocyc.GLYCOLATEDEHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN|reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5111|reaction.ecocyc.RXN0-5111]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7229|reaction.ecocyc.RXN0-7229]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-921|reaction.ecocyc.RXN0-921]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-105|reaction.ecocyc.TRANS-RXN-105]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MALSYN-RXN|reaction.ecocyc.MALSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.CPLX0-7955|complex.ecocyc.CPLX0-7955]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P33231|protein.P33231]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00160`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
