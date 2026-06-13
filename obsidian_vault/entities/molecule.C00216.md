---
entity_id: "molecule.C00216"
entity_type: "small_molecule"
name: "D-Arabinose"
source_database: "KEGG"
source_id: "C00216"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Arabinose"
  - "D-Arabinopyranose"
---

# D-Arabinose

`molecule.C00216`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00216`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Arabinose; D-Arabinopyranose This compound stands for a mixture of CPD-12047 and CPD-12049. In most cases, each of these compounds mutarotates quickly to form a mixture of the two, and thus it is the general rule to use this non-specific form in reactions unless it is specifically known that an enzyme can accept only one of the forms. Arabinoses Arabinose is an aldopentose - a monosaccharide containing five carbon atoms. Unlike many other aldoses, which are more abundant in nature as the "D"-form, L-ARABINOSE is far more common in nature than D-ARABINOSE. Due to its scarcity, most microorganisms are not able to metabolize D-ARABINOSE. This compound class for D-arabinose represents a reducing sugar that exists in solution in multiple configurations. The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration. At equlibrium D-arabinose is present in aqueous solution almost entirely in the pyranose form, with the following distribution: CPD-12047 - 61%, CPD-12049 - 35.5%, CPD-12044 - 2.5%, CPD-12043 - 2%. The concentration of CPD-15700 is only 0.03% .

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Annotation

KEGG compound: D-Arabinose; D-Arabinopyranose

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.RXN-14807|reaction.ecocyc.RXN-14807]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7219|reaction.ecocyc.RXN0-7219]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7221|reaction.ecocyc.RXN0-7221]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DARABISOM-RXN|reaction.ecocyc.DARABISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14806|reaction.ecocyc.RXN-14806]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7221|reaction.ecocyc.RXN0-7221]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN0-6373|reaction.ecocyc.RXN0-6373]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P11551|protein.P11551]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00216`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
