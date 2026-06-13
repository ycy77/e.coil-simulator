---
entity_id: "protein.P0A879"
entity_type: "protein"
name: "trpB"
source_database: "UniProt"
source_id: "P0A879"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trpB b1261 JW1253"
---

# trpB

`protein.P0A879`

## Static

- Type: `protein`
- Source: `UniProt:P0A879`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The beta subunit is responsible for the synthesis of L-tryptophan from indole and L-serine.

## Biological Role

Catalyzes L-serine hydro-lyase (adding indole; L-tryptophan-forming) (reaction.R00674), (1S,2R)-1-C-(indol-3-yl)glycerol 3-phosphate D-glyceraldehyde-3-phosphate-lyase (reaction.R02340). Component of tryptophan synthase, β subunit dimer (complex.ecocyc.CPLX0-2401), tryptophan synthase (complex.ecocyc.TRYPSYN).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: The beta subunit is responsible for the synthesis of L-tryptophan from indole and L-serine.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00674|reaction.R00674]] `KEGG` `database` - via EC:4.2.1.20
- `catalyzes` --> [[reaction.R02340|reaction.R02340]] `KEGG` `database` - via EC:4.2.1.20
- `is_component_of` --> [[complex.ecocyc.CPLX0-2401|complex.ecocyc.CPLX0-2401]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TRYPSYN|complex.ecocyc.TRYPSYN]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1261|gene.b1261]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A879`
- `KEGG:ecj:JW1253;eco:b1261;ecoc:C3026_07400;`
- `GeneID:75203373;945768;`
- `GO:GO:0000162; GO:0004834; GO:0005737; GO:0005829; GO:0009073; GO:0030170; GO:0042802; GO:0042803`
- `EC:4.2.1.20`

## Notes

Tryptophan synthase beta chain (EC 4.2.1.20)
