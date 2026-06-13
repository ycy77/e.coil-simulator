---
entity_id: "protein.P0AG78"
entity_type: "protein"
name: "sbp"
source_database: "UniProt"
source_id: "P0AG78"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sbp b3917 JW3888"
---

# sbp

`protein.P0AG78`

## Static

- Type: `protein`
- Source: `UniProt:P0AG78`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: This protein specifically binds sulfate and is involved in its transmembrane transport. Sbp is a periplasmic sulfate/thiosulfate binding protein; Sbp is one of two periplasmic binding proteins that separately interact with an ABC transporter permease (CysAUW) to mediate high affinity uptake of sulfate and thiosulfate. The predicted amino acid sequence of Sbp from E. coli is 95% identical to the (well characterized) protein from Salmonella typhimurium . Sbp binds sulfate with high affinity (Kd = 0.16 µM) . Double cysP sbp mutants (cysP::Cat sbp::Kan) are cysteine auxotrophs; growth on sulfate (and thiosulfate) as sole sulfur source can be restored in the double mutant by multicopy expression of either cysP or sbp however growth is impaired compared to the wild type strain; CysP and Sbp have overlapping specificity and both are required for wild-type levels of sulfate/thiosulfate transport . Sbp was identified in a set of 'sulfate starvation induced' (SSI) proteins which were induced when cells were grown with sulfur sources (eg.methionine, glutathione, ethanesulfonate) other than sulfate and cysteine . When grown with lanthionine or glutathione as the sulfur source, the level of Sbp is significantly reduced in a G7071 "cbl" null mutant compared to wild type .

## Biological Role

Component of sulfate/thiosulfate ABC transporter (complex.ecocyc.ABC-70-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: This protein specifically binds sulfate and is involved in its transmembrane transport.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-70-CPLX|complex.ecocyc.ABC-70-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3917|gene.b3917]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG78`
- `KEGG:ecj:JW3888;eco:b3917;ecoc:C3026_21175;`
- `GeneID:93777981;948411;`
- `GO:GO:0005615; GO:0006790; GO:0015709; GO:0016020; GO:0030288; GO:0035796; GO:0043199; GO:0140104; GO:1902358`

## Notes

Sulfate-binding protein (Sulfate starvation-induced protein 2) (SSI2)
