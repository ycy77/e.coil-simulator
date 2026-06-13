---
entity_id: "protein.P0AB91"
entity_type: "protein"
name: "aroG"
source_database: "UniProt"
source_id: "P0AB91"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|PROSITE-ProRule:PRU01406}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aroG b0754 JW0737"
---

# aroG

`protein.P0AB91`

## Static

- Type: `protein`
- Source: `UniProt:P0AB91`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|PROSITE-ProRule:PRU01406}.

## Enriched Summary

FUNCTION: Stereospecific condensation of phosphoenolpyruvate (PEP) and D-erythrose-4-phosphate (E4P) giving rise to 3-deoxy-D-arabino-heptulosonate-7-phosphate (DAHP). 2-Dehydro-3-deoxyphosphoheptonate aldolase (DAHP synthase) is involved in the first committed step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. DAHP synthase catalyzes an aldol reaction between phosphoenolpyruvate and D-erythrose 4-phosphate to generate 3-deoxy-D-arabino-heptulosonate 7-phosphate (DAHP). There are three isozymes of DAHP synthase, each specifically feedback regulated by tyrosine, phenylalanine or tryptophan . DAHP synthase which is sensitive to phenylalanine (DAHP synthase (Phe), AroG) is encoded by aroG. All three isozymes are metalloenzymes, and DAHP synthase (Phe) has been shown to contain 1 mol of iron per mol of tetramer . There is a high degree of sequence identity (41%) between the three isozymes and the polypeptides are nearly identical in size . In wild-type cells grown in minimal media, DAHP synthase (Phe) makes up about 80% of the total DAHP synthase activity, DAHP synthase (Tyr) makes up about 20%, and DAHP synthase (Trp) makes up about 1% . Mutations in aroG lead to phenylalanine-insensitive DAHP synthase . Site directed mutagenesis studies of cysteines showed that Cys-61 is essential for catalytic and metal binding...

## Biological Role

Component of 3-deoxy-7-phosphoheptulonate synthase (complex.ecocyc.AROG-CPLX).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Stereospecific condensation of phosphoenolpyruvate (PEP) and D-erythrose-4-phosphate (E4P) giving rise to 3-deoxy-D-arabino-heptulosonate-7-phosphate (DAHP).

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.AROG-CPLX|complex.ecocyc.AROG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0754|gene.b0754]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB91`
- `KEGG:ecj:JW0737;eco:b0754;ecoc:C3026_03815;`
- `GeneID:75170753;945605;`
- `GO:GO:0003849; GO:0005737; GO:0005829; GO:0008652; GO:0009073; GO:0009423; GO:0042802`
- `EC:2.5.1.54`

## Notes

Phospho-2-dehydro-3-deoxyheptonate aldolase, Phe-sensitive (EC 2.5.1.54) (3-deoxy-D-arabino-heptulosonate 7-phosphate synthase) (DAHP synthase) (Phospho-2-keto-3-deoxyheptonate aldolase)
