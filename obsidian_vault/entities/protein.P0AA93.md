---
entity_id: "protein.P0AA93"
entity_type: "protein"
name: "ypdA"
source_database: "UniProt"
source_id: "P0AA93"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ypdA b2380 JW5388"
---

# ypdA

`protein.P0AA93`

## Static

- Type: `protein`
- Source: `UniProt:P0AA93`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system YpdA/YpdB, which is part of a nutrient-sensing regulatory network composed of YpdA/YpdB, the high-affinity pyruvate signaling system BtsS/BtsR and their respective target proteins, YhjX and BtsT. YpdA activates YpdB by phosphorylation in response to high concentrations of extracellular pyruvate. Activation of the YpdA/YpdB signaling cascade also promotes BtsS/BtsR-mediated btsT expression. {ECO:0000269|PubMed:23222720, ECO:0000269|PubMed:24659770}. PyrS is the sensory kinase of a two-component signal transduction system which senses extracellular pyruvate and induces expression of the putative pyruvate transporter YHJX-MONOMER "YhjX" . PyrS is predicted to be an inner membrane protein with 6 trans-membrane domains . Phosphorylation of PyrS has not been detected in vitro, however substitution of the conserved histidine residue H371 with glutamine prevents yhjX induction in vivo . yhjX is not induced in a pyrSRypdC deletion mutant; complementation with pyrSRypdC expressed in trans restores induction . yhjX and yhcC promoter activity decreases, and gltB promoter activity increases, when a pyrS deletion mutant is grown in pyruvate minimal media . PyrS interacts with YHJX-MONOMER "YhjX" and with the pyruvate:H+ symporter G7942-MONOMER "BtsT"; PyrS is capable of homo-oligomerisation...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system YpdA/YpdB, which is part of a nutrient-sensing regulatory network composed of YpdA/YpdB, the high-affinity pyruvate signaling system BtsS/BtsR and their respective target proteins, YhjX and BtsT. YpdA activates YpdB by phosphorylation in response to high concentrations of extracellular pyruvate. Activation of the YpdA/YpdB signaling cascade also promotes BtsS/BtsR-mediated btsT expression. {ECO:0000269|PubMed:23222720, ECO:0000269|PubMed:24659770}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2380|gene.b2380]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA93`
- `KEGG:ecj:JW5388;eco:b2380;ecoc:C3026_13235;`
- `GeneID:75172499;75202551;946723;`
- `GO:GO:0000155; GO:0004673; GO:0005524; GO:0005886; GO:0007165; GO:0031670; GO:0071555`
- `EC:2.7.13.3`

## Notes

Sensor histidine kinase YpdA (EC 2.7.13.3)
