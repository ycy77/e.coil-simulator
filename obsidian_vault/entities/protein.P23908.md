---
entity_id: "protein.P23908"
entity_type: "protein"
name: "argE"
source_database: "UniProt"
source_id: "P23908"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01108, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argE b3957 JW3929"
---

# argE

`protein.P23908`

## Static

- Type: `protein`
- Source: `UniProt:P23908`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01108, ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of the amide bond of N(2)-acetylated L-amino acids. Cleaves the acetyl group from N-acetyl-L-ornithine to form L-ornithine, an intermediate in L-arginine biosynthesis pathway, and a branchpoint in the synthesis of polyamines. {ECO:0000255|HAMAP-Rule:MF_01108, ECO:0000269|PubMed:10684608, ECO:0000269|PubMed:1551850}. E. coli acetylornithine deacetylase (ArgE) is a homodimer that catalyses the deacylation of N2-acetyl-L-ornithine to yield ornithine and acetate . Ornithine is an obligatory intermediate in the arginine biosynthetic pathway and a branch point in the synthesis of polyamines . It is a metalloenzyme that is activated by cobalt and inorganic phosphate . The enzyme contains two metal binding sites: a high-affinity site that shows a preference for Zn(II) and a second lower affinity site that shows a strong preference for Co(II) . ArgE can also be activated by Mn(II) ions . Two Mn(II) ions bind to ArgE to form a dinuclear site in ArgE .

## Biological Role

Catalyzes N2-acetyl-L-ornithine amidohydrolase (reaction.R00669), N-acetyl-L-citrulline amidohydrolase (reaction.R09107). Component of acetylornithine deacetylase (complex.ecocyc.ACETYLORNDEACET-CPLX).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of the amide bond of N(2)-acetylated L-amino acids. Cleaves the acetyl group from N-acetyl-L-ornithine to form L-ornithine, an intermediate in L-arginine biosynthesis pathway, and a branchpoint in the synthesis of polyamines. {ECO:0000255|HAMAP-Rule:MF_01108, ECO:0000269|PubMed:10684608, ECO:0000269|PubMed:1551850}.

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00669|reaction.R00669]] `KEGG` `database` - via EC:3.5.1.16
- `catalyzes` --> [[reaction.R09107|reaction.R09107]] `KEGG` `database` - via EC:3.5.1.16
- `is_component_of` --> [[complex.ecocyc.ACETYLORNDEACET-CPLX|complex.ecocyc.ACETYLORNDEACET-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3957|gene.b3957]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23908`
- `KEGG:ecj:JW3929;eco:b3957;ecoc:C3026_21385;`
- `GeneID:948456;`
- `GO:GO:0005737; GO:0006526; GO:0008270; GO:0008777; GO:0050897`
- `EC:3.5.1.16`

## Notes

Acetylornithine deacetylase (AO) (Acetylornithinase) (EC 3.5.1.16) (N-acetylornithinase) (NAO)
