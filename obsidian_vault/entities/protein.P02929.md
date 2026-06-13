---
entity_id: "protein.P02929"
entity_type: "protein"
name: "tonB"
source_database: "UniProt"
source_id: "P02929"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Single-pass membrane protein; Periplasmic side."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tonB exbA b1252 JW5195"
---

# tonB

`protein.P02929`

## Static

- Type: `protein`
- Source: `UniProt:P02929`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Single-pass membrane protein; Periplasmic side.

## Enriched Summary

FUNCTION: Interacts with outer membrane receptor proteins that carry out high-affinity binding and energy dependent uptake into the periplasmic space of specific substrates such as cobalamin, and various iron compounds (such as iron dicitrate, enterochelin, aerobactin, etc.). In the absence of TonB these receptors bind their substrates but do not carry out active transport. TonB also interacts with some colicins and is involved in the energy-dependent, irreversible steps of bacteriophages phi 80 and T1 infection. It could act to transduce energy from the cytoplasmic membrane to specific energy-requiring processes in the outer membrane, resulting in the release into the periplasm of ligands bound by these outer membrane proteins. Implicated in hydroxy radical-mediated cell death induced by hydroxyurea treatment (PubMed:20005847). {ECO:0000269|PubMed:20005847}. TonB is a component of the energy transducing Ton system which functions to harness the energy of the proton motive force (pmf) at the cytoplasmic membrane to support active transport of iron-siderophore complexes and vitamin B12 across the outer membrane...

## Biological Role

Component of energy transducing Ton complex (complex.ecocyc.CPLX0-1923), cobalamin outer membrane transport complex (complex.ecocyc.CPLX0-1924), ferric enterobactin outer membrane transport complex (complex.ecocyc.CPLX0-1941), ferrichrome outer membrane transport complex (complex.ecocyc.CPLX0-1942), ferric citrate outer membrane transport complex (complex.ecocyc.CPLX0-1943), ferric coprogen outer membrane transport complex (complex.ecocyc.CPLX0-7952), ferric catecholate outer membrane transport complex I (complex.ecocyc.CPLX0-8541), ferric catecholate outer membrane transport complex II (complex.ecocyc.CPLX0-8553), and 1 more.

## Annotation

FUNCTION: Interacts with outer membrane receptor proteins that carry out high-affinity binding and energy dependent uptake into the periplasmic space of specific substrates such as cobalamin, and various iron compounds (such as iron dicitrate, enterochelin, aerobactin, etc.). In the absence of TonB these receptors bind their substrates but do not carry out active transport. TonB also interacts with some colicins and is involved in the energy-dependent, irreversible steps of bacteriophages phi 80 and T1 infection. It could act to transduce energy from the cytoplasmic membrane to specific energy-requiring processes in the outer membrane, resulting in the release into the periplasm of ligands bound by these outer membrane proteins. Implicated in hydroxy radical-mediated cell death induced by hydroxyurea treatment (PubMed:20005847). {ECO:0000269|PubMed:20005847}.

## Outgoing Edges (9)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]] `EcoCyc` `database` - EcoCyc component coefficient=5 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-1924|complex.ecocyc.CPLX0-1924]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-1941|complex.ecocyc.CPLX0-1941]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-1942|complex.ecocyc.CPLX0-1942]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-1943|complex.ecocyc.CPLX0-1943]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-7952|complex.ecocyc.CPLX0-7952]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8541|complex.ecocyc.CPLX0-8541]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8553|complex.ecocyc.CPLX0-8553]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-9372|complex.ecocyc.CPLX0-9372]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1252|gene.b1252]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02929`
- `KEGG:ecj:JW5195;eco:b1252;ecoc:C3026_07355;`
- `GeneID:945843;`
- `GO:GO:0005886; GO:0006879; GO:0009279; GO:0015031; GO:0015889; GO:0015891; GO:0016020; GO:0019904; GO:0030003; GO:0030288; GO:0030313; GO:0031992; GO:0042914; GO:0055085; GO:0098002; GO:0098797; GO:1902495`

## Notes

Protein TonB
