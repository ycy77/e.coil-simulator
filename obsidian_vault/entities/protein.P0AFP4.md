---
entity_id: "protein.P0AFP4"
entity_type: "protein"
name: "ybbO"
source_database: "UniProt"
source_id: "P0AFP4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybbO b0493 JW0482"
---

# ybbO

`protein.P0AFP4`

## Static

- Type: `protein`
- Source: `UniProt:P0AFP4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized oxidoreductase YbbO (EC 1.-.-.-) YbbO is an NADP+-dependent aldehyde reductase that showed broad substrate activity toward aldehydes with a preference for long-chain fatty aldehydes . Among the substrates tested by , it has the highest activity toward hexanal and octanal ; showed that the enzyme has maximal activity with C16 and C18 chain length aldehydes. A broad survey of aldehyde reductases showed that YbbO was one of several endogenous aldehyde reductases that contribute to the degradation of desired aldehyde end products of metabolic engineering . In recombinant E. coli expressing a β-carotene biosynthesis pathway and β-carotene 15',15'-monooxygenase, production of retinol can be increased by overexpressing ybbO . Deletion of ybbO reduces long chain fatty alcohol production from externally added substrates by 90% .

## Biological Role

Catalyzes ALCOHOL-DEHYDROGENASE-NADPORNOP+-RXN (reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN), RXN0-7119 (reaction.ecocyc.RXN0-7119).

## Annotation

Uncharacterized oxidoreductase YbbO (EC 1.-.-.-)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN|reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7119|reaction.ecocyc.RXN0-7119]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0493|gene.b0493]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFP4`
- `KEGG:ecj:JW0482;eco:b0493;`
- `GeneID:93776956;945337;`
- `GO:GO:0008106; GO:0008202; GO:0016491`
- `EC:1.-.-.-`

## Notes

Uncharacterized oxidoreductase YbbO (EC 1.-.-.-)
