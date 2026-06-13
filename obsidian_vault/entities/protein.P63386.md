---
entity_id: "protein.P63386"
entity_type: "protein"
name: "mlaF"
source_database: "UniProt"
source_id: "P63386"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:19383799}; Peripheral membrane protein {ECO:0000305|PubMed:19383799}; Cytoplasmic side {ECO:0000305|PubMed:19383799}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mlaF yrbF b3195 JW3162"
---

# mlaF

`protein.P63386`

## Static

- Type: `protein`
- Source: `UniProt:P63386`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:19383799}; Peripheral membrane protein {ECO:0000305|PubMed:19383799}; Cytoplasmic side {ECO:0000305|PubMed:19383799}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex MlaFEDB, which is involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:19383799, ECO:0000269|PubMed:27529189}. mlaF encodes the ATP-binding protein of an inner membrane complex (MlaFEDB) which functions as part of a retrograde and/or anterograde intermembrane phospholipid trafficking system. MlaF contains signature motifs conserved in ATP-binding cassette (ABC) proteins . MlaF is implicated in a retrograde phospholipid trafficking pathway; a ΔmlaF mutant displays increased SDS-EDTA sensitivity (also ). MlaF forms a stable complex with MlaE, MlaD and MlaB; an MlaFEB complex containing an MlaF variant (MlaFK47R) has no intrinsic ATPase activity in vitro . Purified, recombinant MlaFB (co-expressed from a single transcript) forms a complex with 1:1 stoichiometry and structures of both MlaF1B1 - the inactive 'half-transporter' - and MlaF2B2 - the fully assembled complex - have been solved . In the MlaFEDB cryo-EM structures determined by , dimeric MlaF in the cytoplasm associates with the auxiliary MlaB subunits and the MlaE transmembrane core (see also ). mla: maintenance of outer membrane lipid asymmetry

## Biological Role

Component of intermembrane phospholipid transport system (complex.ecocyc.ABC-45-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex MlaFEDB, which is involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:19383799, ECO:0000269|PubMed:27529189}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-45-CPLX|complex.ecocyc.ABC-45-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3195|gene.b3195]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P63386`
- `KEGG:ecj:JW3162;eco:b3195;`
- `GeneID:86862408;93778786;947729;`
- `GO:GO:0005524; GO:0005886; GO:0015914; GO:0016020; GO:0016887; GO:0120010; GO:0120014; GO:1990531`
- `EC:7.6.2.-`

## Notes

Intermembrane phospholipid transport system ATP-binding protein MlaF (EC 7.6.2.-)
