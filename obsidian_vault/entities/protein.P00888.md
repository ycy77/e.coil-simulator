---
entity_id: "protein.P00888"
entity_type: "protein"
name: "aroF"
source_database: "UniProt"
source_id: "P00888"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|PROSITE-ProRule:PRU01406}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aroF b2601 JW2582"
---

# aroF

`protein.P00888`

## Static

- Type: `protein`
- Source: `UniProt:P00888`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|PROSITE-ProRule:PRU01406}.

## Enriched Summary

FUNCTION: Stereospecific condensation of phosphoenolpyruvate (PEP) and D-erythrose-4-phosphate (E4P) giving rise to 3-deoxy-D-arabino-heptulosonate-7-phosphate (DAHP). 2-Dehydro-3-deoxyphosphoheptonate aldolase (DAHP synthase) is involved in the first committed step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. DAHP synthase catalyzes an aldol reaction between phosphoenolpyruvate and D-erythrose 4-phosphate to generate 3-deoxy-D-arabino-heptulosonate 7-phosphate (DAHP). There are three isozymes of DAHP synthase, each specifically feedback regulated by tyrosine, phenylalanine or tryptophan . DAHP synthase which is sensitive to tyrosine (DAHP synthase (Tyr), AroF) is encoded by aroF. All three isozymes are metalloenzymes and require a divalent metal for catalysis and/or structural integrity. Different metal ions have been found in DAHP synthase (Tyr) in vivo and in pure preparations . There is a high degree of sequence identity (41%) between the three isozymes and the polypeptides are nearly identical in size . In wild-type cells grown in minimal media, DAHP synthase (Phe) makes up about 80% of the total DAHP synthase activity, DAHP synthase (Tyr) makes up about 20%, and DAHP synthase (Trp) makes up about 1% . Mutations in aroF lead to tyrosine-insensitive DAHP synthase...

## Biological Role

Component of 3-deoxy-7-phosphoheptulonate synthase (complex.ecocyc.AROF-CPLX).

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

- `is_component_of` --> [[complex.ecocyc.AROF-CPLX|complex.ecocyc.AROF-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2601|gene.b2601]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00888`
- `KEGG:ecj:JW2582;eco:b2601;ecoc:C3026_14405;`
- `GeneID:947084;`
- `GO:GO:0003849; GO:0005737; GO:0008652; GO:0009073; GO:0009423; GO:0042802`
- `EC:2.5.1.54`

## Notes

Phospho-2-dehydro-3-deoxyheptonate aldolase, Tyr-sensitive (EC 2.5.1.54) (3-deoxy-D-arabino-heptulosonate 7-phosphate synthase) (DAHP synthase) (Phospho-2-keto-3-deoxyheptonate aldolase)
