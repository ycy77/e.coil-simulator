---
entity_id: "protein.P00861"
entity_type: "protein"
name: "lysA"
source_database: "UniProt"
source_id: "P00861"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lysA b2838 JW2806"
---

# lysA

`protein.P00861`

## Static

- Type: `protein`
- Source: `UniProt:P00861`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Specifically catalyzes the decarboxylation of meso-diaminopimelate (meso-DAP) to L-lysine. Is not active against the DD- or LL-isomers of diaminopimelate. {ECO:0000269|PubMed:11856852, ECO:0000269|PubMed:14343156, ECO:0000269|PubMed:18508763}.

## Biological Role

Catalyzes meso-2,6-diaminoheptanedioate carboxy-lyase (L-lysine-forming) (reaction.R00451). Component of diaminopimelate decarboxylase (complex.ecocyc.DIAMINOPIMDECARB-CPLX).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Specifically catalyzes the decarboxylation of meso-diaminopimelate (meso-DAP) to L-lysine. Is not active against the DD- or LL-isomers of diaminopimelate. {ECO:0000269|PubMed:11856852, ECO:0000269|PubMed:14343156, ECO:0000269|PubMed:18508763}.

## Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00451|reaction.R00451]] `KEGG` `database` - via EC:4.1.1.20
- `is_component_of` --> [[complex.ecocyc.DIAMINOPIMDECARB-CPLX|complex.ecocyc.DIAMINOPIMDECARB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2838|gene.b2838]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00861`
- `KEGG:ecj:JW2806;eco:b2838;ecoc:C3026_15585;`
- `GeneID:947313;`
- `GO:GO:0008836; GO:0009089; GO:0030170; GO:0042803`
- `EC:4.1.1.20`

## Notes

Diaminopimelate decarboxylase (DAP decarboxylase) (DAPDC) (EC 4.1.1.20)
