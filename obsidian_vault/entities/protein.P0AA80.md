---
entity_id: "protein.P0AA80"
entity_type: "protein"
name: "garP"
source_database: "UniProt"
source_id: "P0AA80"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "garP yhaU b3127 JW3096"
---

# garP

`protein.P0AA80`

## Static

- Type: `protein`
- Source: `UniProt:P0AA80`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Probably involved in the uptake of galactarate and/or D-glucarate (Probable). May also transport D-glycerate (Probable). {ECO:0000305|PubMed:10762278, ECO:0000305|PubMed:9772162}. GarP is a putative substrate:proton symporter which is implicated in uptake of the diacid sugars, galactarate and D-glucarate. garP is located in a polycistronic operon along with genes whose products are involved in galactarate and D-glucarate metabolism; garP encodes a potential D-glucarate or galactarate transporter . A Φ(garP-lacZ) transcriptional fusion is induced in cultures grown in the presence of galactarate, D-glucarate or D-glycerate; a polar garP::Tn5 insertion mutant has 'impaired' D-glucarate and D-glycerate utilization . In the Transporter Classification Database GarP is a member of the Anion:Cation Symporter (ACS) Family within the Major Facilitator Superfamily (MFS) . GarP may function as a proton-driven glucarate symporter and perhaps a glucarate:glycerate antiporter; it may form part of a membrane transport metabolon linking the transport of glucarate with the enzymes responsible for its metabolism...

## Biological Role

Catalyzes galactarate:proton symport (reaction.ecocyc.TRANS-RXN0-203), D-glucarate:proton symport (reaction.ecocyc.TRANS-RXN0-204), D-glycerate:proton symport (reaction.ecocyc.TRANS-RXN0-523).

## Annotation

FUNCTION: Probably involved in the uptake of galactarate and/or D-glucarate (Probable). May also transport D-glycerate (Probable). {ECO:0000305|PubMed:10762278, ECO:0000305|PubMed:9772162}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-203|reaction.ecocyc.TRANS-RXN0-203]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-204|reaction.ecocyc.TRANS-RXN0-204]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-523|reaction.ecocyc.TRANS-RXN0-523]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3127|gene.b3127]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA80`
- `KEGG:ecj:JW3096;eco:b3127;ecoc:C3026_17045;`
- `GeneID:75203757;947642;`
- `GO:GO:0005886; GO:0019580; GO:0022857; GO:0042836; GO:0097533; GO:0098656`

## Notes

Probable galactarate/D-glucarate transporter GarP
