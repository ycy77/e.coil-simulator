---
entity_id: "protein.P23871"
entity_type: "protein"
name: "hemH"
source_database: "UniProt"
source_id: "P23871"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00323}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hemH popA visA b0475 JW0464"
---

# hemH

`protein.P23871`

## Static

- Type: `protein`
- Source: `UniProt:P23871`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00323}.

## Enriched Summary

FUNCTION: Catalyzes the ferrous insertion into protoporphyrin IX. {ECO:0000255|HAMAP-Rule:MF_00323}. Ferrochelatase is the terminal enzyme in the heme biosynthesis pathway and catalyzes the insertion of Fe2+ into protoporphyrin IX. Both eukaryotic and some microbial ferrochelatases have been shown to contain a [2Fe-2S] cluster ; however, no studies have been performed with the E. coli enzyme. A hemH mutant is sensitive to visible light due to the accumulation of protoporphyrin IX. This is similar to the defect observed in human protoporphyria . The defect in iron incorporation into protoporphyrin IX in a hemH mutant results in a defect in assembly of membrane-associated succinate-ubiquinone reductase . Expression of hemH is mildly regulated in response to heme availability and is activated by OxyR . VisA: "visible light-sensitive" HemH: "heme biosynthesis" Reviews:

## Biological Role

Catalyzes protoheme ferro-lyase (protoporphyrin-forming) (reaction.R00310), Fe-coproporphyrin-III ferro-lyase (coproporphyrin-III-forming) (reaction.R11329), PROTOHEMEFERROCHELAT-RXN (reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the ferrous insertion into protoporphyrin IX. {ECO:0000255|HAMAP-Rule:MF_00323}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00310|reaction.R00310]] `KEGG` `database` - via EC:4.98.1.1
- `catalyzes` --> [[reaction.R11329|reaction.R11329]] `KEGG` `database` - via EC:4.99.1.9
- `catalyzes` --> [[reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN|reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0475|gene.b0475]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23871`
- `KEGG:ecj:JW0464;eco:b0475;ecoc:C3026_02335;`
- `GeneID:947532;`
- `GO:GO:0004325; GO:0005737; GO:0006783; GO:0009416; GO:0046501; GO:0046872`
- `EC:4.98.1.1`

## Notes

Ferrochelatase (EC 4.98.1.1) (Heme synthase) (Protoheme ferro-lyase)
