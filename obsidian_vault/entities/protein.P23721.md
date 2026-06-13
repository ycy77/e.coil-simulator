---
entity_id: "protein.P23721"
entity_type: "protein"
name: "serC"
source_database: "UniProt"
source_id: "P23721"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "serC pdxC pdxF b0907 JW0890"
---

# serC

`protein.P23721`

## Static

- Type: `protein`
- Source: `UniProt:P23721`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the reversible conversion of 3-phosphohydroxypyruvate to phosphoserine and of 3-hydroxy-2-oxo-4-phosphonooxybutanoate to phosphohydroxythreonine. Is involved in both pyridoxine and serine biosynthesis. {ECO:0000269|PubMed:2121717, ECO:0000269|PubMed:8706854}. The serC-encoded enzyme, phosphoserine/phosphohydroxythreonine aminotransferase, functions in the biosythesis of both serine and pyridoxine, by using different substrates . Pyridoxal 5'-phosphate is a cofactor for both enzyme activities, suggesting that it can act in an autocatalytic fashion, stimulating its own biosynthesis . The redundancy and promiscuity among aminotransferase enzymes has been investigated. stated that no activity could be observed with non-phosphorylated substrates; however, was able to use 3-hydroxypyruvate as the substrate for an assay of SerC enzymatic activity. In addition, genetic experiments showed that SerC is a minor alanine transaminase . The normal activities of two enzymes, ArgD and SerC, are sufficient for succinyldiaminopimelate (SDAP) and lysine biosynthesis; a third enzyme, AstC, is sufficient for SDAP biosynthesis, but alone can not fulfill the cell's requirement for lysine. Additional enzymes, including GabT and PuuE, may be able to contribute to SDAP biosynthesis...

## Biological Role

Component of phosphoserine/phosphohydroxythreonine aminotransferase (complex.ecocyc.PSERTRANSAM-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible conversion of 3-phosphohydroxypyruvate to phosphoserine and of 3-hydroxy-2-oxo-4-phosphonooxybutanoate to phosphohydroxythreonine. Is involved in both pyridoxine and serine biosynthesis. {ECO:0000269|PubMed:2121717, ECO:0000269|PubMed:8706854}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PSERTRANSAM-CPLX|complex.ecocyc.PSERTRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0907|gene.b0907]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23721`
- `KEGG:ecj:JW0890;eco:b0907;ecoc:C3026_05595;`
- `GeneID:945527;`
- `GO:GO:0004648; GO:0005737; GO:0005829; GO:0006563; GO:0006564; GO:0008615; GO:0030170; GO:0033359; GO:0042803; GO:0042823`
- `EC:2.6.1.52`

## Notes

Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine aminotransferase) (PSAT)
