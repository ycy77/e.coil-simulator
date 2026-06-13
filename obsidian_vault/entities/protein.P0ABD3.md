---
entity_id: "protein.P0ABD3"
entity_type: "protein"
name: "bfr"
source_database: "UniProt"
source_id: "P0ABD3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bfr b3336 JW3298"
---

# bfr

`protein.P0ABD3`

## Static

- Type: `protein`
- Source: `UniProt:P0ABD3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Iron-storage protein, whose ferroxidase center binds Fe(2+), oxidizes it using dioxygen to Fe(3+), and participates in the subsequent Fe(3+) oxide mineral core formation within the central cavity of the BFR protein shell. The mineralized iron core can contain as many as 2700 iron atoms/24-meric molecule. {ECO:0000269|PubMed:10769150, ECO:0000269|PubMed:14636073}. bfr encodes the iron storage hemoprotein bacterioferritin . Bacterioferritin and CPLX0-3969 ferritin are distantly related . Under normal growth conditions, bacterioferritin contains approximately 15% of the cell's iron, with 70% of iron found in SUPEROX-DISMUTFE-MONOMER SodB; when cells are grown at high extracellular iron concentration, ferritin stores the bulk of the iron . Notably, a bfr mutant does not exhibit a defect in iron storage . Bacterioferritin exists as a 24-subunit homomultimer that forms a hollow sphere of 95 Å or 119 to 128 Å in diameter. Structural and physical characteristics of Bfr and Bfr complexes have been examined in detail . A homodimeric form of Bfr is favored under low pH conditions . Minimizing salt concentration combined with adjusting the pH to 8.5 or lower reversibly shifts the equilibrium between dimeric and 24-meric assemblies, a property that has been used for biotechnological application of protein encapsulation within the ferritin cavity...

## Biological Role

Catalyzes Fe(II):oxygen oxidoreductase; (reaction.R00078). Component of bacterioferritin (complex.ecocyc.CPLX0-1421).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

FUNCTION: Iron-storage protein, whose ferroxidase center binds Fe(2+), oxidizes it using dioxygen to Fe(3+), and participates in the subsequent Fe(3+) oxide mineral core formation within the central cavity of the BFR protein shell. The mineralized iron core can contain as many as 2700 iron atoms/24-meric molecule. {ECO:0000269|PubMed:10769150, ECO:0000269|PubMed:14636073}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00078|reaction.R00078]] `KEGG` `database` - via EC:1.16.3.1
- `is_component_of` --> [[complex.ecocyc.CPLX0-1421|complex.ecocyc.CPLX0-1421]] `EcoCyc` `database` - EcoCyc component coefficient=24 | EcoCyc protcplxs.col coefficient=24

## Incoming Edges (1)

- `encodes` <-- [[gene.b3336|gene.b3336]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABD3`
- `KEGG:ecj:JW3298;eco:b3336;ecoc:C3026_18120;`
- `GeneID:86862266;947839;`
- `GO:GO:0004322; GO:0005506; GO:0005829; GO:0006826; GO:0006879; GO:0008199; GO:0016020; GO:0016491; GO:0020037; GO:0042802; GO:0042803; GO:0140315`
- `EC:1.16.3.1`

## Notes

Bacterioferritin (BFR) (EC 1.16.3.1) (Cytochrome b-1) (Cytochrome b-557)
