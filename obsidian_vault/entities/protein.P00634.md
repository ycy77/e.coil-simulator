---
entity_id: "protein.P00634"
entity_type: "protein"
name: "phoA"
source_database: "UniProt"
source_id: "P00634"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phoA b0383 JW0374"
---

# phoA

`protein.P00634`

## Static

- Type: `protein`
- Source: `UniProt:P00634`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

Alkaline phosphatase (APase) (EC 3.1.3.1) Alkaline phosphatase is a periplasmic, homodimeric enzyme that catalyses the hydrolysis and transphosphorylation of a wide variety of phosphate monoesters . The reaction proceeds through a phosphoseryl intermediate with the subsequent release of inorganic phosphate and alcohol . The transphosphorylation reaction results in the transfer of a phosphoryl group to the alcohol of acceptors such as Tris or ethanolamine . Alkaline phosphatase is a metalloenzyme, binding two zinc atoms and one magnesium ion per monomer . The amount of alkaline phosphatase is optimal when cells are starved for phosphate - which is the most common environment for E. coli in the human gut - and is much reduced when there is an excess of phosphate . Under conditions of limiting phosphate, alkaline phosphatase accounts for approximately 6% of the total protein synthesized . Alkaline phosphatase occurs in three major forms designated isozymes 1, 2 and 3 whose relative proportions are dependent on the growth conditions . The isozymes are differentiated by the presence or absence of an NH2-terminal arginine residue: present in both subunits of isozyme 1, absent in both subunits of isozyme 3 and heterogenous in isozyme 2 . Removal of the N-terminal arginine is catalysed by the membrane-associated, proteolytic enzyme EG10488 "Iap"...

## Biological Role

Catalyzes phosphate-monoester phosphohydrolase (reaction.R00626), glycerone phosphate phosphohydrolase (reaction.R01010), thiamin monophosphate phosphohydrolase (reaction.R02135). Component of alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

Alkaline phosphatase (APase) (EC 3.1.3.1)

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00626|reaction.R00626]] `KEGG` `database` - via EC:3.1.3.1
- `catalyzes` --> [[reaction.R01010|reaction.R01010]] `KEGG` `database` - via EC:3.1.3.1
- `catalyzes` --> [[reaction.R02135|reaction.R02135]] `KEGG` `database` - via EC:3.1.3.1
- `is_component_of` --> [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0383|gene.b0383]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00634`
- `KEGG:ecj:JW0374;eco:b0383;`
- `GeneID:945041;`
- `GO:GO:0000287; GO:0004035; GO:0004721; GO:0008270; GO:0030288; GO:0030613; GO:0033748; GO:0042597`
- `EC:3.1.3.1`

## Notes

Alkaline phosphatase (APase) (EC 3.1.3.1)
