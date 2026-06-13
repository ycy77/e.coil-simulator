---
entity_id: "molecule.C00191"
entity_type: "small_molecule"
name: "D-Glucuronate"
source_database: "KEGG"
source_id: "C00191"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Glucuronate"
  - "Glucuronic acid"
  - "Glucuronate"
---

# D-Glucuronate

`molecule.C00191`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00191`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Glucuronate; Glucuronic acid; Glucuronate GLUCURONATE is a reducing acidic sugar that often forms a hexapyranose ring structure. It is common in carbohydrate chains of proteoglycans and is part of mucous animal secretions (such as saliva), cell glycocalyx and intercellular matrix. The hexapyranosic form CPD-12521 is found in the glycosaminoglycans Chondroitin-sulfates, Dermatan-Sulfate, HEPARIN, Heparan-Sulfate and Hyaluronan. The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)

## Annotation

KEGG compound: D-Glucuronate; Glucuronic acid; Glucuronate

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)

## Outgoing Edges (3)

- `activates` --> [[reaction.ecocyc.MANNONDEHYDRAT-RXN|reaction.ecocyc.MANNONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-35|reaction.ecocyc.TRANS-RXN-35]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-35|reaction.ecocyc.TRANS-RXN-35]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0AA78|protein.P0AA78]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00191`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
