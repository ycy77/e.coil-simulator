---
entity_id: "complex.ecocyc.UVRABC-CPLX"
entity_type: "complex"
name: "excision nuclease UvrABC"
source_database: "EcoCyc"
source_id: "UVRABC-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "excinuclease ABC"
  - "UvrABC excinuclease"
  - "excinuclease UvrABC"
  - "excision nuclease ABC"
  - "UvrABC system excision endonuclease"
  - "ABC excision nuclease"
---

# excision nuclease UvrABC

`complex.ecocyc.UVRABC-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:UVRABC-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A8F8|protein.P0A8F8]], [[protein.P0A8G0|protein.P0A8G0]], [[protein.P0A698|protein.P0A698]]

## Enriched Summary

Nucleotide excision repair (NER) is a generalized DNA repair process which can repair a wide diversity of DNA lesion including UV-induced photoproducts (cyclobutane dimers, 6-4 photoproducts, thymine glycol), bulky adducts, apurininc/apyrimidinic (AP) sites and cross-links. While some of these are also repaired by other pathways, in most cases NER is the major pathway for their repair. The nucleotide excision repair pathway consists of the following steps: recognition of the damaged area; incision 3' and 5' to the damaged area; excision of the lesion-containing oligonucleotide; resynthesis of the excised strand and ligation to form a repaired duplex. The main constituents of the pathway are the products of the genes uvrA, uvrB and uvrC . Recognition of the damaged region is carried out in E. coli by UvrA which has been found to exist as a monomer in the absence of ATP but in the presence of ATP it forms homodimers . The most stable dimer of UvrA contains a mixture of ADP and ATP which is formed upon hydrolysis although other studies have shown that UvrA dimerization is stimulated by ATP binding but not hydrolysis . UvrA contains two ATP binding sites and three other structural motifs-- two zinc fingers and a helix-turn-helix motif, which are thought to be required for the proper recognition of damaged DNA substrate...

## Biological Role

Catalyzes RXN-24977 (reaction.ecocyc.RXN-24977), RXN-24978 (reaction.ecocyc.RXN-24978), RXN0-2621 (reaction.ecocyc.RXN0-2621). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

Nucleotide excision repair (NER) is a generalized DNA repair process which can repair a wide diversity of DNA lesion including UV-induced photoproducts (cyclobutane dimers, 6-4 photoproducts, thymine glycol), bulky adducts, apurininc/apyrimidinic (AP) sites and cross-links. While some of these are also repaired by other pathways, in most cases NER is the major pathway for their repair. The nucleotide excision repair pathway consists of the following steps: recognition of the damaged area; incision 3' and 5' to the damaged area; excision of the lesion-containing oligonucleotide; resynthesis of the excised strand and ligation to form a repaired duplex. The main constituents of the pathway are the products of the genes uvrA, uvrB and uvrC . Recognition of the damaged region is carried out in E. coli by UvrA which has been found to exist as a monomer in the absence of ATP but in the presence of ATP it forms homodimers . The most stable dimer of UvrA contains a mixture of ADP and ATP which is formed upon hydrolysis although other studies have shown that UvrA dimerization is stimulated by ATP binding but not hydrolysis . UvrA contains two ATP binding sites and three other structural motifs-- two zinc fingers and a helix-turn-helix motif, which are thought to be required for the proper recognition of damaged DNA substrate . UvrA binds DNA as a dimer with a strong preference for DNA ends . In vitro studies at physiological concentrations show that UvrA associates with UvrB to form a (UvrA2)UvrB complex in an ATP-dependent interaction . The complex has been shown to have a higher binding affinity for damaged DNA than for undamaged DNA . Purification studies of the complex binding characteristics suggest that the UvrA2B complex tracks along the DNA until a damage site is located.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-24977|reaction.ecocyc.RXN-24977]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24978|reaction.ecocyc.RXN-24978]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-2621|reaction.ecocyc.RXN0-2621]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A698|protein.P0A698]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A8F8|protein.P0A8F8]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A8G0|protein.P0A8G0]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:UVRABC-CPLX`
- `QSPROTEOME:QS00183311`

## Notes

protein.P0A8F8|protein.P0A8G0|protein.P0A698
