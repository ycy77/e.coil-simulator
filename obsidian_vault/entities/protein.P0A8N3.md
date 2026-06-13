---
entity_id: "protein.P0A8N3"
entity_type: "protein"
name: "lysS"
source_database: "UniProt"
source_id: "P0A8N3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lysS asuD herC b2890 JW2858"
---

# lysS

`protein.P0A8N3`

## Static

- Type: `protein`
- Source: `UniProt:P0A8N3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Lysine--tRNA ligase (EC 6.1.1.6) (Lysyl-tRNA synthetase) (LysRS) The lysine-tRNA ligase LysS is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. LysS belongs to the subclass IIB of aminoacyl-tRNA synthetases . E. coli contains both a constitutive and an inducible lysyl-tRNA synthetase ; lysS encodes the constitutively expressed enzyme and lysU encodes the inducible . The LYSU-MONOMER LysU enzyme appears to be more error-prone than LysS . The ATP binding site was investigated by affinity labeling . Key residues for recognition of the cognate amino acid and catalytic activity have been identified , providing insight into differences between the class I and class II tRNA synthetases. A model for the recognition specificity of the cognate anticodon is presented . A solution structure of the N-terminal anticodon binding domain has been solved . Specificity determinants within tRNA that are important for recognition by LysS have been identified , and residues within LysS that are important for tRNALys anticodon recognition were analyzed by site-directed mutagenesis . Crystal structures of unliganded and lysine-bound LysS revealed reorganization of the active site upon lysine binding...

## Biological Role

Component of lysine—tRNA ligase, constitutive (complex.ecocyc.LYSS-CPLX).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

Lysine--tRNA ligase (EC 6.1.1.6) (Lysyl-tRNA synthetase) (LysRS)

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.LYSS-CPLX|complex.ecocyc.LYSS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2890|gene.b2890]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8N3`
- `KEGG:ecj:JW2858;eco:b2890;ecoc:C3026_15850;`
- `GeneID:947372;`
- `GO:GO:0000049; GO:0000287; GO:0004824; GO:0005524; GO:0005737; GO:0005829; GO:0006418; GO:0006430; GO:0016020; GO:0016874; GO:0042803`
- `EC:6.1.1.6`

## Notes

Lysine--tRNA ligase (EC 6.1.1.6) (Lysyl-tRNA synthetase) (LysRS)
