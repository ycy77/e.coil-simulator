---
entity_id: "protein.P0ABU7"
entity_type: "protein"
name: "exbB"
source_database: "UniProt"
source_id: "P0ABU7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "exbB b3006 JW2974"
---

# exbB

`protein.P0ABU7`

## Static

- Type: `protein`
- Source: `UniProt:P0ABU7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Involved in the TonB-dependent energy-dependent transport of various receptor-bound substrates. Protects ExbD from proteolytic degradation and functionally stabilizes TonB. ExbB is a component of the energy transducing Ton system which functions to harness the energy of the proton motive force (pmf) at the cytoplasmic membrane to support active transport of iron-siderophore complexes and certain cofactors across the outer membrane. ExbB affects the stability of TonB and disruption of exbB (exbB::Tn10) results in decreased TonB function . ExbB is an inner membrane protein . ExbB interacts with ExbD and TonB . Topology analysis suggests that ExbB contains three transmembrane (TM) regions with the N-terminus in the periplasm and the C-terminus in the cytoplasm . ExbB forms multimers in vitro and in vivo . A large cytoplasmic loop (residues 40-129) is essential for Ton system function; expression of ExbB proteins with sequential 10-residue deletions in the cytoplasmic loop results in (reversible) growth arrest (that is not due to collapse of the PMF) . ExbB transmembrane domains do not participate in a proton translocation pathway...

## Biological Role

Component of energy transducing Ton complex (complex.ecocyc.CPLX0-1923), cobalamin outer membrane transport complex (complex.ecocyc.CPLX0-1924), ferric enterobactin outer membrane transport complex (complex.ecocyc.CPLX0-1941), ferrichrome outer membrane transport complex (complex.ecocyc.CPLX0-1942), ferric citrate outer membrane transport complex (complex.ecocyc.CPLX0-1943), ferric coprogen outer membrane transport complex (complex.ecocyc.CPLX0-7952), ferric catecholate outer membrane transport complex I (complex.ecocyc.CPLX0-8541), ferric catecholate outer membrane transport complex II (complex.ecocyc.CPLX0-8553), and 1 more.

## Annotation

FUNCTION: Involved in the TonB-dependent energy-dependent transport of various receptor-bound substrates. Protects ExbD from proteolytic degradation and functionally stabilizes TonB.

## Outgoing Edges (9)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=5
- `is_component_of` --> [[complex.ecocyc.CPLX0-1924|complex.ecocyc.CPLX0-1924]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5
- `is_component_of` --> [[complex.ecocyc.CPLX0-1941|complex.ecocyc.CPLX0-1941]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5
- `is_component_of` --> [[complex.ecocyc.CPLX0-1942|complex.ecocyc.CPLX0-1942]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5
- `is_component_of` --> [[complex.ecocyc.CPLX0-1943|complex.ecocyc.CPLX0-1943]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5
- `is_component_of` --> [[complex.ecocyc.CPLX0-7952|complex.ecocyc.CPLX0-7952]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5
- `is_component_of` --> [[complex.ecocyc.CPLX0-8541|complex.ecocyc.CPLX0-8541]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5
- `is_component_of` --> [[complex.ecocyc.CPLX0-8553|complex.ecocyc.CPLX0-8553]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5
- `is_component_of` --> [[complex.ecocyc.CPLX0-9372|complex.ecocyc.CPLX0-9372]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5

## Incoming Edges (1)

- `encodes` <-- [[gene.b3006|gene.b3006]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABU7`
- `KEGG:ecj:JW2974;eco:b3006;ecoc:C3026_16430;`
- `GeneID:86861149;93778981;945420;`
- `GO:GO:0005886; GO:0006879; GO:0009279; GO:0015889; GO:0016020; GO:0017038; GO:0022857; GO:0030003; GO:0031992; GO:0042802; GO:0042928; GO:0043213; GO:0050821; GO:0098797; GO:1902495`

## Notes

Biopolymer transport protein ExbB
