---
entity_id: "protein.P06149"
entity_type: "protein"
name: "dld"
source_database: "UniProt"
source_id: "P06149"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02092, ECO:0000269|PubMed:1092688, ECO:0000269|PubMed:4575624, ECO:0000269|PubMed:4582730}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_02092, ECO:0000269|PubMed:1092688}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_02092, ECO:0000269|PubMed:1092688}. Note=May bind the membrane through electrostatic rather than hydrophobic forces. {ECO:0000305|PubMed:10944213}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dld b2133 JW2121"
---

# dld

`protein.P06149`

## Static

- Type: `protein`
- Source: `UniProt:P06149`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02092, ECO:0000269|PubMed:1092688, ECO:0000269|PubMed:4575624, ECO:0000269|PubMed:4582730}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_02092, ECO:0000269|PubMed:1092688}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_02092, ECO:0000269|PubMed:1092688}. Note=May bind the membrane through electrostatic rather than hydrophobic forces. {ECO:0000305|PubMed:10944213}.

## Enriched Summary

FUNCTION: Catalyzes the oxidation of D-lactate to pyruvate. Electrons derived from D-lactate oxidation are transferred to the ubiquinone/cytochrome electron transfer chain, where they may be used to provide energy for the active transport of a variety of amino acids and sugars across the membrane. {ECO:0000269|PubMed:2185834, ECO:0000269|PubMed:3013300, ECO:0000269|PubMed:4575624, ECO:0000269|PubMed:4582730, ECO:0000269|PubMed:7578233}. D-lactate dehydrogenase (Dld) is a FAD-dependent peripheral membrane dehydrogenase catalysing the oxidation of D-lactate to pyruvate. Dld is a respiratory enzyme; electrons derived from D-lactate oxidation are transferred to the membrane soluble quinone pool . D-lactate dehydrogenase functions as a primary dehydrogenase in aerobic and anaerobic respiratory chains in vitro. Electron transfer from D-lactate to oxygen under aerobic conditions and electron transfer from D-lactate to nitrate under anaerobic conditions depends on the presence of a quinone . Anaerobic β-galactoside transport in whole cells and membrane vesicles can be coupled to the oxidation of D-lactate with fumarate as a terminal acceptor . Proteoliposomes reconstituted with purified cytochrome bo oxidase, ubiquinone-8 and D-lactate dehydrogenase generate an H+ electrochemical gradient (negative inside) in the presence of D-lactate...

## Biological Role

Catalyzes DLACTDEHYDROGFAD-RXN (reaction.ecocyc.DLACTDEHYDROGFAD-RXN). Bound by FAD (molecule.C00016).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidation of D-lactate to pyruvate. Electrons derived from D-lactate oxidation are transferred to the ubiquinone/cytochrome electron transfer chain, where they may be used to provide energy for the active transport of a variety of amino acids and sugars across the membrane. {ECO:0000269|PubMed:2185834, ECO:0000269|PubMed:3013300, ECO:0000269|PubMed:4575624, ECO:0000269|PubMed:4582730, ECO:0000269|PubMed:7578233}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DLACTDEHYDROGFAD-RXN|reaction.ecocyc.DLACTDEHYDROGFAD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2133|gene.b2133]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06149`
- `KEGG:ecj:JW2121;eco:b2133;ecoc:C3026_11960;`
- `GeneID:946653;`
- `GO:GO:0004458; GO:0005886; GO:0006089; GO:0009055; GO:0009060; GO:0009061; GO:0009898; GO:0016901; GO:0022904; GO:0031234; GO:0048038; GO:0050660; GO:0055085; GO:0071949; GO:0102029`
- `EC:1.1.5.12`

## Notes

Quinone-dependent D-lactate dehydrogenase (EC 1.1.5.12) ((R)-lactate:quinone 2-oxidoreductase) (D-lactate dehydrogenase) (D-LDH) (Respiratory D-lactate dehydrogenase)
