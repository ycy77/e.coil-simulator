---
entity_id: "protein.P00887"
entity_type: "protein"
name: "aroH"
source_database: "UniProt"
source_id: "P00887"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|PROSITE-ProRule:PRU01406}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aroH b1704 JW1694"
---

# aroH

`protein.P00887`

## Static

- Type: `protein`
- Source: `UniProt:P00887`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|PROSITE-ProRule:PRU01406}.

## Enriched Summary

FUNCTION: Stereospecific condensation of phosphoenolpyruvate (PEP) and D-erythrose-4-phosphate (E4P) giving rise to 3-deoxy-D-arabino-heptulosonate-7-phosphate (DAHP). 2-Dehydro-3-deoxyphosphoheptonate aldolase (DAHP synthase) is involved in the first committed step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. DAHP synthase catalyzes an aldol reaction between phosphoenolpyruvate and D-erythrose 4-phosphate to generate 3-deoxy-D-arabino-heptulosonate 7-phosphate (DAHP). There are three isozymes of DAHP synthase, each specifically feedback regulated by tyrosine, phenylalanine or tryptophan . DAHP synthase which is sensitive to tryptophan (DAHP synthase (Trp), AroH) is encoded by aroH. All three isozymes are metalloenzymes, and DAHP synthase (Trp) is activated by Fe2+ . There is a high degree of sequence identity (41%) between the three isozymes and the polypeptides are nearly identical in size . In wild-type cells grown in minimal media, DAHP synthase (Phe) makes up about 80% of the total DAHP synthase activity, DAHP synthase (Tyr) makes up about 20%, and DAHP synthase (Trp) makes up about 1% . Mutations in aroH lead to tryptophan-insensitive DAHP synthase . Essential regions for catalytic activity and feedback regulation have been described...

## Biological Role

Component of 3-deoxy-7-phosphoheptulonate synthase (complex.ecocyc.AROH-CPLX).

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

- `is_component_of` --> [[complex.ecocyc.AROH-CPLX|complex.ecocyc.AROH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1704|gene.b1704]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00887`
- `KEGG:ecj:JW1694;eco:b1704;ecoc:C3026_09760;`
- `GeneID:946229;`
- `GO:GO:0003849; GO:0005737; GO:0008652; GO:0009073; GO:0009423; GO:0042802`
- `EC:2.5.1.54`

## Notes

Phospho-2-dehydro-3-deoxyheptonate aldolase, Trp-sensitive (EC 2.5.1.54) (3-deoxy-D-arabino-heptulosonate 7-phosphate synthase) (DAHP synthase) (Phospho-2-keto-3-deoxyheptonate aldolase)
