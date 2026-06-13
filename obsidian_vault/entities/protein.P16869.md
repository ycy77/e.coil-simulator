---
entity_id: "protein.P16869"
entity_type: "protein"
name: "fhuE"
source_database: "UniProt"
source_id: "P16869"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|PROSITE-ProRule:PRU01360, ECO:0000305|PubMed:31098021}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU01360}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fhuE b1102 JW1088"
---

# fhuE

`protein.P16869`

## Static

- Type: `protein`
- Source: `UniProt:P16869`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|PROSITE-ProRule:PRU01360, ECO:0000305|PubMed:31098021}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU01360}.

## Enriched Summary

FUNCTION: Involved in the active transport across the outer membrane of iron complexed with linear hydroxamate siderophores coprogen, rhodotorulic acid and ferrioxamine B. Binds Fe-coprogen with high affinity, rhodotorulic acid to a lesser extent, and weakly to ferrioxamine B. Selective for planar siderophores. Does not use cyclic siderophores ferrichrome nor ferrioxamine E as substrates. {ECO:0000269|PubMed:31098021}. FhuE is a protein which serves as a receptor for ferric-coprogen (a hydroxamate-type iron chelator) and ferric-rhodotorulic acid . Uptake into the periplasm is facilitated by TonB coupling of inner membrane energy to power specific uptake across the outer membrane . Coprogen iron uptake is dependent on tonB, exbB and fhuCDB . FhuE appears to have a preference for Δ-absolute configuration metal complexes . In the Transporter Classification Database FhuE is a member of the Outer Membrane Receptor (OMR) family

## Biological Role

Component of ferric coprogen outer membrane transport complex (complex.ecocyc.CPLX0-7952).

## Annotation

FUNCTION: Involved in the active transport across the outer membrane of iron complexed with linear hydroxamate siderophores coprogen, rhodotorulic acid and ferrioxamine B. Binds Fe-coprogen with high affinity, rhodotorulic acid to a lesser extent, and weakly to ferrioxamine B. Selective for planar siderophores. Does not use cyclic siderophores ferrichrome nor ferrioxamine E as substrates. {ECO:0000269|PubMed:31098021}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7952|complex.ecocyc.CPLX0-7952]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1102|gene.b1102]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16869`
- `KEGG:ecj:JW1088;eco:b1102;ecoc:C3026_06655;`
- `GeneID:945649;`
- `GO:GO:0006879; GO:0009279; GO:0015092; GO:0015343; GO:0015344; GO:0015687; GO:0016020; GO:0033214; GO:0038023; GO:0044718; GO:0072711; GO:1902495`

## Notes

Hydroxamate siderophore receptor FhuE (Ferric iron uptake protein) (Ferric-coprogen receptor FhuE) (Outer-membrane receptor for Fe(III)-coprogen, Fe(III)-ferrioxamine B and Fe(III)-rhodotrulic acid) (TonB-dependent transporter receptor FhuE) (TBDT receptor FhuE)
