---
entity_id: "protein.P64461"
entity_type: "protein"
name: "lsrG"
source_database: "UniProt"
source_id: "P64461"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02051}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lsrG yneC b1518 JW1511"
---

# lsrG

`protein.P64461`

## Static

- Type: `protein`
- Source: `UniProt:P64461`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02051}.

## Enriched Summary

FUNCTION: Involved in the degradation of phospho-AI-2, thereby terminating induction of the lsr operon and closing the AI-2 signaling cycle. Catalyzes the conversion of (4S)-4-hydroxy-5-phosphonooxypentane-2,3-dione (P-DPD) to 3-hydroxy-5-phosphonooxypentane-2,4-dione (P-HPD). {ECO:0000255|HAMAP-Rule:MF_02051, ECO:0000269|PubMed:17274596, ECO:0000269|PubMed:21454635}. LsrG is an enzyme involved in the degradation of the quorum-sensing regulator Autoinducer 2 (AI-2). Purified LsrG degrades CPD-10551 phospho-AI-2 (4-hydroxy-2,3-pentanedione 5-phosphate) . The reaction products were later shown to be a mixture of CPD0-2467 (P-HPD) and CPD0-2468 (P-TPO); CPD0-2466 was proposed to be a reaction intermediate . It is now thought that LsrG catalyzes the isomerization reaction from phospho-AI-2 to P-HPD, and that P-HPD exists in equilibrium with its hydrated form, P-TPO . A crystal structure of the enzyme has been solved at 1.8 Å resolution. Mutants in predicted active site residues N25, E54, H65, H70 have reduced or no catalytic activity in vitro . LsrG: "luxS regulated"

## Biological Role

Catalyzes (4S)-4-hydroxy-5-phosphooxypentane-2,3-dione aldose-ketose-isomerase (reaction.R10939), RXN-15216 (reaction.ecocyc.RXN-15216), RXN0-6720 (reaction.ecocyc.RXN0-6720).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Involved in the degradation of phospho-AI-2, thereby terminating induction of the lsr operon and closing the AI-2 signaling cycle. Catalyzes the conversion of (4S)-4-hydroxy-5-phosphonooxypentane-2,3-dione (P-DPD) to 3-hydroxy-5-phosphonooxypentane-2,4-dione (P-HPD). {ECO:0000255|HAMAP-Rule:MF_02051, ECO:0000269|PubMed:17274596, ECO:0000269|PubMed:21454635}.

## Pathways

- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R10939|reaction.R10939]] `KEGG` `database` - via EC:5.3.1.32
- `catalyzes` --> [[reaction.ecocyc.RXN-15216|reaction.ecocyc.RXN-15216]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6720|reaction.ecocyc.RXN0-6720]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1518|gene.b1518]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64461`
- `KEGG:ecj:JW1511;eco:b1518;ecoc:C3026_08775;`
- `GeneID:75057398;946073;`
- `GO:GO:0002952; GO:0005829; GO:0009372; GO:0016491; GO:0016853`
- `EC:5.3.1.32`

## Notes

(4S)-4-hydroxy-5-phosphonooxypentane-2,3-dione isomerase (EC 5.3.1.32) (Autoinducer 2-degrading protein LsrG) (AI-2-degrading protein LsrG) (Phospho-(S)-4,5-dihydroxy-2,3-pentanedione isomerase) (Phospho-AI-2 isomerase)
