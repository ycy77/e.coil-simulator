---
entity_id: "complex.ecocyc.ENTE-CPLX"
entity_type: "complex"
name: "2,3-dihydroxybenzoate-[aryl-carrier protein] ligase"
source_database: "EcoCyc"
source_id: "ENTE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN|CCO-MEMBRANE"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "enterobactin synthetase component E"
  - "enterochelin synthase E"
  - "enterobactin synthase component E"
---

# 2,3-dihydroxybenzoate-[aryl-carrier protein] ligase

`complex.ecocyc.ENTE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ENTE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN|CCO-MEMBRANE
- Complex type: `structural`
- Components: [[protein.P10378|protein.P10378]]

## Enriched Summary

EntE is an enzyme of the ENTBACSYN-PWY pathway that catalyzes the ATP-dependent condensation of 2,3-dihydroxybenzoate (DHB) and ENTB-CPLX (holo-EntB) to form the covalently arylated form of EntB, CPLX0-7849. EntE activity has been characterized as a two-step adenylation-ligation reaction. In the first step it catalyzes the condensation of DHB with ATP to form the adenylate intermediate 2,3-dihydroxybenzoyl-AMP. In the second step DHB is ligated onto the phosphopantetheinyl cofactor of holo-entB to form aryl-entB . Initial studies showed that EntE is a 2,3-dihydroxybenzoate-AMP ligase, and kinetic data suggested that the (2,3-dihydroxybenzoyl)adenylate intermediate remains bound to the enzyme . Later, EntE was found to catalyze a second half-reaction, transfer of the aryl fragment, 2,3-dihydroxybenzoate, via a thioester linkage to the phosphopantetheinyl moiety of ENTB-CPLX "holo-EntB" . The kinetic mechanism has been studied in detail, suggesting a bi-uni-uni-b ping pong mechanism . The adenylation activity of EntE is specific for holo-EntB . The interaction between EntE and holo-EntB is remarkably tolerant to point mutations in the predicted interaction surface of EntB and is most efficient in the presence of DHB...

## Biological Role

Catalyzes RXN-19445 (reaction.ecocyc.RXN-19445), RXN0-5208 (reaction.ecocyc.RXN0-5208). Component of enterobactin synthase (complex.ecocyc.ENTMULTI-CPLX). Bound by Magnesium cation (molecule.C00305).

## Annotation

EntE is an enzyme of the ENTBACSYN-PWY pathway that catalyzes the ATP-dependent condensation of 2,3-dihydroxybenzoate (DHB) and ENTB-CPLX (holo-EntB) to form the covalently arylated form of EntB, CPLX0-7849. EntE activity has been characterized as a two-step adenylation-ligation reaction. In the first step it catalyzes the condensation of DHB with ATP to form the adenylate intermediate 2,3-dihydroxybenzoyl-AMP. In the second step DHB is ligated onto the phosphopantetheinyl cofactor of holo-entB to form aryl-entB . Initial studies showed that EntE is a 2,3-dihydroxybenzoate-AMP ligase, and kinetic data suggested that the (2,3-dihydroxybenzoyl)adenylate intermediate remains bound to the enzyme . Later, EntE was found to catalyze a second half-reaction, transfer of the aryl fragment, 2,3-dihydroxybenzoate, via a thioester linkage to the phosphopantetheinyl moiety of ENTB-CPLX "holo-EntB" . The kinetic mechanism has been studied in detail, suggesting a bi-uni-uni-b ping pong mechanism . The adenylation activity of EntE is specific for holo-EntB . The interaction between EntE and holo-EntB is remarkably tolerant to point mutations in the predicted interaction surface of EntB and is most efficient in the presence of DHB . In the absence of holo-EntB, EntE can transfer the adenylate moiety of the (2,3-dihydroxybenzoyl)adenylate intermediate to ATP, generating the stress signaling molecule Ap4A and releasing 2,3-dihydroxybenzoate . Enhancement of the DHB-AMP ligase activity of EntE by interaction with the DHB-producing enzyme EntA has been demonstrated . EntE can be released from the cell by osmotic shock, but not by formation of spheroplasts; it was therefore suggested that the enzyme is membrane-associated . Subsequent cell lysis and fractionation studies have led to the prop

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-19445|reaction.ecocyc.RXN-19445]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5208|reaction.ecocyc.RXN0-5208]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.ENTMULTI-CPLX|complex.ecocyc.ENTMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P10378|protein.P10378]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ENTE-CPLX`
- `QSPROTEOME:QS00188699`

## Notes

2*protein.P10378
