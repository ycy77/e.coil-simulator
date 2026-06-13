---
entity_id: "protein.P0A8N5"
entity_type: "protein"
name: "lysU"
source_database: "UniProt"
source_id: "P0A8N5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lysU b4129 JW4090"
---

# lysU

`protein.P0A8N5`

## Static

- Type: `protein`
- Source: `UniProt:P0A8N5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Can also synthesize a number of adenyl dinucleotides (in particular AppppA). These dinucleotides have been proposed to act as modulators of the heat-shock response and stress response. The lysine-tRNA ligase LysU is a member of the family of aminoacyl tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. LysU belongs to the subclass IIB of aminoacyl-tRNA synthetases . E. coli contains both a constitutive (LYSS-MONOMER LysS) and an inducible lysyl-tRNA synthetase; lysU encodes the inducible, more thermostable enzyme . LysU may be more error-prone than LysS . LysU catalyzes misacylation of tRNALys with arginine, threonine, methionine, leucine, alanine, serine, and cysteine, although even the most efficient noncognate substrate, arginine, is used with 1600-fold lower catalytic efficiency than the cognate amino acid lysine . The enzyme does not appear to possess a post-transfer editing mechanism, but it does possess an efficient pre-transfer editing function, discriminating against ornithine, homocysteine, and homoserine by cyclization of the respective adenylates, forming lactams...

## Biological Role

Component of lysine—tRNA ligase (complex.ecocyc.LYSU-CPLX).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

FUNCTION: Can also synthesize a number of adenyl dinucleotides (in particular AppppA). These dinucleotides have been proposed to act as modulators of the heat-shock response and stress response.

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.LYSU-CPLX|complex.ecocyc.LYSU-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4129|gene.b4129]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8N5`
- `KEGG:ecj:JW4090;eco:b4129;ecoc:C3026_22320;`
- `GeneID:86944658;948645;`
- `GO:GO:0000049; GO:0000287; GO:0004824; GO:0005524; GO:0005737; GO:0005829; GO:0006418; GO:0006430; GO:0016020; GO:0016874; GO:0034605; GO:0036260; GO:0042803`
- `EC:6.1.1.6`

## Notes

Lysine--tRNA ligase, heat inducible (EC 6.1.1.6) (Lysyl-tRNA synthetase) (LysRS)
