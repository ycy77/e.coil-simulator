---
entity_id: "protein.P00926"
entity_type: "protein"
name: "dsdA"
source_database: "UniProt"
source_id: "P00926"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dsdA b2366 JW2363"
---

# dsdA

`protein.P00926`

## Static

- Type: `protein`
- Source: `UniProt:P00926`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

D-serine dehydratase (EC 4.3.1.18) (D-serine deaminase) (DSD) It was established long ago that E. coli is able to deaminate serine and that the activity is inducible by D-serine . D-serine ammonia-lyase (DsdA) catalyzes the deamination of D-serine to form pyruvate and ammonia. D-serine has a bacteriostatic effect on E. coli; thus, when D-serine is present, detoxification is necessary for cell growth . Once the cell expresses DsdA, D-serine can be utilized as the sole source of carbon and nitrogen . Toxicity of D-serine in minimal medium appears to be due to an effect on biosynthesis of L-serine and pantothenate . The cofactor requirements and reaction mechanism of the enzyme have been investigated. Binding of the pyridoxal phosphate (PLP) cofactor has been studied in detail . The reaction involves a transient Schiff base intermediate of α-aminoacrylate and PLP . The G279D and G281D mutations eliminate enzyme activity due to altered interactions with PLP . More conservative substitutions at G278, G279, and G281 result in reduced or altered enzymatic activity . Crystal structures of the enzyme have been solved, confirming results from the analysis of mutant enzymes, and leading to the proposal of a catalytic mechanism . Regulation of DsdA expression has been extensively investigated and was shown to involve positive regulation by DsdC and cAMP-CRP...

## Biological Role

Catalyzes D-serine ammonia-lyase (reaction.R00221), DSERDEAM-RXN (reaction.ecocyc.DSERDEAM-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

D-serine dehydratase (EC 4.3.1.18) (D-serine deaminase) (DSD)

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00221|reaction.R00221]] `KEGG` `database` - via EC:4.3.1.18
- `catalyzes` --> [[reaction.ecocyc.DSERDEAM-RXN|reaction.ecocyc.DSERDEAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2366|gene.b2366]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00926`
- `KEGG:ecj:JW2363;eco:b2366;ecoc:C3026_13160;`
- `GeneID:946837;`
- `GO:GO:0005737; GO:0005829; GO:0006974; GO:0008721; GO:0016836; GO:0030170; GO:0036088; GO:0051410; GO:0070178`
- `EC:4.3.1.18`

## Notes

D-serine dehydratase (EC 4.3.1.18) (D-serine deaminase) (DSD)
