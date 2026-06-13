---
entity_id: "protein.P0A794"
entity_type: "protein"
name: "pdxJ"
source_database: "UniProt"
source_id: "P0A794"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdxJ b2564 JW2548"
---

# pdxJ

`protein.P0A794`

## Static

- Type: `protein`
- Source: `UniProt:P0A794`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the complicated ring closure reaction between the two acyclic compounds 1-deoxy-D-xylulose-5-phosphate (DXP) and 3-amino-2-oxopropyl phosphate (1-amino-acetone-3-phosphate or AAP) to form pyridoxine 5'-phosphate (PNP) and inorganic phosphate. {ECO:0000269|PubMed:10225425}. Pyridoxine 5'-phosphate synthase (PdxJ) is one of the key enzymes in de novo pyridoxine 5'-phosphate synthesis. It catalyzes a complicated ring-closure reaction involving the condensation of 1-deoxy-D-xylulose 5-phosphate (DXP) and 3-amino-1-hydroxyacetone 1-phosphate to form pyridoxine 5'-phosphate (PNP) . Crystal structures of PdxJ have been solved . The enzyme is an octamer in solution . The octamer is organized as a tetramer of active dimers; each monomer consists of a (β/α)8 TIM barrel domain. Structures of enzyme/substrate and enzyme/product complexes allowed localization of the active site within a deep cavity which is closed in the presence of the product . Each subunit of the octamer has a unique conformation that is correlated with the occupancy of the active site. The substrate-binding sites are located at the interface of two subunits . A reaction mechanism involving Schiff base formation, water elimination and addition, phosphate elimination, ring closure, and various proton shifts has been proposed...

## Biological Role

Catalyzes pyridoxine 5'-phosphate synthase (reaction.R05838). Component of pyridoxine 5'-phosphate synthase (complex.ecocyc.CPLX0-321).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the complicated ring closure reaction between the two acyclic compounds 1-deoxy-D-xylulose-5-phosphate (DXP) and 3-amino-2-oxopropyl phosphate (1-amino-acetone-3-phosphate or AAP) to form pyridoxine 5'-phosphate (PNP) and inorganic phosphate. {ECO:0000269|PubMed:10225425}.

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R05838|reaction.R05838]] `KEGG` `database` - via EC:2.6.99.2
- `is_component_of` --> [[complex.ecocyc.CPLX0-321|complex.ecocyc.CPLX0-321]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b2564|gene.b2564]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A794`
- `KEGG:ecj:JW2548;eco:b2564;ecoc:C3026_14205;`
- `GeneID:86860685;947039;`
- `GO:GO:0005829; GO:0008615; GO:0033856; GO:0042802`
- `EC:2.6.99.2`

## Notes

Pyridoxine 5'-phosphate synthase (PNP synthase) (EC 2.6.99.2)
