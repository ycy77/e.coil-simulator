---
entity_id: "protein.P38683"
entity_type: "protein"
name: "torT"
source_database: "UniProt"
source_id: "P38683"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "torT yccH b0994 JW0979"
---

# torT

`protein.P38683`

## Static

- Type: `protein`
- Source: `UniProt:P38683`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Upon binding a putative inducer it probably interacts with TorS and allows it to play a role in the induction of the torCAD operon for trimethylamine N-oxide reductase. TorT is a periplasmic trimethylamine-N-oxide (TMAO) binding protein that forms part of the PWY0-1506 "TorTS-TorR signaling system" which regulates expression of the torCAD operon for TMAO-based respiration. torT encodes a periplasmic protein which is required for expression of the torCAD operon; disruption of torT results in significantly reduced expression of a torA'-'lacZ fusion and loss of inducible TMAO reductase activity; overproduction of the TorR response regulator can partially bypass the requirement for TorT . TorT is dispensable in a torS constitutive mutant . TorT binds TMAO with µM affinity (KD = 150 µM); TorT becomes resistant to proteolytic digestion in the presence of TMAO; both TorT alone and TorT-TMAO interact with the periplasmic domain of the two-component sensor protein TORS-CPLX "TorS"; TMAO binding may induce a cascade of conformational change from TorT to TorS . TorT-TorS complexes, in both apo and TMAO bound states, have been characterized from Vibrio parahaemolyticus; in both this species and E. coli TorT-TorS complexes are likely the physiologically relevant form of signaling complex whether TMAO is present or not...

## Biological Role

Component of TorTS signaling complex (complex.ecocyc.CPLX0-11302).

## Annotation

FUNCTION: Upon binding a putative inducer it probably interacts with TorS and allows it to play a role in the induction of the torCAD operon for trimethylamine N-oxide reductase.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-11302|complex.ecocyc.CPLX0-11302]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0994|gene.b0994]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P38683`
- `KEGG:ecj:JW0979;eco:b0994;ecoc:C3026_06060;`
- `GeneID:946289;`
- `GO:GO:0000976; GO:0003700; GO:0006355; GO:0009061; GO:0042597`

## Notes

Periplasmic protein TorT
