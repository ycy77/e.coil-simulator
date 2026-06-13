---
entity_id: "protein.P06721"
entity_type: "protein"
name: "metC"
source_database: "UniProt"
source_id: "P06721"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metC b3008 JW2975"
---

# metC

`protein.P06721`

## Static

- Type: `protein`
- Source: `UniProt:P06721`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Primarily catalyzes the cleavage of cystathionine to homocysteine, pyruvate and ammonia during methionine biosynthesis (PubMed:7049234). Also exhibits cysteine desulfhydrase activity, producing sulfide from cysteine (PubMed:12883870). In addition, under certain growth conditions, exhibits significant alanine racemase coactivity (PubMed:21193606). {ECO:0000269|PubMed:12883870, ECO:0000269|PubMed:21193606, ECO:0000269|PubMed:7049234}.

## Biological Role

Catalyzes L-cysteine hydrogen-sulfide-lyase (deaminating; pyruvate-forming) (reaction.R00782). Component of cystathionine β-lyase / L-cysteine desulfhydrase / alanine racemase (complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Primarily catalyzes the cleavage of cystathionine to homocysteine, pyruvate and ammonia during methionine biosynthesis (PubMed:7049234). Also exhibits cysteine desulfhydrase activity, producing sulfide from cysteine (PubMed:12883870). In addition, under certain growth conditions, exhibits significant alanine racemase coactivity (PubMed:21193606). {ECO:0000269|PubMed:12883870, ECO:0000269|PubMed:21193606, ECO:0000269|PubMed:7049234}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00782|reaction.R00782]] `KEGG` `database` - via EC:4.4.1.13
- `is_component_of` --> [[complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX|complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3008|gene.b3008]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06721`
- `KEGG:ecj:JW2975;eco:b3008;ecoc:C3026_16440;`
- `GeneID:946240;`
- `GO:GO:0005737; GO:0008784; GO:0009086; GO:0019346; GO:0019450; GO:0030170; GO:0032991; GO:0042802; GO:0047804; GO:0051289; GO:0080146`
- `EC:4.4.1.13; 4.4.1.28`

## Notes

Cystathionine beta-lyase MetC (CBL) (CL) (EC 4.4.1.13) (Beta-cystathionase MetC) (Cysteine desulfhydrase MetC) (CD) (EC 4.4.1.28) (Cysteine lyase MetC) (Cysteine-S-conjugate beta-lyase MetC)
