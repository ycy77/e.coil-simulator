---
entity_id: "protein.P0ADV1"
entity_type: "protein"
name: "lptA"
source_database: "UniProt"
source_id: "P0ADV1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_01914, ECO:0000269|PubMed:17056748, ECO:0000269|PubMed:18480051, ECO:0000269|PubMed:20446753}. Note=Associates with both the inner membrane and the outer membrane."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lptA yhbN b3200 JW3167"
---

# lptA

`protein.P0ADV1`

## Static

- Type: `protein`
- Source: `UniProt:P0ADV1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_01914, ECO:0000269|PubMed:17056748, ECO:0000269|PubMed:18480051, ECO:0000269|PubMed:20446753}. Note=Associates with both the inner membrane and the outer membrane.

## Enriched Summary

FUNCTION: Involved in the assembly of lipopolysaccharide (LPS). Required for the translocation of LPS from the inner membrane to the outer membrane. May form a bridge between the inner membrane and the outer membrane, via interactions with LptC and LptD, thereby facilitating LPS transfer across the periplasm. {ECO:0000255|HAMAP-Rule:MF_01914, ECO:0000269|PubMed:16765569, ECO:0000269|PubMed:17056748, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:18480051, ECO:0000269|PubMed:21169485}. LptA is an essential periplasmic component of the Lpt lipopolysaccharide (LPS) transport system. Depletion of LptA results in impaired lipopolysaccharide transport to the outer membrane ; a conditional mutant which contains inactivating point mutations in LptA rapidly stops growing when incubated at the restrictive temperature and newly synthesized LPS appears trapped on the periplasmic side of the inner membrane . LptA drives a specific, protein mediated, long lived association between proteoliposomes containing LptBFGC and LPS and proteliposomes containing LptDE . Purified LptA binds smooth and rough LPS; purified LptA binds to the lipid A domain of LPS . Over-expressed His-tagged LptA is found in the soluble periplasmic fraction of whole cell lysates . Untagged LptA, expressed at native levels fractionates with the outer membranes whilst His-tagged LptA fractionates with the inner membranes...

## Biological Role

Component of lipopolysaccharide transport system (complex.ecocyc.CPLX0-7992).

## Annotation

FUNCTION: Involved in the assembly of lipopolysaccharide (LPS). Required for the translocation of LPS from the inner membrane to the outer membrane. May form a bridge between the inner membrane and the outer membrane, via interactions with LptC and LptD, thereby facilitating LPS transfer across the periplasm. {ECO:0000255|HAMAP-Rule:MF_01914, ECO:0000269|PubMed:16765569, ECO:0000269|PubMed:17056748, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:18480051, ECO:0000269|PubMed:21169485}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7992|complex.ecocyc.CPLX0-7992]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3200|gene.b3200]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADV1`
- `KEGG:ecj:JW3167;eco:b3200;ecoc:C3026_17415;`
- `GeneID:86862403;93778781;947920;`
- `GO:GO:0001530; GO:0009279; GO:0015920; GO:0017089; GO:0030288; GO:0042597; GO:0042802; GO:0043165; GO:1990351`

## Notes

Lipopolysaccharide export system protein LptA
