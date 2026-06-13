---
entity_id: "protein.P05194"
entity_type: "protein"
name: "aroD"
source_database: "UniProt"
source_id: "P05194"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aroD b1693 JW1683"
---

# aroD

`protein.P05194`

## Static

- Type: `protein`
- Source: `UniProt:P05194`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the third step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids (AroAA). Catalyzes the cis-dehydration of 3-dehydroquinate (DHQ) and introduces the first double bond of the aromatic ring to yield 3-dehydroshikimate. The reaction involves the formation of an imine intermediate between the keto group of 3-dehydroquinate and the epsilon-amino group of a Lys-170 at the active site. {ECO:0000255|HAMAP-Rule:MF_00214, ECO:0000269|PubMed:13198937, ECO:0000269|PubMed:2950851, ECO:0000269|PubMed:3541912, ECO:0000269|PubMed:7592767}. 3-Dehydroquinate dehydratase (DHQ dehydratase) is involved in the 3rd step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. DHQ dehydratase catalyzes the conversion of DHQ to 3-dehydroshikimate and introduces the first double bond of the aromatic ring . The first step of the 3-dehydroquinase reaction involves the formation of an imine intermediate between the keto group of 3-dehydroquinate and the e-amino group of a lysine at the active site of the enzyme. Chemical modification and mutagenesis experiments have identified this lysine to be Lys-170 . In addition to the lysine side chain involved in imine formation, the enzyme also requires a basic group for proton abstraction...

## Biological Role

Component of 3-dehydroquinate dehydratase (complex.ecocyc.AROD-CPLX).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Involved in the third step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids (AroAA). Catalyzes the cis-dehydration of 3-dehydroquinate (DHQ) and introduces the first double bond of the aromatic ring to yield 3-dehydroshikimate. The reaction involves the formation of an imine intermediate between the keto group of 3-dehydroquinate and the epsilon-amino group of a Lys-170 at the active site. {ECO:0000255|HAMAP-Rule:MF_00214, ECO:0000269|PubMed:13198937, ECO:0000269|PubMed:2950851, ECO:0000269|PubMed:3541912, ECO:0000269|PubMed:7592767}.

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.AROD-CPLX|complex.ecocyc.AROD-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1693|gene.b1693]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05194`
- `KEGG:ecj:JW1683;eco:b1693;ecoc:C3026_09695;`
- `GeneID:946210;`
- `GO:GO:0003855; GO:0005829; GO:0008652; GO:0009073; GO:0009423; GO:0042803; GO:0046279`
- `EC:4.2.1.10`

## Notes

3-dehydroquinate dehydratase (3-dehydroquinase) (EC 4.2.1.10) (Type I DHQase) (Type I dehydroquinase) (DHQ1)
