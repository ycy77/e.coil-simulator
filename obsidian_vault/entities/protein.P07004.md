---
entity_id: "protein.P07004"
entity_type: "protein"
name: "proA"
source_database: "UniProt"
source_id: "P07004"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00412}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "proA b0243 JW0233"
---

# proA

`protein.P07004`

## Static

- Type: `protein`
- Source: `UniProt:P07004`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00412}.

## Enriched Summary

FUNCTION: Catalyzes the NADPH-dependent reduction of L-glutamate 5-phosphate into L-glutamate 5-semialdehyde and phosphate. The product spontaneously undergoes cyclization to form 1-pyrroline-5-carboxylate. {ECO:0000255|HAMAP-Rule:MF_00412, ECO:0000269|PubMed:7034716, ECO:0000269|PubMed:7035170}.

## Biological Role

Component of glutamate-5-semialdehyde dehydrogenase (complex.ecocyc.GLUTSEMIALDEHYDROG-CPLX).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the NADPH-dependent reduction of L-glutamate 5-phosphate into L-glutamate 5-semialdehyde and phosphate. The product spontaneously undergoes cyclization to form 1-pyrroline-5-carboxylate. {ECO:0000255|HAMAP-Rule:MF_00412, ECO:0000269|PubMed:7034716, ECO:0000269|PubMed:7035170}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GLUTSEMIALDEHYDROG-CPLX|complex.ecocyc.GLUTSEMIALDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0243|gene.b0243]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07004`
- `KEGG:ecj:JW0233;eco:b0243;ecoc:C3026_01155;ecoc:C3026_23890;`
- `GeneID:93777150;946680;`
- `GO:GO:0004350; GO:0005829; GO:0042802; GO:0050661; GO:0055129`
- `EC:1.2.1.41`

## Notes

Gamma-glutamyl phosphate reductase (GPR) (EC 1.2.1.41) (Glutamate-5-semialdehyde dehydrogenase) (Glutamyl-gamma-semialdehyde dehydrogenase) (GSA dehydrogenase)
