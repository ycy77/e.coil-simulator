---
entity_id: "protein.P24174"
entity_type: "protein"
name: "manC"
source_database: "UniProt"
source_id: "P24174"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "manC cpsB rfbM b2049 JW2034"
---

# manC

`protein.P24174`

## Static

- Type: `protein`
- Source: `UniProt:P24174`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the capsular polysaccharide colanic acid. Mannose-1-phosphate guanylyltransferase is involved in the biosynthesis of the capsular polysaccharide colanic acid. Colanic acid is a high molecular weight repeating polymer of glucose, galactose, fucose and glucuronic acid (see PWY-8243). The enzyme has only been assayed in crude extract . cpsB expression is positively regulated by the RcsCBA two-component signal transduction system . A lon mutation increases the half life of RcsA and thus increases cpsB expression . cpsB expression is increased by osmotic shock . The cpsB transcription level is decreased in rpoB mutants . In a metabolic engineering study, an E. coli mutant was constructed that included a deletion of manA and the cps gene cluster, and carried a plasmid harboring cpsG and cpsB from E. coli as well as another plasmid harboring msg from Rhodothermus marinus. This strain was used in the production of the osmolyte mannosylglycerate . Recombinant E. coli strains overexpressing E. coli K-12 mannose-1-phosphate guanylytransferase, phosphomannomutase and glucokinase (either together or separately) were used to produce GDP-mannose. GDP-mannose is a precursor of fucosyloligosaccharides which are of pharmaceutical interest (see pathway PWY-66). cpsB is induced under biofilm conditions . CpsB: "capsular polysaccharide synthesis" Reviews:

## Biological Role

Catalyzes 2.7.7.13-RXN (reaction.ecocyc.2.7.7.13-RXN).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the capsular polysaccharide colanic acid.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.7.13-RXN|reaction.ecocyc.2.7.7.13-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2049|gene.b2049]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24174`
- `KEGG:ecj:JW2034;eco:b2049;ecoc:C3026_11535;`
- `GeneID:946580;`
- `GO:GO:0004475; GO:0005525; GO:0006972; GO:0009103; GO:0009242; GO:0009298`
- `EC:2.7.7.13`

## Notes

Mannose-1-phosphate guanylyltransferase (EC 2.7.7.13) (GDP-mannose pyrophosphorylase) (GMP) (GMPP)
