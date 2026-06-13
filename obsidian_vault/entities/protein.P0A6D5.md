---
entity_id: "protein.P0A6D5"
entity_type: "protein"
name: "ydiB"
source_database: "UniProt"
source_id: "P0A6D5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydiB b1692 JW1682"
---

# ydiB

`protein.P0A6D5`

## Static

- Type: `protein`
- Source: `UniProt:P0A6D5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The actual biological function of YdiB remains unclear, nor is it known whether 3-dehydroshikimate or quinate represents the natural substrate. Catalyzes the reversible NAD-dependent reduction of both 3-dehydroshikimate (DHSA) and 3-dehydroquinate to yield shikimate (SA) and quinate, respectively. It can use both NAD or NADP for catalysis, however it has higher catalytic efficiency with NAD. {ECO:0000255|HAMAP-Rule:MF_01578, ECO:0000269|PubMed:12624088, ECO:0000269|PubMed:12637497, ECO:0000269|PubMed:15596430}. YdiB was identified as a quinate/shikimate dehydrogenase. The low catalytic efficiency of YdiB with both quinate and shikimate suggests that neither may be the physiological substrate . Wild-type E. coli is not known to synthesize quinate or to use it as a source of carbon. Phylogenomic analysis of the shikimate dehydrogenase family showed that the two enzymes encoded in E. coli, AROE-MONOMER AroE and YdiB, belong to different subclasses; the authors suggested that YdiB was acquired by horizontal gene transfer. Common and subclass-specific catalytic residues and substrate binding motifs were identified . YdiB can use both NAD+ or NADP+ as a cosubstrate for catalysis . Because the intracellular concentration of NAD+ is 40-fold higher than that of NADH+, the dehydrogenase direction is expected to be favored by YdiB in vivo...

## Biological Role

Component of shikimate dehydrogenase / quinate dehydrogenase (complex.ecocyc.CPLX0-7462).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: The actual biological function of YdiB remains unclear, nor is it known whether 3-dehydroshikimate or quinate represents the natural substrate. Catalyzes the reversible NAD-dependent reduction of both 3-dehydroshikimate (DHSA) and 3-dehydroquinate to yield shikimate (SA) and quinate, respectively. It can use both NAD or NADP for catalysis, however it has higher catalytic efficiency with NAD. {ECO:0000255|HAMAP-Rule:MF_01578, ECO:0000269|PubMed:12624088, ECO:0000269|PubMed:12637497, ECO:0000269|PubMed:15596430}.

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7462|complex.ecocyc.CPLX0-7462]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1692|gene.b1692]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6D5`
- `KEGG:ecj:JW1682;eco:b1692;ecoc:C3026_09690;`
- `GeneID:75171755;946200;`
- `GO:GO:0004764; GO:0008652; GO:0009073; GO:0009423; GO:0019632; GO:0030266; GO:0042803; GO:0052733; GO:0052734`
- `EC:1.1.1.282`

## Notes

Quinate/shikimate dehydrogenase (EC 1.1.1.282) (NAD-dependent shikimate 5-dehydrogenase)
