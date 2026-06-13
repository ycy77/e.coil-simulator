---
entity_id: "protein.P00946"
entity_type: "protein"
name: "manA"
source_database: "UniProt"
source_id: "P00946"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "manA pmi b1613 JW1605"
---

# manA

`protein.P00946`

## Static

- Type: `protein`
- Source: `UniProt:P00946`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in the conversion of glucose to GDP-L-fucose, which can be converted to L-fucose, a capsular polysaccharide. Mannose-6-phosphate isomerase (phosphomannose isomerase, PMI) catalyzes the reversible isomerization of mannose-6-phosphate and fructose-6-phosphate. This reaction is the first committed step in the synthesis of GDP-α-D-mannose (see pathway PWY-5659). The enzyme is required for growth on mannose as the sole source of carbon and energy. It is also required for the formation of GDP-L-fucose, a building block of capsular polysaccharide (see pathways MANNCAT-PWY and COLANSYN-PWY). PMI activity is increased by growth on p-fluorophenylalanine (FPA), which leads to formation of mucoid colonies . A manA mutant is unable to grow on mannose as the sole source of carbon and energy and has a defect in the maintenance of colonization of the mouse intestine . The manA gene can be used as a selectable marker . Pmi: "phosphomannose isomerase" The E. coli enzyme is a type I PMI, a monofunctional, Zn2+-dependent metalloenzyme found in most bacteria and mammals . Crystal structures have been determined for the PMI from Salmonella typhimurium bound to metal atoms and substrate...

## Biological Role

Catalyzes D-mannose-6-phosphate aldose-ketose-isomerase (reaction.R00772), MANNPISOM-RXN (reaction.ecocyc.MANNPISOM-RXN). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Involved in the conversion of glucose to GDP-L-fucose, which can be converted to L-fucose, a capsular polysaccharide.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00772|reaction.R00772]] `KEGG` `database` - via EC:5.3.1.8
- `catalyzes` --> [[reaction.ecocyc.MANNPISOM-RXN|reaction.ecocyc.MANNPISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1613|gene.b1613]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00946`
- `KEGG:ecj:JW1605;eco:b1613;ecoc:C3026_09280;`
- `GeneID:75204457;944840;`
- `GO:GO:0004476; GO:0005829; GO:0008270; GO:0009242; GO:0009298; GO:0019309`
- `EC:5.3.1.8`

## Notes

Mannose-6-phosphate isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphomannose isomerase) (PMI)
