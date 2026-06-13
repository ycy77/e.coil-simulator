---
entity_id: "protein.P0AAI3"
entity_type: "protein"
name: "ftsH"
source_database: "UniProt"
source_id: "P0AAI3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01458, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:8444797, ECO:0000269|PubMed:8947034}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01458, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:8444797, ECO:0000269|PubMed:8947034}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ftsH hflB mrsC std tolZ b3178 JW3145"
---

# ftsH

`protein.P0AAI3`

## Static

- Type: `protein`
- Source: `UniProt:P0AAI3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01458, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:8444797, ECO:0000269|PubMed:8947034}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01458, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:8444797, ECO:0000269|PubMed:8947034}.

## Enriched Summary

FUNCTION: Acts as a processive, ATP-dependent zinc metallopeptidase for both cytoplasmic and membrane proteins. Plays a role in the quality control of integral membrane proteins. Degrades a few membrane proteins that have not been assembled into complexes such as SecY, F(0) ATPase subunit a and YccA, and also cytoplasmic proteins sigma-32, LpxC, KdtA and phage lambda cII protein among others. Degrades membrane proteins in a processive manner starting at either the N- or C-terminus; recognition requires a cytoplasmic tail of about 20 residues with no apparent sequence requirements. It presumably dislocates membrane-spanning and periplasmic segments of the protein into the cytoplasm to degrade them, this probably requires ATP. Degrades C-terminal-tagged cytoplasmic proteins which are tagged with an 11-amino-acid nonpolar destabilizing tail via a mechanism involving the 10SA (SsrA) stable RNA.; FUNCTION: As FtsH regulates the levels of both LpxC and KdtA it is required for synthesis of both the protein and lipid components of lipopolysaccharide (LPS). {ECO:0000269|PubMed:18776015}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from E.coli strain 536, E.cloacae strain ATCC 13047 and of Y.pestis strain A across the inner membrane to the cytoplasm, where CdiA has a toxic effect...

## Biological Role

Component of FtsH/HflKC protease complex (complex.ecocyc.CPLX0-2982).

## Annotation

FUNCTION: Acts as a processive, ATP-dependent zinc metallopeptidase for both cytoplasmic and membrane proteins. Plays a role in the quality control of integral membrane proteins. Degrades a few membrane proteins that have not been assembled into complexes such as SecY, F(0) ATPase subunit a and YccA, and also cytoplasmic proteins sigma-32, LpxC, KdtA and phage lambda cII protein among others. Degrades membrane proteins in a processive manner starting at either the N- or C-terminus; recognition requires a cytoplasmic tail of about 20 residues with no apparent sequence requirements. It presumably dislocates membrane-spanning and periplasmic segments of the protein into the cytoplasm to degrade them, this probably requires ATP. Degrades C-terminal-tagged cytoplasmic proteins which are tagged with an 11-amino-acid nonpolar destabilizing tail via a mechanism involving the 10SA (SsrA) stable RNA.; FUNCTION: As FtsH regulates the levels of both LpxC and KdtA it is required for synthesis of both the protein and lipid components of lipopolysaccharide (LPS). {ECO:0000269|PubMed:18776015}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from E.coli strain 536, E.cloacae strain ATCC 13047 and of Y.pestis strain A across the inner membrane to the cytoplasm, where CdiA has a toxic effect. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins. {ECO:0000269|PubMed:26305955}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2982|complex.ecocyc.CPLX0-2982]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3178|gene.b3178]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAI3`
- `KEGG:ecj:JW3145;eco:b3178;ecoc:C3026_17305;`
- `GeneID:93778803;947690;`
- `GO:GO:0004176; GO:0004222; GO:0005524; GO:0005886; GO:0006508; GO:0008270; GO:0016887; GO:0030163; GO:0098796; GO:0098797`
- `EC:3.4.24.-`

## Notes

ATP-dependent zinc metalloprotease FtsH (EC 3.4.24.-) (Cell division protease FtsH)
