---
entity_id: "protein.P38051"
entity_type: "protein"
name: "menF"
source_database: "UniProt"
source_id: "P38051"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "menF yfbA b2265 JW2260"
---

# menF

`protein.P38051`

## Static

- Type: `protein`
- Source: `UniProt:P38051`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of chorismate to isochorismate. Can also catalyze the reverse reaction, but with a lower efficiency. {ECO:0000269|PubMed:17240978, ECO:0000269|PubMed:8764478, ECO:0000269|PubMed:9150206, ECO:0000269|PubMed:9795253}.

## Biological Role

Component of isochorismate synthase MenF (complex.ecocyc.MENF-CPLX).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of chorismate to isochorismate. Can also catalyze the reverse reaction, but with a lower efficiency. {ECO:0000269|PubMed:17240978, ECO:0000269|PubMed:8764478, ECO:0000269|PubMed:9150206, ECO:0000269|PubMed:9795253}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.MENF-CPLX|complex.ecocyc.MENF-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2265|gene.b2265]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P38051`
- `KEGG:ecj:JW2260;eco:b2265;ecoc:C3026_12650;`
- `GeneID:946712;`
- `GO:GO:0000287; GO:0008909; GO:0009234`
- `EC:5.4.4.2`

## Notes

Isochorismate synthase MenF (EC 5.4.4.2) (Isochorismate hydroxymutase) (Isochorismate mutase)
