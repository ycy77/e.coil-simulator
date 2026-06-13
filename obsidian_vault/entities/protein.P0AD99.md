---
entity_id: "protein.P0AD99"
entity_type: "protein"
name: "brnQ"
source_database: "UniProt"
source_id: "P0AD99"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "brnQ b0401 JW0391"
---

# brnQ

`protein.P0AD99`

## Static

- Type: `protein`
- Source: `UniProt:P0AD99`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Liv-II branched chain amino acid transport system, which transports leucine, valine and isoleucine (PubMed:4590465, PubMed:4945181). Also acts as a low-affinity threonine transporter (PubMed:37025642). This activity has probably minor relevance for normal cellular physiology, but BrnQ may form the main entry point when the threonine concentration in the external environment reaches a toxic level (PubMed:37025642). {ECO:0000269|PubMed:37025642, ECO:0000269|PubMed:4590465, ECO:0000269|PubMed:4945181}. BrnQ is a probable branched chain amino acid transporter. BrnQ is highly similar to the Salmonella typhimurium BrnQ branched chain amino acid transporter and very probably corresponds to the LIV-II branched chain amino acid transport system in E. coli, which has been shown to transport leucine, valine, and isoleucine . In the Transporter Classification Database BrnQ is a member of the LIVCS family of branched chain amino acid transporters and probably functions as a branched chain amino acid:Na+ symporter. BrnQ is a low-affinity threonine transporter that is of minor relevance for normal cell physiology .

## Biological Role

Catalyzes L-isoleucine:Na+ symport (reaction.ecocyc.TRANS-RXN-126), L-valine:Na+ symport (reaction.ecocyc.TRANS-RXN-126A), L-leucine:Na+ symport (reaction.ecocyc.TRANS-RXN-126B). Transports L-Leucine (molecule.C00123), L-Valine (molecule.C00183), L-Isoleucine (molecule.C00407), Sodium cation (molecule.C01330).

## Annotation

FUNCTION: Liv-II branched chain amino acid transport system, which transports leucine, valine and isoleucine (PubMed:4590465, PubMed:4945181). Also acts as a low-affinity threonine transporter (PubMed:37025642). This activity has probably minor relevance for normal cellular physiology, but BrnQ may form the main entry point when the threonine concentration in the external environment reaches a toxic level (PubMed:37025642). {ECO:0000269|PubMed:37025642, ECO:0000269|PubMed:4590465, ECO:0000269|PubMed:4945181}.

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-126|reaction.ecocyc.TRANS-RXN-126]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-126A|reaction.ecocyc.TRANS-RXN-126A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-126B|reaction.ecocyc.TRANS-RXN-126B]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00407|molecule.C00407]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0401|gene.b0401]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD99`
- `KEGG:ecj:JW0391;eco:b0401;ecoc:C3026_01950;`
- `GeneID:86862946;93777059;945042;`
- `GO:GO:0005304; GO:0005886; GO:0015188; GO:0015190; GO:0015803; GO:0015818; GO:0015820; GO:0015829`

## Notes

Branched-chain amino acid permease BrnQ (BCAA permease) (Branched-chain amino acid transport system 2 carrier protein) (LIV-II)
