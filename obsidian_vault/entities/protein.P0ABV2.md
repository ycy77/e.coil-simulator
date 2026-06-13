---
entity_id: "protein.P0ABV2"
entity_type: "protein"
name: "exbD"
source_database: "UniProt"
source_id: "P0ABV2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Single-pass type II membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "exbD b3005 JW2973"
---

# exbD

`protein.P0ABV2`

## Static

- Type: `protein`
- Source: `UniProt:P0ABV2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Single-pass type II membrane protein.

## Enriched Summary

FUNCTION: Involved in the TonB-dependent energy-dependent transport of various receptor-bound substrates. ExbD is a component of the energy transducing Ton system which functions to harness the energy of the proton motive force (pmf) at the cytoplasmic membrane to support active transport of iron-siderophore complexes and certain cofactors across the outer membrane. ExbD is an inner membrane protein ; topology analysis suggests that it contains a single transmembrane region with the N-terminus located in the cytoplasm and a larger C-terminal domain located in the periplasm . ExbD interacts with TonB and with ExbB and forms homodimers in vivo; ExbD and TonB interact through their periplasmic domains; ExbD-TonB interaction requires PMF . ExbD binds to the TonB "D-box" motif and this interaction is suggested to be critical for force transduction between the membranes . Over-expressed ExbBD purifies in multiple stoichiometries; the principle complex, ExbB4ExbD2, contains a TM region expected to consist of 14 TM helices (12 from ExbB and two from ExbD), a periplasmic domain comprised of the ExbD C-terminus and a cytoplasmic domain . Crystallized ExbBExbDΔperi contains a pentamer of ExbB which forms a transmembrane pore that is filled by the transmembrane helix of ExbD (see also ). ExbBD is a heteroheptameric 5:2 rotary motor (see )...

## Biological Role

Component of energy transducing Ton complex (complex.ecocyc.CPLX0-1923), cobalamin outer membrane transport complex (complex.ecocyc.CPLX0-1924), ferric enterobactin outer membrane transport complex (complex.ecocyc.CPLX0-1941), ferrichrome outer membrane transport complex (complex.ecocyc.CPLX0-1942), ferric citrate outer membrane transport complex (complex.ecocyc.CPLX0-1943), ferric coprogen outer membrane transport complex (complex.ecocyc.CPLX0-7952), ferric catecholate outer membrane transport complex I (complex.ecocyc.CPLX0-8541), ferric catecholate outer membrane transport complex II (complex.ecocyc.CPLX0-8553), and 1 more.

## Annotation

FUNCTION: Involved in the TonB-dependent energy-dependent transport of various receptor-bound substrates.

## Outgoing Edges (9)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-1924|complex.ecocyc.CPLX0-1924]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-1941|complex.ecocyc.CPLX0-1941]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-1942|complex.ecocyc.CPLX0-1942]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-1943|complex.ecocyc.CPLX0-1943]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7952|complex.ecocyc.CPLX0-7952]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8541|complex.ecocyc.CPLX0-8541]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8553|complex.ecocyc.CPLX0-8553]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-9372|complex.ecocyc.CPLX0-9372]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3005|gene.b3005]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABV2`
- `KEGG:ecj:JW2973;eco:b3005;ecoc:C3026_16425;`
- `GeneID:93778982;946345;`
- `GO:GO:0005886; GO:0006879; GO:0009279; GO:0015031; GO:0015889; GO:0016020; GO:0022857; GO:0030003; GO:0031992; GO:0042802; GO:0042803; GO:0043213; GO:0050821; GO:0098797; GO:1902495`

## Notes

Biopolymer transport protein ExbD
