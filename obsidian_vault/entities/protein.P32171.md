---
entity_id: "protein.P32171"
entity_type: "protein"
name: "rhaB"
source_database: "UniProt"
source_id: "P32171"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhaB b3904 JW3875"
---

# rhaB

`protein.P32171`

## Static

- Type: `protein`
- Source: `UniProt:P32171`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the catabolism of L-rhamnose (6-deoxy-L-mannose). It could also play a role in the metabolism of some rare sugars such as L-fructose. Catalyzes the transfer of the gamma-phosphate group from ATP to the 1-hydroxyl group of L-rhamnulose to yield L-rhamnulose 1-phosphate. Uridine triphosphate (UTP), cytidine 5-triphosphate (CTP), guanosine 5-triphosphate (GTP), and thymidine triphosphate (TTP) also can act as phosphoryl donors. It can also phosphorylate L-fuculose and L-xylulose. {ECO:0000255|HAMAP-Rule:MF_01535, ECO:0000269|PubMed:14264882, ECO:0000269|PubMed:16674975, ECO:0000269|PubMed:5341476}. L-rhamnulose kinase catalyzes the second step of rhamnose degradation, the phosphorylation of rhamnulose. The substrate spectrum of L-rhamnulose kinase has been investigated; the enzyme shows a broad tolerance for structural modifications of the natural substrate . Rare sugars have been modeled into the active center of the crystal structure . L-rhamnulose kinase is a monomer in solution . Crystal structures of L-rhamnulose kinase as an apo- and holo-enzyme as well as the ternary complex including the sugar have been determined and show that the enzyme belongs to the hexokinase-hsp70-actin superfamily. A catalytic mechanism has been proposed . A mutated form of RhaB has been shown to also phosphorylate L-xylulose to L-xylulose 1-phosphate and to allow growth of E...

## Biological Role

Catalyzes ATP:L-xylulose 1-phosphotransferase (reaction.R01902), RHAMNULOKIN-RXN (reaction.ecocyc.RHAMNULOKIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Involved in the catabolism of L-rhamnose (6-deoxy-L-mannose). It could also play a role in the metabolism of some rare sugars such as L-fructose. Catalyzes the transfer of the gamma-phosphate group from ATP to the 1-hydroxyl group of L-rhamnulose to yield L-rhamnulose 1-phosphate. Uridine triphosphate (UTP), cytidine 5-triphosphate (CTP), guanosine 5-triphosphate (GTP), and thymidine triphosphate (TTP) also can act as phosphoryl donors. It can also phosphorylate L-fuculose and L-xylulose. {ECO:0000255|HAMAP-Rule:MF_01535, ECO:0000269|PubMed:14264882, ECO:0000269|PubMed:16674975, ECO:0000269|PubMed:5341476}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01902|reaction.R01902]] `KEGG` `database` - via EC:2.7.1.5
- `catalyzes` --> [[reaction.ecocyc.RHAMNULOKIN-RXN|reaction.ecocyc.RHAMNULOKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3904|gene.b3904]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32171`
- `KEGG:ecj:JW3875;eco:b3904;ecoc:C3026_21105;`
- `GeneID:948399;`
- `GO:GO:0005524; GO:0005829; GO:0008993; GO:0019301`
- `EC:2.7.1.5`

## Notes

L-Rhamnulokinase (RhaB) (RhuK) (EC 2.7.1.5) (ATP:L-rhamnulose phosphotransferase) (L-rhamnulose 1-kinase) (Rhamnulose kinase)
