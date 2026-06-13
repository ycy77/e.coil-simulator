---
entity_id: "protein.P10378"
entity_type: "protein"
name: "entE"
source_database: "UniProt"
source_id: "P10378"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Membrane {ECO:0000269|PubMed:10692387}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "entE b0594 JW0586"
---

# entE

`protein.P10378`

## Static

- Type: `protein`
- Source: `UniProt:P10378`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Membrane {ECO:0000269|PubMed:10692387}.

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine. The serine trilactone serves as a scaffolding for the three catechol functionalities that provide hexadentate coordination for the tightly ligated iron(2+) atoms. EntE processes via a two-step adenylation-ligation reaction (bi-uni-uni-bi ping-pong mechanism). First, it catalyzes the activation of the carboxylate group of 2,3-dihydroxy-benzoate (DHB), via a reversible ATP-dependent pyrophosphate exchange reactions to yield the acyladenylate intermediate 2,3-dihydroxybenzoyl-AMP. It can also transfer AMP to salicylate, 2,4-dihydroxybenzoate, gentisate and 2,3,4-trihydroxybenzoate. In the second step, DHB is transferred from 2,3-dihydroxybenzoyl-AMP onto the phosphopantetheinylated EntB (holo-EntB) to form DHB-holo-EntB. Then this product will serve in the formation of the amide bond between 2,3-dihydroxybenzoate (DHB) and L-serine. It can also transfer adenylated salicylate to holo-EntB. {ECO:0000269|PubMed:10688898, ECO:0000269|PubMed:16567620, ECO:0000269|PubMed:16632253, ECO:0000269|PubMed:19699210, ECO:0000269|PubMed:19852513, ECO:0000269|PubMed:20359185, ECO:0000269|PubMed:20845982, ECO:0000269|PubMed:21166461, ECO:0000269|PubMed:2531000, ECO:0000269|PubMed:9214294}.

## Biological Role

Component of 2,3-dihydroxybenzoate-[aryl-carrier protein] ligase (complex.ecocyc.ENTE-CPLX), enterobactin synthase (complex.ecocyc.ENTMULTI-CPLX).

## Enriched Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine. The serine trilactone serves as a scaffolding for the three catechol functionalities that provide hexadentate coordination for the tightly ligated iron(2+) atoms. EntE processes via a two-step adenylation-ligation reaction (bi-uni-uni-bi ping-pong mechanism). First, it catalyzes the activation of the carboxylate group of 2,3-dihydroxy-benzoate (DHB), via a reversible ATP-dependent pyrophosphate exchange reactions to yield the acyladenylate intermediate 2,3-dihydroxybenzoyl-AMP. It can also transfer AMP to salicylate, 2,4-dihydroxybenzoate, gentisate and 2,3,4-trihydroxybenzoate. In the second step, DHB is transferred from 2,3-dihydroxybenzoyl-AMP onto the phosphopantetheinylated EntB (holo-EntB) to form DHB-holo-EntB. Then this product will serve in the formation of the amide bond between 2,3-dihydroxybenzoate (DHB) and L-serine. It can also transfer adenylated salicylate to holo-EntB. {ECO:0000269|PubMed:10688898, ECO:0000269|PubMed:16567620, ECO:0000269|PubMed:16632253, ECO:0000269|PubMed:19699210, ECO:0000269|PubMed:19852513, ECO:0000269|PubMed:20359185, ECO:0000269|PubMed:20845982, ECO:0000269|PubMed:21166461, ECO:0000269|PubMed:2531000, ECO:0000269|PubMed:9214294}.

## Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ENTE-CPLX|complex.ecocyc.ENTE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.ENTMULTI-CPLX|complex.ecocyc.ENTMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0594|gene.b0594]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10378`
- `KEGG:ecj:JW0586;eco:b0594;ecoc:C3026_02965;`
- `GeneID:947426;`
- `GO:GO:0005524; GO:0005829; GO:0008668; GO:0009239; GO:0016020; GO:0016746; GO:0047527`
- `EC:6.2.1.71; 6.3.2.14`

## Notes

Enterobactin synthase component E (EC 6.3.2.14) (2,3-dihydroxybenzoate-AMP ligase) (DHB-AMP ligase) (2,3-dihydroxybenzoate-AMP synthase) (EC 6.2.1.71) (Dihydroxybenzoic acid-activating enzyme) (Enterochelin synthase E)
