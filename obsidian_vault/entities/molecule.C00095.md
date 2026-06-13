---
entity_id: "molecule.C00095"
entity_type: "small_molecule"
name: "D-Fructose"
source_database: "KEGG"
source_id: "C00095"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Fructose"
  - "Levulose"
  - "Fruit sugar"
  - "D-arabino-Hexulose"
---

# D-Fructose

`molecule.C00095`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00095`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Fructose; Levulose; Fruit sugar; D-arabino-Hexulose Fructose is a 6-carbon polyhydroxyketone. When dissolved in solution fructose forms one of two ring structures - the 5-member ring Fructofuranoseand the 6-member ring D-Fructopyranose. Mixtures at equilibrium contain 70% fructopyranose and 30% fructofuranose (see ). A homopolymeric form of fructose is called Fructans, and can be formed by β(2->1) or β(2->6) glycosidic bonds between fructose molecules. This compound class represents a reducing sugar that exists in solution in multiple configurations. The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: D-Fructose; Levulose; Fruit sugar; D-arabino-Hexulose

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R00801|reaction.R00801]] `KEGG` `database` - C00089 + C00001 <=> C00095 + C00031
- `is_substrate_of` --> [[reaction.R00760|reaction.R00760]] `KEGG` `database` - C00002 + C00095 <=> C00008 + C00085
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-1567|reaction.ecocyc.TRANS-RXN-1567]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-158A|reaction.ecocyc.TRANS-RXN-158A]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.CPLX-158|complex.ecocyc.CPLX-158]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.CPLX-165|complex.ecocyc.CPLX-165]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00095`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
