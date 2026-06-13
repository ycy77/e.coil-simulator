---
entity_id: "protein.P0AEZ3"
entity_type: "protein"
name: "minD"
source_database: "UniProt"
source_id: "P0AEZ3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "minD b1175 JW1164"
---

# minD

`protein.P0AEZ3`

## Static

- Type: `protein`
- Source: `UniProt:P0AEZ3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: ATPase required for the correct placement of the division site. Cell division inhibitors MinC and MinD act in concert to form an inhibitor capable of blocking formation of the polar Z ring septums. Rapidly oscillates between the poles of the cell to destabilize FtsZ filaments that have formed before they mature into polar Z rings. {ECO:0000269|PubMed:1836760, ECO:0000269|PubMed:22380631}. The EG10596-MONOMER "MinC"-MinD-EG10598-MONOMER "MinE" system acts to direct septation to the proper (central) site in the dividing E. coli cell; the Min proteins are involved in a pole-to-pole oscillating system that restricts Z-ring formation to midcell. MinD recruits MinC to the membrane to form the MinC-MinD complex, which inhibits septum formation, and MinE acts to localize and restrict inhibition to the inappropriate septation sites . MinDE is also implicated in a generic mechanism which regulates the positioning of membrane proteins in cells; MinDE form a propagating diffusion barrier which regulates the positioning of functionally unrelated membrane-bound molecules in vitro . MinDE constitutes the minimal set of proteins to drive the formation of FtsA-FtsZ cytoskeletal patterns on supported lipid bilayers...

## Biological Role

Component of Z-ring inhibitor complex MinCD (complex.ecocyc.CPLX0-8188).

## Annotation

FUNCTION: ATPase required for the correct placement of the division site. Cell division inhibitors MinC and MinD act in concert to form an inhibitor capable of blocking formation of the polar Z ring septums. Rapidly oscillates between the poles of the cell to destabilize FtsZ filaments that have formed before they mature into polar Z rings. {ECO:0000269|PubMed:1836760, ECO:0000269|PubMed:22380631}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8188|complex.ecocyc.CPLX0-8188]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1175|gene.b1175]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEZ3`
- `KEGG:ecj:JW1164;eco:b1175;ecoc:C3026_06925;`
- `GeneID:93776259;945741;`
- `GO:GO:0000918; GO:0005524; GO:0005829; GO:0005886; GO:0007059; GO:0008298; GO:0009898; GO:0016887; GO:0042802; GO:0051301; GO:0060187`

## Notes

Septum site-determining protein MinD (Cell division inhibitor MinD)
