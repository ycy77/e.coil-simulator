---
entity_id: "protein.P23256"
entity_type: "protein"
name: "malY"
source_database: "UniProt"
source_id: "P23256"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "malY b1622 JW1614"
---

# malY

`protein.P23256`

## Static

- Type: `protein`
- Source: `UniProt:P23256`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Acts as a beta-cystathionase and as a repressor of the maltose regulon.

## Biological Role

Catalyzes L-cysteine hydrogen-sulfide-lyase (deaminating; pyruvate-forming) (reaction.R00782). Component of negative regulator of MalT activity/cystathionine β-lyase (complex.ecocyc.CPLX0-8092).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Acts as a beta-cystathionase and as a repressor of the maltose regulon.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00782|reaction.R00782]] `KEGG` `database` - via EC:4.4.1.13
- `is_component_of` --> [[complex.ecocyc.CPLX0-8092|complex.ecocyc.CPLX0-8092]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1622|gene.b1622]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23256`
- `KEGG:ecj:JW1614;eco:b1622;ecoc:C3026_09325;`
- `GeneID:945937;`
- `GO:GO:0009086; GO:0030170; GO:0042803; GO:0047804; GO:0080146; GO:0140297`
- `EC:4.4.1.13`

## Notes

Protein MalY [Includes: Cystathionine beta-lyase MalY (CBL) (EC 4.4.1.13) (Beta-cystathionase MalY) (Cysteine lyase MalY) (Cysteine-S-conjugate beta-lyase MalY); Maltose regulon modulator]
