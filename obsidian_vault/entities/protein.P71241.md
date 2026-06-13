---
entity_id: "protein.P71241"
entity_type: "protein"
name: "wcaJ"
source_database: "UniProt"
source_id: "P71241"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22408159}; Multi-pass membrane protein {ECO:0000269|PubMed:22408159}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wcaJ b2047 JW2032"
---

# wcaJ

`protein.P71241`

## Static

- Type: `protein`
- Source: `UniProt:P71241`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22408159}; Multi-pass membrane protein {ECO:0000269|PubMed:22408159}.

## Enriched Summary

FUNCTION: Is the initiating enzyme for colanic acid (CA) synthesis. Catalyzes the transfer of the glucose-1-phosphate moiety from UDP-Glc onto the carrier lipid undecaprenyl phosphate (C55-P), forming a phosphoanhydride bond yielding to glucosyl-pyrophosphoryl-undecaprenol (Glc-PP-C55). Also possesses a weak galactose-1-P transferase activity. {ECO:0000269|PubMed:22408159}. WcaJ belongs to the polyisoprenyl-phosphate hexose-1-phosphate transferase (PHPT) family and catalyzes the transfer of glucose-1-phosphate from UDP-glucose to undecaprenyl-phosphate , which is the initial step of colanic acid biosynthesis in E. coli . WcaJ was predicted to catalyze this reaction based on sequence similarity and its presence in a colanic acid biosynthesis operon . Experimental validation led to a revision of the predicted membrane topology of WcaJ and the PHPT family of enzymes. The enzyme comprises four canonical transmembrane helices followed by a cytoplasmic loop and an additional membrane domain that adopts a helix-break-helix structure that does not span the membrane, thus leading to cytoplasmic localization of the C terminus . Inactivation of wcaJ was used to increase the cellular pool of the colanic acid (CA) synthesis building block GDP-fucose . A wcaJ mutant produces nonmucoid colonies in an RcsA-overexpressing strain background...

## Biological Role

Catalyzes RXN-11791 (reaction.ecocyc.RXN-11791).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

FUNCTION: Is the initiating enzyme for colanic acid (CA) synthesis. Catalyzes the transfer of the glucose-1-phosphate moiety from UDP-Glc onto the carrier lipid undecaprenyl phosphate (C55-P), forming a phosphoanhydride bond yielding to glucosyl-pyrophosphoryl-undecaprenol (Glc-PP-C55). Also possesses a weak galactose-1-P transferase activity. {ECO:0000269|PubMed:22408159}.

## Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11791|reaction.ecocyc.RXN-11791]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2047|gene.b2047]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P71241`
- `KEGG:ecj:JW2032;eco:b2047;ecoc:C3026_11525;`
- `GeneID:946583;`
- `GO:GO:0005886; GO:0009103; GO:0009242; GO:0016757; GO:0089702`
- `EC:2.7.8.31`

## Notes

UDP-glucose:undecaprenyl-phosphate glucose-1-phosphate transferase (UDP-Glc:Und-P Glc-1-P transferase) (EC 2.7.8.31) (Colanic acid biosynthesis UDP-glucose lipid carrier transferase) (Glucosyl-P-P-undecaprenol synthase)
