---
entity_id: "protein.P0A867"
entity_type: "protein"
name: "talA"
source_database: "UniProt"
source_id: "P0A867"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "talA b2464 JW2448"
---

# talA

`protein.P0A867`

## Static

- Type: `protein`
- Source: `UniProt:P0A867`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Transaldolase is important for the balance of metabolites in the pentose-phosphate pathway. Transaldolase is an enzyme of the pentose phosphate pathway, where it catalyzes the reversible interconversion of glyceraldehyde-3-phosphate and sedoheptulose-7-phosphate to fructose-6-phosphate and erythrose-4-phosphate. The reversibility of this reaction and carbon flux through the pentose phosphate pathway has been addressed both experimentally (summarized in ) and theoretically . There are two closely related transaldolases in E. coli, encoded by talA and talB. Transaldolase A has not been biochemically characterized. Under aerobic growth conditions with glucose as the sole source of carbon, a talA mutant shows a similar growth rate, but a decreased acetate production and increased biomass yield compared to wild type . A talA mutant is more sensitive to gentamicin than wild-type . Protein levels of TalA are induced by osmotic stress only under aerobic conditions and by exposure to mercury . talA belongs to the σS regulon ; its expression increases in early stationary phase just as expression of talB decreases . Expression is negatively regulated by ArcA and positively regulated by ppGpp . Transcription of talA is induced by the CreBC two-component system in minimal media growth conditions . TalA: "transaldolase A" Reviews:

## Biological Role

Catalyzes TRANSALDOL-RXN (reaction.ecocyc.TRANSALDOL-RXN).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Transaldolase is important for the balance of metabolites in the pentose-phosphate pathway.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANSALDOL-RXN|reaction.ecocyc.TRANSALDOL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2464|gene.b2464]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A867`
- `KEGG:ecj:JW2448;eco:b2464;ecoc:C3026_13670;`
- `GeneID:75204264;947006;`
- `GO:GO:0004801; GO:0005829; GO:0005975; GO:0009052`
- `EC:2.2.1.2`

## Notes

Transaldolase A (EC 2.2.1.2)
