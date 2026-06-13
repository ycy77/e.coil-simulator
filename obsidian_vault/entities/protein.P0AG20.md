---
entity_id: "protein.P0AG20"
entity_type: "protein"
name: "relA"
source_database: "UniProt"
source_id: "P0AG20"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "relA b2784 JW2755"
---

# relA

`protein.P0AG20`

## Static

- Type: `protein`
- Source: `UniProt:P0AG20`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: In eubacteria ppGpp (guanosine 3'-diphosphate 5'-diphosphate) is a mediator of the stringent response which coordinates a variety of cellular activities in response to changes in nutritional abundance. This enzyme catalyzes the formation of pppGpp which is then hydrolyzed to form ppGpp. The second messengers ppGpp and c-di-GMP together control biofilm formation in response to translational stress; ppGpp represses biofilm formation while c-di-GMP induces it. ppGpp activates transcription of CsrA-antagonistic small RNAs CsrB and CsrC, which down-regulate CsrA's action on translation during the stringent response (PubMed:21488981). {ECO:0000269|PubMed:14622409, ECO:0000269|PubMed:19460094, ECO:0000269|PubMed:21488981, ECO:0000269|PubMed:26051177}. RelA is a key enzyme involved in the stringent response of Escherichia coli to amino acid starvation. It activates the synthesis of the global regulatory molecules of the stringent response, ppGpp and pppGpp (referred to collectively as (p)ppGpp), via a ribosomal mechanism (see below). The amino acid sequence of RelA has been shown to be extensively related to that of SPOT-MONOMER . The RelA (p)ppGpp synthetase activity is referred to as (p)ppGpp synthetase I, or PSI. RelA also contains an inactive hydrolase domain (reviewed in )...

## Biological Role

Catalyzes ATP:GTP 3'-diphosphotransferase (reaction.R00429), GDPPYPHOSKIN-RXN (reaction.ecocyc.GDPPYPHOSKIN-RXN), GTPPYPHOSKIN-RXN (reaction.ecocyc.GTPPYPHOSKIN-RXN).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: In eubacteria ppGpp (guanosine 3'-diphosphate 5'-diphosphate) is a mediator of the stringent response which coordinates a variety of cellular activities in response to changes in nutritional abundance. This enzyme catalyzes the formation of pppGpp which is then hydrolyzed to form ppGpp. The second messengers ppGpp and c-di-GMP together control biofilm formation in response to translational stress; ppGpp represses biofilm formation while c-di-GMP induces it. ppGpp activates transcription of CsrA-antagonistic small RNAs CsrB and CsrC, which down-regulate CsrA's action on translation during the stringent response (PubMed:21488981). {ECO:0000269|PubMed:14622409, ECO:0000269|PubMed:19460094, ECO:0000269|PubMed:21488981, ECO:0000269|PubMed:26051177}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00429|reaction.R00429]] `KEGG` `database` - via EC:2.7.6.5
- `catalyzes` --> [[reaction.ecocyc.GDPPYPHOSKIN-RXN|reaction.ecocyc.GDPPYPHOSKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GTPPYPHOSKIN-RXN|reaction.ecocyc.GTPPYPHOSKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2784|gene.b2784]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG20`
- `KEGG:ecj:JW2755;eco:b2784;`
- `GeneID:93779214;947244;`
- `GO:GO:0005524; GO:0005525; GO:0008728; GO:0008893; GO:0015949; GO:0015969; GO:0015970; GO:0016301; GO:0042594; GO:0051302`
- `EC:2.7.6.5`

## Notes

GTP pyrophosphokinase (EC 2.7.6.5) ((p)ppGpp synthase) (ATP:GTP 3'-pyrophosphotransferase) (ppGpp synthase I)
