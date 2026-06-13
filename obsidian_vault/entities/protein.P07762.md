---
entity_id: "protein.P07762"
entity_type: "protein"
name: "glgB"
source_database: "UniProt"
source_id: "P07762"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glgB b3432 JW3395"
---

# glgB

`protein.P07762`

## Static

- Type: `protein`
- Source: `UniProt:P07762`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of the alpha-1,6-glucosidic linkages in glycogen by scission of a 1,4-alpha-linked oligosaccharide from growing alpha-1,4-glucan chains and the subsequent attachment of the oligosaccharide to the alpha-1,6 position. {ECO:0000250}. Gycogen branching enzyme (GlgB) belongs to the glycosyl hydrolase GH13 family of enzymes and catalyzes the formation of the branched α-1,6-glucosidic linkages from the growing α-1,4-glucan chain during glycogen biosynthesis. When cells are grown in Kornberg medium, a threshold level of around 4 nmoles (dry weight) of ppGpp is necessary to trigger net glycogen accumulation . Biochemical studies of the enzyme have been performed using E. coli B . Gycogen branching enzyme has a preference for transferring chains between 5 and 16 glucose units. The minimum chain length required for branching is 12 . The enzyme appears to prefer A chains as acceptors and to form branch linkages at the third glucose residue from the reducing end of the acceptor chain . The reaction products of N-terminally truncated enzymes show an altered branching pattern . The Glu459 residue is important for specific activity and substrate specificity of the enzyme , and the Tyr300 residue is required for enzymatic activity and thermostability . Crystal structures of GlgB have been solved...

## Biological Role

Catalyzes 1,4-alpha-D-glucan:1,4-alpha-D-glucan 6-alpha-D-(1,4-alpha-D-glucano)-transferase (reaction.R02110), R06186 (reaction.R06186), GLYCOGEN-BRANCH-RXN (reaction.ecocyc.GLYCOGEN-BRANCH-RXN).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of the alpha-1,6-glucosidic linkages in glycogen by scission of a 1,4-alpha-linked oligosaccharide from growing alpha-1,4-glucan chains and the subsequent attachment of the oligosaccharide to the alpha-1,6 position. {ECO:0000250}.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R02110|reaction.R02110]] `KEGG` `database` - via EC:2.4.1.18
- `catalyzes` --> [[reaction.R06186|reaction.R06186]] `KEGG` `database` - via EC:2.4.1.18
- `catalyzes` --> [[reaction.ecocyc.GLYCOGEN-BRANCH-RXN|reaction.ecocyc.GLYCOGEN-BRANCH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3432|gene.b3432]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07762`
- `KEGG:ecj:JW3395;eco:b3432;ecoc:C3026_18605;`
- `GeneID:93778557;947940;`
- `GO:GO:0003844; GO:0004553; GO:0005737; GO:0005829; GO:0005978; GO:0006974; GO:0043169`
- `EC:2.4.1.18`

## Notes

1,4-alpha-glucan branching enzyme GlgB (EC 2.4.1.18) (1,4-alpha-D-glucan:1,4-alpha-D-glucan 6-glucosyl-transferase) (Alpha-(1->4)-glucan branching enzyme) (Glycogen branching enzyme) (BE)
