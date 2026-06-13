---
entity_id: "protein.P77454"
entity_type: "protein"
name: "glsA1"
source_database: "UniProt"
source_id: "P77454"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glsA1 ybaS b0485 JW0474"
---

# glsA1

`protein.P77454`

## Static

- Type: `protein`
- Source: `UniProt:P77454`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Glutaminase 1 (EC 3.5.1.2) GlsA (YbaS) is a glutaminase that is highly selective for L-glutamine. Based on the pH profile of the enzymatic activity, GlsA was proposed to correspond to the previously described GLUTAMINA-CPLX of E. coli B. Glutamine binding exhibits positive cooperativity . Together with the antiporter XASA-MONOMER GadC, GlsA constitutes an acid resistance system. GlsA. which is activated by acidic conditions, converts GLN to GLT and neutralizes H+ by producing ammonia, which binds a proton to form ammonium . A crystal structure of unliganded GlsA has been solved at 1.6 Å resolution; an active site has been predicted, and site-directed mutagenesis confirmed the importance of various conserved residues for catalytic activity. The S66 residue is proposed to act as a catalytic nucleophile, and the enzyme is predicted to employ a β-lactamase-like catalytic mechanism . Under certain growth conditions, a glsA deletion mutant shows a reduced growth rate . glsA is required for glutamine-mediated acid resistance . Expression of glsA is increased during acid shock . glsA is associated with isobutanol tolerance in an engineered E. coli strain . Review:

## Biological Role

Catalyzes L-glutamine amidohydrolase (reaction.R00256). Component of glutaminase 1 (complex.ecocyc.CPLX0-7694).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

Glutaminase 1 (EC 3.5.1.2)

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00256|reaction.R00256]] `KEGG` `database` - via EC:3.5.1.2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7694|complex.ecocyc.CPLX0-7694]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0485|gene.b0485]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77454`
- `KEGG:ecj:JW0474;eco:b0485;ecoc:C3026_02385;`
- `GeneID:946187;`
- `GO:GO:0004359; GO:0006537; GO:0006543; GO:0010447; GO:0032991; GO:0045926`
- `EC:3.5.1.2`

## Notes

Glutaminase 1 (EC 3.5.1.2)
