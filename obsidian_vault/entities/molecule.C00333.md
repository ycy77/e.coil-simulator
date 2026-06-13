---
entity_id: "molecule.C00333"
entity_type: "small_molecule"
name: "D-Galacturonate"
source_database: "KEGG"
source_id: "C00333"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Galacturonate"
  - "D-Galacturonic acid"
  - "β-D-galacturonic acid"
  - "β-D-galacturonate"
---

# D-Galacturonate

`molecule.C00333`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00333`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Galacturonate; D-Galacturonic acid D-GALACTURONATE is a reducing acidic sugar that exists in solution in multiple configurations. It can form a ring structure, as shown for CPD-12523 and CPD-12524 . The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: D-Galacturonate; D-Galacturonic acid

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (3)

- `activates` --> [[reaction.ecocyc.MANNONDEHYDRAT-RXN|reaction.ecocyc.MANNONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-123|reaction.ecocyc.TRANS-RXN-123]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-123|reaction.ecocyc.TRANS-RXN-123]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0AA78|protein.P0AA78]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00333`
- `EcoCyc:CPD-12524`
- `HMDB:HMDB0002545`
- `ZINC:ZINC000004097542`
- `SEED:cpd05262`
- `METANETX:MNXM114564`
- `LIGAND-CPD:C08348`
- `CHEBI:85312`
- `CHEMSPIDER:5360184`
- `PUBCHEM:6992022`
- `canonicalized_from:molecule.ecocyc.CPD-12524`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.CPD-12524: EcoCyc:CPD-12524
