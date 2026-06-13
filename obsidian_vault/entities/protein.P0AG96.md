---
entity_id: "protein.P0AG96"
entity_type: "protein"
name: "secE"
source_database: "UniProt"
source_id: "P0AG96"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00422, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00422, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "secE prlG b3981 JW3944"
---

# secE

`protein.P0AG96`

## Static

- Type: `protein`
- Source: `UniProt:P0AG96`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00422, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00422, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Essential subunit of the protein translocation channel SecYEG. Clamps together the 2 halves of SecY. May contact the channel plug during translocation. Overexpression of some hybrid proteins has been thought to jam the protein secretion apparatus resulting in cell death; while this may be true it also results in FtsH-mediated degradation of SecY. {ECO:0000269|PubMed:15140892}. The SecE inner membrane protein is a component of the heterotrimeric SecYEG preprotein translocase. SecY, SecE and SecG form a stable complex which supports precursor protein translocation in vitro . A cold sensitive SecE mutant (SecEcsE501) accumulates the precursor form of periplasmic and envelope proteins (MBP, LamB and RBP) when grown at the non-permissive temperature ; the SecEcsE501 allele is an alteration to the concensus ribosome binding site that results in decreased expression of secE . SecE is an inner membrane protein with three predicted transmembrane regions . SecE is essential for growth; a truncated SecE (secEΔ7-78) functions effectively in vivo . prl alleles of secE which suppress a variety of signal sequence mutations have been characterized . Overexpression of secE stabilizes over-expressed SecY in vivo...

## Biological Role

Component of SecYEG-SecA complex (complex.ecocyc.CPLX0-12269), Sec Holo-Translocon (complex.ecocyc.SEC-SECRETION-CPLX), SecYEG translocon (complex.ecocyc.SECE-G-Y-CPLX).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Essential subunit of the protein translocation channel SecYEG. Clamps together the 2 halves of SecY. May contact the channel plug during translocation. Overexpression of some hybrid proteins has been thought to jam the protein secretion apparatus resulting in cell death; while this may be true it also results in FtsH-mediated degradation of SecY. {ECO:0000269|PubMed:15140892}.

## Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12269|complex.ecocyc.CPLX0-12269]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.SEC-SECRETION-CPLX|complex.ecocyc.SEC-SECRETION-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.SECE-G-Y-CPLX|complex.ecocyc.SECE-G-Y-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3981|gene.b3981]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG96`
- `KEGG:ecj:JW3944;eco:b3981;ecoc:C3026_21505;`
- `GeneID:86861618;93777913;948486;`
- `GO:GO:0005886; GO:0006616; GO:0006886; GO:0008320; GO:0009306; GO:0016020; GO:0031522; GO:0043952; GO:0065002`

## Notes

Protein translocase subunit SecE
