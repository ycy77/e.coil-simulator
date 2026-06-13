---
entity_id: "protein.P0ABN5"
entity_type: "protein"
name: "dcuA"
source_database: "UniProt"
source_id: "P0ABN5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:9733683}; Multi-pass membrane protein {ECO:0000269|PubMed:9733683}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dcuA genA b4138 JW5735"
---

# dcuA

`protein.P0ABN5`

## Static

- Type: `protein`
- Source: `UniProt:P0ABN5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:9733683}; Multi-pass membrane protein {ECO:0000269|PubMed:9733683}.

## Enriched Summary

FUNCTION: Responsible for the transport of C4-dicarboxylates during aerobic and anaerobic growth (PubMed:29995997, PubMed:7961398, PubMed:8131924, PubMed:8955408). Required for the uptake of L-aspartate as a nitrogen source during aerobic growth (PubMed:29995997). The uptake of L-aspartate in aerobic conditions is coupled to the excretion of fumarate, resulting in the net uptake of nitrogen without carbon uptake (PubMed:29995997). In addition, during anaerobic growth, catalyzes the uptake of fumarate, malate or aspartate coupled to the export of succinate (PubMed:7961398, PubMed:8955408). Can also catalyze the uptake (without exchange) of fumarate (PubMed:8955408). May play a a general role in anaerobic C4-dicarboxylate transport (PubMed:9852003). {ECO:0000269|PubMed:29995997, ECO:0000269|PubMed:7961398, ECO:0000269|PubMed:8131924, ECO:0000269|PubMed:8955408, ECO:0000269|PubMed:9852003}. DcuA is a C4-dicarboxylate transporter which is required for the uptake of L-aspartate as a nitrogen source under aerobic conditions; DcuA mediates an L-aspartate:fumarate antiport reaction which results in the net uptake of nitrogen without carbon uptake; DcuA is the major transporter for L-aspartate uptake under aerobic conditions (see further ). dcuA and dcuB encode predicted inner membrane proteins with high sequence similarity; E...

## Biological Role

Catalyzes fumarate:succinate antiport (reaction.ecocyc.TRANS-RXN-106), aspartate:succinate antiport (reaction.ecocyc.TRANS-RXN-106A), malate:succinate antiport (reaction.ecocyc.TRANS-RXN-106B), fumarate:proton symport (reaction.ecocyc.TRANS-RXN-299), L-aspartate:fumarate antiport (reaction.ecocyc.TRANS-RXN-379). Transports L-Aspartate (molecule.C00049), Fumarate (molecule.C00122).

## Annotation

FUNCTION: Responsible for the transport of C4-dicarboxylates during aerobic and anaerobic growth (PubMed:29995997, PubMed:7961398, PubMed:8131924, PubMed:8955408). Required for the uptake of L-aspartate as a nitrogen source during aerobic growth (PubMed:29995997). The uptake of L-aspartate in aerobic conditions is coupled to the excretion of fumarate, resulting in the net uptake of nitrogen without carbon uptake (PubMed:29995997). In addition, during anaerobic growth, catalyzes the uptake of fumarate, malate or aspartate coupled to the export of succinate (PubMed:7961398, PubMed:8955408). Can also catalyze the uptake (without exchange) of fumarate (PubMed:8955408). May play a a general role in anaerobic C4-dicarboxylate transport (PubMed:9852003). {ECO:0000269|PubMed:29995997, ECO:0000269|PubMed:7961398, ECO:0000269|PubMed:8131924, ECO:0000269|PubMed:8955408, ECO:0000269|PubMed:9852003}.

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-106|reaction.ecocyc.TRANS-RXN-106]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-106A|reaction.ecocyc.TRANS-RXN-106A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-106B|reaction.ecocyc.TRANS-RXN-106B]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-299|reaction.ecocyc.TRANS-RXN-299]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-379|reaction.ecocyc.TRANS-RXN-379]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4138|gene.b4138]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABN5`
- `KEGG:ecj:JW5735;eco:b4138;ecoc:C3026_22365;`
- `GeneID:86861469;93777686;948659;`
- `GO:GO:0005469; GO:0005886; GO:0009061; GO:0015293; GO:0015556; GO:0015740; GO:0140009`

## Notes

C4-dicarboxylate transporter DcuA
