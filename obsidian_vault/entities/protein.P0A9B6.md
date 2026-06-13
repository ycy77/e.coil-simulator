---
entity_id: "protein.P0A9B6"
entity_type: "protein"
name: "epd"
source_database: "UniProt"
source_id: "P0A9B6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "epd gapB b2927 JW2894"
---

# epd

`protein.P0A9B6`

## Static

- Type: `protein`
- Source: `UniProt:P0A9B6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the NAD-dependent conversion of D-erythrose 4-phosphate to 4-phosphoerythronate. {ECO:0000269|PubMed:9182530, ECO:0000269|PubMed:9696782}. A tetrameric D-erythrose-4-phosphate dehydrogenase encoded by the epd gene in E. coli catalyses the first reaction of NAD-dependent oxidation of D-erythrose-4-phosphate in the de novo pyridoxine 5'-phosphate (vitamin B6) and pyridoxal 5'-phosphate biosynthesis. This enzyme shows an efficient non-phosphorylating erythrose 4-phosphate dehydrogenase activity and a low phosphorylating glyceraldehyde 3-phosphate dehydrogenase activity . Most of the amino acids that are essential for the chemical mechanism and for the binding of substrates and cofactors of the enzyme encoded by epd is conserved for its glycolytic enzyme GAPDH-A-MONOMER activity . There is a common chemical mechanism for the oxidation of glyceraldehyde 3-phosphate and erythrose 4-phosphate catalyzed by Epd. The reactions proceed through a two-step mechanism involving a covalent thioacyl intermediate with Cys-149. The limiting step is associated with the formation of this thioacyl intermediate. Replacement of Cys-149 abolishes the catalytic efficiency of Epd. The binding of erythrose 4-phosphate to the enzyme-NAD complex favors the formation of a ternary complex efficient for the hydride transfer...

## Biological Role

Component of D-erythrose-4-phosphate dehydrogenase (complex.ecocyc.ERYTH4PDEHYDROG-CPLX).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the NAD-dependent conversion of D-erythrose 4-phosphate to 4-phosphoerythronate. {ECO:0000269|PubMed:9182530, ECO:0000269|PubMed:9696782}.

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ERYTH4PDEHYDROG-CPLX|complex.ecocyc.ERYTH4PDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2927|gene.b2927]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9B6`
- `KEGG:ecj:JW2894;eco:b2927;ecoc:C3026_16035;`
- `GeneID:93779071;947413;`
- `GO:GO:0004365; GO:0005829; GO:0006006; GO:0008615; GO:0042823; GO:0048001; GO:0051287`
- `EC:1.2.1.72`

## Notes

D-erythrose-4-phosphate dehydrogenase (E4PDH) (EC 1.2.1.72)
