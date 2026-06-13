---
entity_id: "protein.P17169"
entity_type: "protein"
name: "glmS"
source_database: "UniProt"
source_id: "P17169"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glmS b3729 JW3707"
---

# glmS

`protein.P17169`

## Static

- Type: `protein`
- Source: `UniProt:P17169`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the first step in hexosamine metabolism, converting fructose-6P into glucosamine-6P using glutamine as a nitrogen source. L-glutamine:D-fructose-6-phosphate aminotransferase, or GFAT, catalyzes the first step in hexosamine biosynthesis. The enzyme uses a nucleophilic attack by the thiol group of Cys1 on the δ-carbonyl group of glutamine to form ammonia, which is then channeled through the enzyme to the acceptor group on fructose-6-phosphate. The enzyme can not use exogenous ammonia as the nitrogen donor . The N-terminal domain contains the glutamine amidohydrolase activity, and the C-terminal domain contains the ketose/aldose isomerase activity . Crystal structures of the isolated domains and the full length enzyme have been solved . An 18 Å hydrophobic channel provides a conduit for the transfer of ammonia from the glutamine amidohydrolase active site to the isomerase active site . Molecular dynamics simulations and kinetic analysis of mutants identified roles for W74, A602 and V605 in the opening and closing of the ammonia channel . Major structural changes occur during the catalytic cycle . Mutants of GlmS that show reduced sensitivity to product inhibition by glucosamine-6-phosphate have been isolated . Expression of GlmS is controlled at several levels. glmS mRNA and protein levels are decreased by growth on amino sugars...

## Biological Role

Catalyzes L-glutamine:D-fructose-6-phosphate isomerase (deaminating); (reaction.R00768). Component of L-glutamine—D-fructose-6-phosphate aminotransferase (complex.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-CPLX).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the first step in hexosamine metabolism, converting fructose-6P into glucosamine-6P using glutamine as a nitrogen source.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00768|reaction.R00768]] `KEGG` `database` - via EC:2.6.1.16
- `is_component_of` --> [[complex.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-CPLX|complex.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3729|gene.b3729]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17169`
- `KEGG:ecj:JW3707;eco:b3729;`
- `GeneID:75173963;948241;`
- `GO:GO:0004360; GO:0005829; GO:0005975; GO:0006002; GO:0006047; GO:0006048; GO:0006487; GO:0097367`
- `EC:2.6.1.16`

## Notes

Glutamine--fructose-6-phosphate aminotransferase [isomerizing] (EC 2.6.1.16) (D-fructose-6-phosphate amidotransferase) (GFAT) (Glucosamine-6-phosphate synthase) (Hexosephosphate aminotransferase) (L-glutamine--D-fructose-6-phosphate amidotransferase)
