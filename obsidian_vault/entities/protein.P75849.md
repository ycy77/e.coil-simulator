---
entity_id: "protein.P75849"
entity_type: "protein"
name: "gloC"
source_database: "UniProt"
source_id: "P75849"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gloC ycbL b0927 JW0910"
---

# gloC

`protein.P75849`

## Static

- Type: `protein`
- Source: `UniProt:P75849`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Type II glyoxalase, isozyme of GloB, that hydrolyzes (R)-S-lactoylglutathione to (R)-lactate and glutathione. Plays a minor contribution to methylglyoxal (MG) detoxification in E.coli, compared to GloB. The two isoenzymes have additive effects and ensure maximal MG degradation. {ECO:0000269|PubMed:25670698}. GloC is a type II glyoxalase that is an isozyme of GLYOXII-MONOMER GloB. It plays a minor role in methylglyoxal detoxification . The metal binding properties of the ortholog from Salmonella enterica serovar typhimurium 14028s have been studied . The S. enterica enzyme was found to have glyoxalase II activity . Single gloB and gloC mutants show decreased methylglyoxal tolerance; a ΔgloBC double deletion mutant is more sensitive to methylglyoxal than either single mutant . GloC in E. coli was shown to interact with the enzyme G7767-MONOMER in a protein-enzyme interactions (PEIs) study that examined the connection between protein-protein interactions (PPIs) and metabolomics networks studied in 22 different environmental conditions. This PEI may have a metabolic regulatory role in the PWY-5386 pathway involved in pyruvate metabolism, in part because the PEI is conserved across many other bacterial taxa . Review:

## Biological Role

Catalyzes (R)-S-lactoylglutathione hydrolase (reaction.R01736), GLYOXII-RXN (reaction.ecocyc.GLYOXII-RXN). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Type II glyoxalase, isozyme of GloB, that hydrolyzes (R)-S-lactoylglutathione to (R)-lactate and glutathione. Plays a minor contribution to methylglyoxal (MG) detoxification in E.coli, compared to GloB. The two isoenzymes have additive effects and ensure maximal MG degradation. {ECO:0000269|PubMed:25670698}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01736|reaction.R01736]] `KEGG` `database` - via EC:3.1.2.6
- `catalyzes` --> [[reaction.ecocyc.GLYOXII-RXN|reaction.ecocyc.GLYOXII-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0927|gene.b0927]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75849`
- `KEGG:ecj:JW0910;eco:b0927;ecoc:C3026_05695;`
- `GeneID:945551;`
- `GO:GO:0004416; GO:0005829; GO:0019243; GO:0046872`
- `EC:3.1.2.6`

## Notes

Hydroxyacylglutathione hydrolase GloC (EC 3.1.2.6) (Accessory type II glyoxalase) (Glyoxalase II 2) (GlxII-2)
