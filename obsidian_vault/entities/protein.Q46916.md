---
entity_id: "protein.Q46916"
entity_type: "protein"
name: "gudP"
source_database: "UniProt"
source_id: "Q46916"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gudP ygcZ b2789 JW2760"
---

# gudP

`protein.Q46916`

## Static

- Type: `protein`
- Source: `UniProt:Q46916`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Probably involved in the uptake of galactarate and/or D-glucarate (Probable). May also transport D-glycerate (Probable). {ECO:0000305|PubMed:10762278, ECO:0000305|PubMed:9772162}. GudP is a putative substrate:proton symporter which is implicated in uptake of the diacid sugars, galactarate and D-glucarate gudP encodes a potential D-glucarate or galactarate transporter; it is located in an operon with gudD, encoding a D-glucarate dehydratase and gudX, encoding a 'glucarate dehydratase-related protein' . A Φ(gudP-lacZ) transcriptional fusion is induced in cultures grown in the presence of galactarate, D-glucarate or D-glycerate . In the Transporter Classification Database GudP is a member of the Anion:Cation Symporter (ACS) Family within the Major Facilitator Superfamily (MFS) . The genes encoding enzymes involved in D-glucarate and galactarate metabolism are organized in three transcriptional units ; during aerobic growth with galactarate, D-glucarate or D-glycerate expression of these genes is coordinately regulated by the transcription factor CdaR .

## Biological Role

Catalyzes galactarate:proton symport (reaction.ecocyc.TRANS-RXN0-203), D-glucarate:proton symport (reaction.ecocyc.TRANS-RXN0-204), D-glycerate:proton symport (reaction.ecocyc.TRANS-RXN0-523). Transports D-Glycerate (molecule.C00258), D-Glucarate (molecule.C00818), D-Galactarate (molecule.C00879), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Probably involved in the uptake of galactarate and/or D-glucarate (Probable). May also transport D-glycerate (Probable). {ECO:0000305|PubMed:10762278, ECO:0000305|PubMed:9772162}.

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-203|reaction.ecocyc.TRANS-RXN0-203]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-204|reaction.ecocyc.TRANS-RXN0-204]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-523|reaction.ecocyc.TRANS-RXN0-523]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00258|molecule.C00258]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00818|molecule.C00818]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00879|molecule.C00879]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2789|gene.b2789]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46916`
- `KEGG:ecj:JW2760;eco:b2789;ecoc:C3026_15335;`
- `GeneID:947265;`
- `GO:GO:0005886; GO:0019580; GO:0022857; GO:0042836; GO:0098656`

## Notes

Probable galactarate/D-glucarate transporter GudP
