---
entity_id: "protein.P0AAA9"
entity_type: "protein"
name: "zraP"
source_database: "UniProt"
source_id: "P0AAA9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:9694902}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "zraP yjaI zra b4002 JW5546"
---

# zraP

`protein.P0AAA9`

## Static

- Type: `protein`
- Source: `UniProt:P0AAA9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:9694902}.

## Enriched Summary

FUNCTION: Part of the Zra signaling pathway, an envelope stress response (ESR) system composed of the periplasmic accessory protein ZraP, the histidine kinase ZraS and the transcriptional regulator ZraR (PubMed:26438879, PubMed:30389436, PubMed:33309686). The ZraPSR system contributes to antibiotic resistance and is important for membrane integrity in the presence of membrane-targeting biocides (PubMed:30389436). ZraP acts as a modulator which has both a regulatory and a chaperone function (PubMed:26438879, PubMed:30389436). The zinc-bound form of ZraP modulates the response of the ZraPSR system by inhibiting the expression of the zra genes, probably by interacting with ZraS (PubMed:26438879). Participation to the cell protection arises mainly from this repressor function (PubMed:30389436). Also displays chaperone properties in vitro and protects malate dehydrogenase (MDH) from thermal denaturation at 45 degrees Celsius (PubMed:26438879). Binds zinc, copper, nickel, cobalt but not cadmium or manganese (PubMed:22094925, PubMed:26438879, PubMed:30616070, PubMed:9694902). In vitro, has a higher affinity for copper than for zinc (PubMed:26438879, PubMed:30616070). Is the main zinc containing protein under zinc stress conditions (PubMed:22094925). However, the system has no direct role in zinc or copper resistance (PubMed:26438879, PubMed:30616070)...

## Biological Role

Component of signaling pathway modulator ZraP (complex.ecocyc.CPLX0-8204).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the Zra signaling pathway, an envelope stress response (ESR) system composed of the periplasmic accessory protein ZraP, the histidine kinase ZraS and the transcriptional regulator ZraR (PubMed:26438879, PubMed:30389436, PubMed:33309686). The ZraPSR system contributes to antibiotic resistance and is important for membrane integrity in the presence of membrane-targeting biocides (PubMed:30389436). ZraP acts as a modulator which has both a regulatory and a chaperone function (PubMed:26438879, PubMed:30389436). The zinc-bound form of ZraP modulates the response of the ZraPSR system by inhibiting the expression of the zra genes, probably by interacting with ZraS (PubMed:26438879). Participation to the cell protection arises mainly from this repressor function (PubMed:30389436). Also displays chaperone properties in vitro and protects malate dehydrogenase (MDH) from thermal denaturation at 45 degrees Celsius (PubMed:26438879). Binds zinc, copper, nickel, cobalt but not cadmium or manganese (PubMed:22094925, PubMed:26438879, PubMed:30616070, PubMed:9694902). In vitro, has a higher affinity for copper than for zinc (PubMed:26438879, PubMed:30616070). Is the main zinc containing protein under zinc stress conditions (PubMed:22094925). However, the system has no direct role in zinc or copper resistance (PubMed:26438879, PubMed:30616070). {ECO:0000269|PubMed:22094925, ECO:0000269|PubMed:26438879, ECO:0000269|PubMed:30389436, ECO:0000269|PubMed:30616070, ECO:0000269|PubMed:33309686, ECO:0000269|PubMed:9694902}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8204|complex.ecocyc.CPLX0-8204]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b4002|gene.b4002]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAA9`
- `KEGG:ecj:JW5546;eco:b4002;ecoc:C3026_21615;`
- `GeneID:93777892;948507;`
- `GO:GO:0005507; GO:0008270; GO:0016151; GO:0030288; GO:0036460; GO:0042802; GO:0050897`

## Notes

Signaling pathway modulator ZraP (Zinc resistance-associated protein) (Zra periplasmic repressor partner) (Zra system accessory protein ZraP)
