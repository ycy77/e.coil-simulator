---
entity_id: "protein.P0A877"
entity_type: "protein"
name: "trpA"
source_database: "UniProt"
source_id: "P0A877"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trpA b1260 JW1252"
---

# trpA

`protein.P0A877`

## Static

- Type: `protein`
- Source: `UniProt:P0A877`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The alpha subunit is responsible for the aldol cleavage of indoleglycerol phosphate to indole and glyceraldehyde 3-phosphate. The TrpA polypeptide (TSase α) functions as the α subunit of the tetrameric (α2-β2) tryptophan synthase complex . As a purified protein, the α subunit is a monomer. TSase α contains the binding site for indole-3-glycerol-phosphate (InGP) and can carry out the cleavage reaction of InGP to indole and glyceraldehyde-3-phosphate, also termed the α reaction. Within the physiological complex with the β subunit, the reaction rate is increased by 1-2 orders of magnitude (in ). TrpA has been shown to lack tryptophan residues . Numerous TrpA mutant studies have examined structure-function relationships in this protein. Mutations that affect catalytic activity , subunit interactions , conformational stability and folding have been identified. The crystal structure of the wild-type TrpA protein has been reported at 2.8 Å resolution , 2.5 Å resolution and 2.3 Å resolution . The crystal structure of a double mutant TrpA protein has been reported at 1.8 Å resolution . The TrpA protein has been structurally classified as a (beta alpha)(8) TIM barrel protein, a member of the common TIM barrel superfamily...

## Biological Role

Catalyzes L-serine hydro-lyase (adding indole; L-tryptophan-forming) (reaction.R00674), (1S,2R)-1-C-(indol-3-yl)glycerol 3-phosphate D-glyceraldehyde-3-phosphate-lyase (reaction.R02340), RXN0-2381 (reaction.ecocyc.RXN0-2381). Component of tryptophan synthase (complex.ecocyc.TRYPSYN).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: The alpha subunit is responsible for the aldol cleavage of indoleglycerol phosphate to indole and glyceraldehyde 3-phosphate.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00674|reaction.R00674]] `KEGG` `database` - via EC:4.2.1.20
- `catalyzes` --> [[reaction.R02340|reaction.R02340]] `KEGG` `database` - via EC:4.2.1.20
- `catalyzes` --> [[reaction.ecocyc.RXN0-2381|reaction.ecocyc.RXN0-2381]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.TRYPSYN|complex.ecocyc.TRYPSYN]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1260|gene.b1260]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A877`
- `KEGG:ecj:JW1252;eco:b1260;ecoc:C3026_07395;`
- `GeneID:75171374;946204;`
- `GO:GO:0000162; GO:0004834; GO:0005737; GO:0005829; GO:0009073; GO:0016829; GO:0060090`
- `EC:4.2.1.20`

## Notes

Tryptophan synthase alpha chain (EC 4.2.1.20)
