---
entity_id: "protein.P69908"
entity_type: "protein"
name: "gadA"
source_database: "UniProt"
source_id: "P69908"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gadA gadS b3517 JW3485"
---

# gadA

`protein.P69908`

## Static

- Type: `protein`
- Source: `UniProt:P69908`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts glutamate to gamma-aminobutyrate (GABA), consuming one intracellular proton in the reaction. The gad system helps to maintain a near-neutral intracellular pH when cells are exposed to extremely acidic conditions. The ability to survive transit through the acidic conditions of the stomach is essential for successful colonization of the mammalian host by commensal and pathogenic bacteria. GadA, a glutamate decarboxylase enzyme, is part of the glutamate-dependent acid resistance system 2 (AR2) which confers resistance to extreme acid conditions. There are two distinct E. coli GAD polypeptides which are highly similar to one another. AR2 also protects the cell during anaerobic phosphate starvation when glutamate is available by preventing damage from weak acids produced from carbohydrate fermentation. gadABC mutants have reduced viability after anaerobic phosphate starvation compared to wild-type . The crystal structure of the hexameric GadA in complex with the substrate analog glutarate has been determined to a resolution of 2.05 Å . Regulation has been described . Using a method that distinguishes N-phosphorylation from O-phosphorylation, N-phosphorylation was detected in vitro . EG50009 was significantly upregulated in simulated microgravity .

## Biological Role

Catalyzes L-glutamate 1-carboxy-lyase (4-aminobutanoate-forming) (reaction.R00261), L-aspartate 1-carboxy-lyase (beta-alanine-forming) (reaction.R00489). Component of glutamate decarboxylase A (complex.ecocyc.GLUTDECARBOXA-CPLX).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Converts glutamate to gamma-aminobutyrate (GABA), consuming one intracellular proton in the reaction. The gad system helps to maintain a near-neutral intracellular pH when cells are exposed to extremely acidic conditions. The ability to survive transit through the acidic conditions of the stomach is essential for successful colonization of the mammalian host by commensal and pathogenic bacteria.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00261|reaction.R00261]] `KEGG` `database` - via EC:4.1.1.15
- `catalyzes` --> [[reaction.R00489|reaction.R00489]] `KEGG` `database` - via EC:4.1.1.15
- `is_component_of` --> [[complex.ecocyc.GLUTDECARBOXA-CPLX|complex.ecocyc.GLUTDECARBOXA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3517|gene.b3517]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69908`
- `KEGG:ecj:JW3485;eco:b3517;ecoc:C3026_19055;`
- `GeneID:93778467;948027;`
- `GO:GO:0004351; GO:0005829; GO:0006538; GO:0016020; GO:0030170; GO:0051454`
- `EC:4.1.1.15`

## Notes

Glutamate decarboxylase alpha (GAD-alpha) (EC 4.1.1.15)
