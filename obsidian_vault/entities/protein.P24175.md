---
entity_id: "protein.P24175"
entity_type: "protein"
name: "manB"
source_database: "UniProt"
source_id: "P24175"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "manB cpsG rfbL b2048 JW2033"
---

# manB

`protein.P24175`

## Static

- Type: `protein`
- Source: `UniProt:P24175`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the capsular polysaccharide colanic acid. Colanic acid is an atypical type I capsule that is present in E. coli K-12. It is a high molecular weight polymer composed of six-residue repeat units made up of glucose, galactose, glucuronic acid and fucose. Phosphomannomutase is part of the GDP-mannose biosynthetic pathway, which is a precursor for colanic acid production. In E. coli K-12 phosphomannomutase is coded for by the cpsG gene, but in other E. coli strains it is the rfbK gene that codes for the enzyme (see pathways PWY-5659 and COLANSYN-PWY). In a metabolic engineering study, an E. coli mutant was constructed that included a deletion of manA and the cps gene cluster, and carried a plasmid harboring cpsG and cpsB from E. coli as well as another plasmid harboring msg from Rhodothermus marinus. This strain was used in the production of the osmolyte mannosylglycerate . In another study TDP-2-deoxy-glucose was produced in a one-pot enzymatic synthesis from TMP and 2-deoxy glucose-6-phosphate using the purified recombinant E. coli K-12 enzymes phsophomannomutase, TDP-glucose synthase, TMP kinase, and acetate kinase. The replacement of phosphoglucomutase with phosphomannomutase resulted in higher conversion of 2-deoxy glucose-6-phosphate. Such TDP-sugars are useful in the development of new antibiotics Recombinant E...

## Biological Role

Catalyzes PHOSMANMUT-RXN (reaction.ecocyc.PHOSMANMUT-RXN).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the capsular polysaccharide colanic acid.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PHOSMANMUT-RXN|reaction.ecocyc.PHOSMANMUT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2048|gene.b2048]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24175`
- `KEGG:ecj:JW2033;eco:b2048;ecoc:C3026_11530;`
- `GeneID:946574;`
- `GO:GO:0000287; GO:0004615; GO:0009103; GO:0009298`
- `EC:5.4.2.8`

## Notes

Phosphomannomutase (PMM) (EC 5.4.2.8)
