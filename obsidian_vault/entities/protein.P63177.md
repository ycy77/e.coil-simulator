---
entity_id: "protein.P63177"
entity_type: "protein"
name: "rlmB"
source_database: "UniProt"
source_id: "P63177"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlmB yjfH b4180 JW4138"
---

# rlmB

`protein.P63177`

## Static

- Type: `protein`
- Source: `UniProt:P63177`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically methylates the ribose of guanosine 2251 in 23S rRNA. {ECO:0000269|PubMed:11698387}. RlmB is the methyltransferase responsible for methylation of 23S rRNA at the 2'-O position of the ribose at the G2251 nucleotide . RlmB is a 2'O-methyltransferase that belongs to the SPOUT superfamily . A crystal structure of RlmB has been solved at 2.5 Å resolution. The N terminus is implicated in rRNA recognition, and the C-terminal domain contains a deep knot structure that encompasses the predicted SAM binding site . Computational docking analysis of the SAM binding site allowed inference of functionally important residues and a reaction mechanism . An rlmB deletion mutant does not show growth defects or defects in ribosome maturation . Ribosomal RNA in a ΔrlmB mutant was more susceptible to reactive oxygen species (ROS) and UVA damage than wild-type...

## Biological Role

Component of 23S rRNA 2'-O-ribose G2251 methyltransferase (complex.ecocyc.CPLX0-1121).

## Annotation

FUNCTION: Specifically methylates the ribose of guanosine 2251 in 23S rRNA. {ECO:0000269|PubMed:11698387}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1121|complex.ecocyc.CPLX0-1121]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4180|gene.b4180]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P63177`
- `KEGG:ecj:JW4138;eco:b4180;ecoc:C3026_22585;`
- `GeneID:93777641;948694;`
- `GO:GO:0003723; GO:0005829; GO:0006364; GO:0070039`
- `EC:2.1.1.185`

## Notes

23S rRNA (guanosine-2'-O-)-methyltransferase RlmB (EC 2.1.1.185) (23S rRNA (guanosine2251 2'-O)-methyltransferase) (23S rRNA Gm2251 2'-O-methyltransferase)
