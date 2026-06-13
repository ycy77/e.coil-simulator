---
entity_id: "protein.P0AE82"
entity_type: "protein"
name: "cpxA"
source_database: "UniProt"
source_id: "P0AE82"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:25207645, ECO:0000269|PubMed:3058985}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996, ECO:0000305|PubMed:3058985}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cpxA ecfB eup ssd b3911 JW3882"
---

# cpxA

`protein.P0AE82`

## Static

- Type: `protein`
- Source: `UniProt:P0AE82`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:25207645, ECO:0000269|PubMed:3058985}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996, ECO:0000305|PubMed:3058985}.

## Enriched Summary

FUNCTION: Histidine kinase member of the two-component regulatory system CpxA/CpxR which responds to envelope stress response by activating expression of downstream genes including cpxP, degP, dsbA and ppiA (PubMed:7883164, PubMed:9401031, PubMed:9473036). Activates CpxR by phosphorylation; has autokinase, phosphotransferase and (in the presence of Mg(2+) and/or ATP or ADP) phosphatase activity (PubMed:17259177, PubMed:24492262, PubMed:9401031). The kinase activity is inhibited by periplasmic accessory protein CpxP; proteolysis of CpxP relieves inhibition (PubMed:16166523, PubMed:17259177, PubMed:25207645). Involved in several diverse cellular processes, including the functioning of acetohydroxyacid synthetase I, the biosynthesis of isoleucine and valine, the TraJ protein activation activity for tra gene expression in F plasmid (PubMed:8432716), and the synthesis, translocation, or stability of cell envelope proteins (PubMed:7883164). Activates transcription of periplasmic protease degP, probably by phosphorylating the cognate response protein CpxR; overexpression of an outer membrane lipoprotein NlpE also leads to transcription of degP via CpxRA (PubMed:7883164). Required for efficient binding of stationary phase cells to hydrophobic surfaces, part of the process of biofilm formation (PubMed:11830644)...

## Biological Role

Component of sensor histidine kinase CpxA (complex.ecocyc.CPLX0-8270), CpxA-N-phospho-L-histidine (complex.ecocyc.PHOSPHO-CPXA).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Histidine kinase member of the two-component regulatory system CpxA/CpxR which responds to envelope stress response by activating expression of downstream genes including cpxP, degP, dsbA and ppiA (PubMed:7883164, PubMed:9401031, PubMed:9473036). Activates CpxR by phosphorylation; has autokinase, phosphotransferase and (in the presence of Mg(2+) and/or ATP or ADP) phosphatase activity (PubMed:17259177, PubMed:24492262, PubMed:9401031). The kinase activity is inhibited by periplasmic accessory protein CpxP; proteolysis of CpxP relieves inhibition (PubMed:16166523, PubMed:17259177, PubMed:25207645). Involved in several diverse cellular processes, including the functioning of acetohydroxyacid synthetase I, the biosynthesis of isoleucine and valine, the TraJ protein activation activity for tra gene expression in F plasmid (PubMed:8432716), and the synthesis, translocation, or stability of cell envelope proteins (PubMed:7883164). Activates transcription of periplasmic protease degP, probably by phosphorylating the cognate response protein CpxR; overexpression of an outer membrane lipoprotein NlpE also leads to transcription of degP via CpxRA (PubMed:7883164). Required for efficient binding of stationary phase cells to hydrophobic surfaces, part of the process of biofilm formation (PubMed:11830644). {ECO:0000269|PubMed:16166523, ECO:0000269|PubMed:17259177, ECO:0000269|PubMed:24492262, ECO:0000269|PubMed:25207645, ECO:0000269|PubMed:7883164, ECO:0000269|PubMed:8432716, ECO:0000269|PubMed:9401031, ECO:0000269|PubMed:9473036, ECO:0000305|PubMed:11830644}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8270|complex.ecocyc.CPLX0-8270]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PHOSPHO-CPXA|complex.ecocyc.PHOSPHO-CPXA]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3911|gene.b3911]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE82`
- `KEGG:ecj:JW3882;eco:b3911;ecoc:C3026_21150;`
- `GeneID:93778027;948405;`
- `GO:GO:0000155; GO:0004721; GO:0005524; GO:0005886; GO:0007165; GO:0009314; GO:0036460; GO:0042802; GO:0043708`
- `EC:2.7.13.3`

## Notes

Sensor histidine kinase CpxA (EC 2.7.13.3)
