---
entity_id: "protein.P69910"
entity_type: "protein"
name: "gadB"
source_database: "UniProt"
source_id: "P69910"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:12912902}. Membrane {ECO:0000269|PubMed:12912902}. Note=Localized exclusively in the cytoplasm at neutral pH, but is recruited to the membrane when the pH falls."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gadB b1493 JW1488"
---

# gadB

`protein.P69910`

## Static

- Type: `protein`
- Source: `UniProt:P69910`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:12912902}. Membrane {ECO:0000269|PubMed:12912902}. Note=Localized exclusively in the cytoplasm at neutral pH, but is recruited to the membrane when the pH falls.

## Enriched Summary

FUNCTION: Converts glutamate to gamma-aminobutyrate (GABA), consuming one intracellular proton in the reaction. The gad system helps to maintain a near-neutral intracellular pH when cells are exposed to extremely acidic conditions. The ability to survive transit through the acidic conditions of the stomach is essential for successful colonization of the mammalian host by commensal and pathogenic bacteria. GadB, a glutamate decarboxylase enzyme, is part of the glutamate-dependent acid resistance system 2 (AR2) which confers resistance to extreme acid conditions. There are two distinct E. coli GAD polypeptides which are highly similar to one another. AR2 also protects the cell during anaerobic phosphate starvation when glutamate is available by preventing damage from weak acids produced from carbohydrate fermentation. gadABC mutants have reduced viability after anaerobic phosphate starvation compared to wild-type . The crystal structure of GadB has been determined at acidic and neutral pH to resolutions of 2.0 and 2.3 Å, respectively . GadB is hexameric . At neutral pH GadB is inactive and is found in the cytosol, but when it becomes active at acidic pH, GadB associates with the membrane . Crystal structures of the autoinhibited, bromide-bound, and iodide-bound forms have been determined to 1.90, 3.15, and 1.95 Å, respectively...

## Biological Role

Catalyzes L-glutamate 1-carboxy-lyase (4-aminobutanoate-forming) (reaction.R00261), L-aspartate 1-carboxy-lyase (beta-alanine-forming) (reaction.R00489). Component of glutamate decarboxylase B (complex.ecocyc.GLUTDECARBOXB-CPLX).

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
- `is_component_of` --> [[complex.ecocyc.GLUTDECARBOXB-CPLX|complex.ecocyc.GLUTDECARBOXB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b1493|gene.b1493]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69910`
- `KEGG:ecj:JW1488;eco:b1493;ecoc:C3026_08645;`
- `GeneID:75171580;946058;`
- `GO:GO:0004351; GO:0005829; GO:0006538; GO:0016020; GO:0030170; GO:0051454`
- `EC:4.1.1.15`

## Notes

Glutamate decarboxylase beta (GAD-beta) (EC 4.1.1.15)
