---
entity_id: "protein.P0AFA7"
entity_type: "protein"
name: "nhaB"
source_database: "UniProt"
source_id: "P0AFA7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01599, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01599}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nhaB b1186 JW1175"
---

# nhaB

`protein.P0AFA7`

## Static

- Type: `protein`
- Source: `UniProt:P0AFA7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01599, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01599}.

## Enriched Summary

FUNCTION: Na(+)/H(+) antiporter that extrudes sodium in exchange for external protons (PubMed:1317851, PubMed:7929345, PubMed:8019504, PubMed:8093613). Catalyzes the exchange of 3 H(+) per 2 Na(+) (PubMed:7929345). Can also transport lithium (PubMed:8019504). Essential for regulation of intracellular pH under alkaline conditions (PubMed:7822245). Is necessary for growth on Na(+)/symport substrates such as glutamate and proline under conditions in which nhaA is not expressed, such as acidic pH and low Na(+) concentration (PubMed:8093613). {ECO:0000269|PubMed:1317851, ECO:0000269|PubMed:7822245, ECO:0000269|PubMed:7929345, ECO:0000269|PubMed:8019504, ECO:0000269|PubMed:8093613}. nhaB encodes a Na+:H+ antiporter implicated in alkaline pH homeostasis. E. coli contains other transporters which mediate active proton uptake for alkaline pH homeostasis including CPLX0-7629 "NhaA" (the prominent Na+:H+ antiporter), CHAA-MONOMER "ChaA", CMR-MONOMER "MdfA" and YJIO-MONOMER "MdtM", each of which may function under varying conditions of external pH and cation composition (see ) Purified, reconstituted NhaB is an electrogenic antiporter with a stoichiometry of 3H+:2Na+ . NhaB also contributes to Li+ export (Li+:H+ antiport) at high external Li+ concentrations (0.2 M LiCl) . The E...

## Biological Role

Catalyzes Na+:proton antiport (reaction.ecocyc.TRANS-RXN-130).

## Annotation

FUNCTION: Na(+)/H(+) antiporter that extrudes sodium in exchange for external protons (PubMed:1317851, PubMed:7929345, PubMed:8019504, PubMed:8093613). Catalyzes the exchange of 3 H(+) per 2 Na(+) (PubMed:7929345). Can also transport lithium (PubMed:8019504). Essential for regulation of intracellular pH under alkaline conditions (PubMed:7822245). Is necessary for growth on Na(+)/symport substrates such as glutamate and proline under conditions in which nhaA is not expressed, such as acidic pH and low Na(+) concentration (PubMed:8093613). {ECO:0000269|PubMed:1317851, ECO:0000269|PubMed:7822245, ECO:0000269|PubMed:7929345, ECO:0000269|PubMed:8019504, ECO:0000269|PubMed:8093613}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-130|reaction.ecocyc.TRANS-RXN-130]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1186|gene.b1186]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFA7`
- `KEGG:ecj:JW1175;eco:b1186;ecoc:C3026_06985;`
- `GeneID:75171290;75203299;944822;`
- `GO:GO:0005886; GO:0010226; GO:0015385`

## Notes

Na(+)/H(+) antiporter NhaB (Sodium/proton antiporter NhaB)
