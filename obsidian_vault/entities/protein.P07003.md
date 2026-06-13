---
entity_id: "protein.P07003"
entity_type: "protein"
name: "poxB"
source_database: "UniProt"
source_id: "P07003"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00850, ECO:0000269|PubMed:365232, ECO:0000305|PubMed:5336022}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_00850, ECO:0000269|PubMed:365232, ECO:0000305|PubMed:5336022}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_00850, ECO:0000269|PubMed:365232}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "poxB b0871 JW0855"
---

# poxB

`protein.P07003`

## Static

- Type: `protein`
- Source: `UniProt:P07003`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00850, ECO:0000269|PubMed:365232, ECO:0000305|PubMed:5336022}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_00850, ECO:0000269|PubMed:365232, ECO:0000305|PubMed:5336022}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_00850, ECO:0000269|PubMed:365232}.

## Enriched Summary

FUNCTION: A peripheral cell membrane enzyme that catalyzes the oxidative decarboxylation of pyruvate to form acetate and CO(2). It channels electrons from the cytoplasm to the respiratory chain at the cell membrane via ubiquinone (By similarity) (PubMed:18988747, PubMed:2663858, PubMed:365232). The main pathway for acetate production during stationary phase (PubMed:16080684). {ECO:0000255|HAMAP-Rule:MF_00850, ECO:0000269|PubMed:16080684, ECO:0000269|PubMed:18988747, ECO:0000269|PubMed:2663858, ECO:0000269|PubMed:365232}. Pyruvate oxidase is a peripheral membrane enzyme that catalyzes the oxidative decarboxylation of pyruvate to form acetate and CO2. The reaction is coupled to the electron transport chain via ubiquinone. Metabolism of pyruvate by pyruvate oxidase is less efficient than the route via PYRUVATEDEH-CPLX (PDH); however, the pyruvate oxidase route is important for wild-type growth efficiency and responsible for a significant amount of pyruvate metabolism under aerobic conditions . PoxB is the main pathway for acetate production in stationary phase . Under aerobic phosphate starvation conditions, pyruvate flux is diverted from PDH to PoxB, which may decrease oxidative stress...

## Biological Role

Catalyzes pyruvate:ubiquinone oxidoreductase (reaction.R03145). Component of pyruvate oxidase (complex.ecocyc.PYRUVOXID-CPLX).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: A peripheral cell membrane enzyme that catalyzes the oxidative decarboxylation of pyruvate to form acetate and CO(2). It channels electrons from the cytoplasm to the respiratory chain at the cell membrane via ubiquinone (By similarity) (PubMed:18988747, PubMed:2663858, PubMed:365232). The main pathway for acetate production during stationary phase (PubMed:16080684). {ECO:0000255|HAMAP-Rule:MF_00850, ECO:0000269|PubMed:16080684, ECO:0000269|PubMed:18988747, ECO:0000269|PubMed:2663858, ECO:0000269|PubMed:365232}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03145|reaction.R03145]] `KEGG` `database` - via EC:1.2.5.1
- `is_component_of` --> [[complex.ecocyc.PYRUVOXID-CPLX|complex.ecocyc.PYRUVOXID-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0871|gene.b0871]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07003`
- `KEGG:ecj:JW0855;eco:b0871;ecoc:C3026_05415;`
- `GeneID:946132;`
- `GO:GO:0000287; GO:0005829; GO:0005886; GO:0008289; GO:0030976; GO:0032991; GO:0042802; GO:0042867; GO:0048039; GO:0050660; GO:0052737`
- `EC:1.2.5.1`

## Notes

Pyruvate dehydrogenase [ubiquinone] (EC 1.2.5.1) (Pyruvate oxidase) (POX) (Pyruvate:ubiquinone-8 oxidoreductase)
