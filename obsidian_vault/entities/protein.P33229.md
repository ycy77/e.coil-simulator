---
entity_id: "protein.P33229"
entity_type: "protein"
name: "ralR"
source_database: "UniProt"
source_id: "P33229"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ralR lar ral ydaB b1348 JW5208"
---

# ralR

`protein.P33229`

## Static

- Type: `protein`
- Source: `UniProt:P33229`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. Upon overexpression inhibits growth and reduces colony-forming units in both the presence and absence of the Rac prophage, cells become filamentous. Has deoxyribonuclease activity (probably endonucleolytic), does not digest RNA. Its toxic effects are neutralized by sRNA antitoxin RalA, which is encoded in trans on the opposite DNA strand (PubMed:24748661). Has RAL-like activity (PubMed:7476171). {ECO:0000269|PubMed:24748661, ECO:0000269|PubMed:7476171}. RalR (Lar) is the toxin of the RalRA type I toxin-antitoxin system. RalR is a non-specific DNA endonuclease that cleaves both methylated and unmethylated DNA. A RalR mutant with reduced toxicity also has lost endonuclease activity . Overexpression of RalR inhibits growth. In the presence of the small RNA RalA, the level of RalR protein expressed from a plasmid is decreased . Growth of a ΔralR or ΔralRA mutant is more severely inhibited by fosfomycin than wild type . ralR is part of the lambdoid prophage Rac. It was shown to be involved in restriction alleviation and enhancement of modification by EcoKI (a type I restriction/modification system) , but not in restriction alleviation of type III restriction systems . RalR (Lar) and the phage λ Ral protein show 25% sequence identity .

## Biological Role

Catalyzes RXN0-7100 (reaction.ecocyc.RXN0-7100). Bound by Magnesium cation (molecule.C00305), Ca2+ (molecule.ecocyc.CA_2).

## Annotation

FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. Upon overexpression inhibits growth and reduces colony-forming units in both the presence and absence of the Rac prophage, cells become filamentous. Has deoxyribonuclease activity (probably endonucleolytic), does not digest RNA. Its toxic effects are neutralized by sRNA antitoxin RalA, which is encoded in trans on the opposite DNA strand (PubMed:24748661). Has RAL-like activity (PubMed:7476171). {ECO:0000269|PubMed:24748661, ECO:0000269|PubMed:7476171}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7100|reaction.ecocyc.RXN0-7100]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1348|gene.b1348]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33229`
- `KEGG:ecj:JW5208;eco:b1348;ecoc:C3026_07895;`
- `GeneID:945914;`
- `GO:GO:0009307; GO:0046677; GO:1990238`
- `EC:3.1.-.-`

## Notes

Endodeoxyribonuclease toxin RalR (DNase RalR) (EC 3.1.-.-) (Restriction alleviation and modification enhancement protein) (Toxin RalR)
