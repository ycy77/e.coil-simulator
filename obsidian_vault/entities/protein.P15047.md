---
entity_id: "protein.P15047"
entity_type: "protein"
name: "entA"
source_database: "UniProt"
source_id: "P15047"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "entA b0596 JW0588"
---

# entA

`protein.P15047`

## Static

- Type: `protein`
- Source: `UniProt:P15047`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine. Catalyzes the reversible NAD-dependent oxidation of the C3-hydroxyl group of 2,3-dihydro-2,3-dihydroxybenzoate (2,3-diDHB), producing the transient intermediate 2-hydroxy-3-oxo-4,6-cyclohexadiene-1-carboxylate, which undergoes rapid aromatization to the final product, 2,3-dihydroxybenzoate (2,3-DHB). Only the compounds with a C3-hydroxyl group such as methyl 2,3-dihydro-2,3-dihydroxybenzoate, methyl-3-hydroxy-1,4-cyclohexadiene-1-carboxylate, trans-3-hydroxy-2-cyclohexene-1-carboxylate, cis-3-hydroxy-4-cyclohexene-1-carboxylate, cis-3-hydroxycyclohexane-1-carboxylic acid are oxidized to the corresponding ketone products. The stereospecificity of the C3 allylic alcohol group oxidation is 3R in a 1R,3R dihydro substrate. It can also increase the DHB-AMP ligase activity of EntE by interaction EntE. {ECO:0000269|PubMed:21166461, ECO:0000269|PubMed:2144454, ECO:0000269|PubMed:2521622}.

## Biological Role

Component of 2,3-dihydro-2,3-dihydroxybenzoate dehydrogenase (complex.ecocyc.ENTA-CPLX).

## Enriched Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine. Catalyzes the reversible NAD-dependent oxidation of the C3-hydroxyl group of 2,3-dihydro-2,3-dihydroxybenzoate (2,3-diDHB), producing the transient intermediate 2-hydroxy-3-oxo-4,6-cyclohexadiene-1-carboxylate, which undergoes rapid aromatization to the final product, 2,3-dihydroxybenzoate (2,3-DHB). Only the compounds with a C3-hydroxyl group such as methyl 2,3-dihydro-2,3-dihydroxybenzoate, methyl-3-hydroxy-1,4-cyclohexadiene-1-carboxylate, trans-3-hydroxy-2-cyclohexene-1-carboxylate, cis-3-hydroxy-4-cyclohexene-1-carboxylate, cis-3-hydroxycyclohexane-1-carboxylic acid are oxidized to the corresponding ketone products. The stereospecificity of the C3 allylic alcohol group oxidation is 3R in a 1R,3R dihydro substrate. It can also increase the DHB-AMP ligase activity of EntE by interaction EntE. {ECO:0000269|PubMed:21166461, ECO:0000269|PubMed:2144454, ECO:0000269|PubMed:2521622}.

## Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ENTA-CPLX|complex.ecocyc.ENTA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0596|gene.b0596]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15047`
- `KEGG:ecj:JW0588;eco:b0596;ecoc:C3026_02975;`
- `GeneID:945284;`
- `GO:GO:0005829; GO:0008667; GO:0009239; GO:0032991; GO:0042802`
- `EC:1.3.1.28`

## Notes

2,3-dihydro-2,3-dihydroxybenzoate dehydrogenase (DiDHB-DH) (EC 1.3.1.28) (Trans-2,3-dihydro-2,3-dihydroxybenzoate dehydrogenase)
