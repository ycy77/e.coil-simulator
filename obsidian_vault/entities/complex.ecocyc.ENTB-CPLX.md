---
entity_id: "complex.ecocyc.ENTB-CPLX"
entity_type: "complex"
name: "holo-EntB dimer"
source_database: "EcoCyc"
source_id: "ENTB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "holo-EntB"
---

# holo-EntB dimer

`complex.ecocyc.ENTB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ENTB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ADI4|protein.P0ADI4]]

## Enriched Summary

The EntB protein is bifunctional, the N-terminal domain contains the isochorismate lyase (isochorismatase) activity and the C-terminus contains the aryl carrier protein (ArCP) domain. The isochorismatase activity of the entB gene product catalyzes the second step in both the overall enterobactin biosynthetic pathway (see pathway ENTBACSYN-PWY) and in the first part of the pathway, the conversion of chorismate to 2,3-dihydroxybenzoate (see pathway PWY-5901) . The ArCP domain of apo-EntB becomes phosphopantetheinylated in a reaction catalyzed by the entD gene product, ENTD-MONOMER. The ENTB-CPLX (holo-EntB) formed can now serve as a substrate for the entE product, a ENTE-CPLX that activates 2,3-dihydroxybenzoate as the acyl-AMP derivative and transfers the acyl moiety onto holo-EntB. The arylated holo-EntB product (CPLX0-7849) then serves as the aryl donor for the amide bond formation in enterobactin assembly . The crystal structure of this two domain protein has been determined at 2.3 Å resolution. Its two functionally independent domains are joined by a proline-rich linker. Functional analysis of EntB and EntE mutants probed the interaction between these two proteins . Based on gel filtration data, EntB was originally suggested to be a pentamer and later suggested to be a trimer . However subsequent gel filtration and crystallographic data showed it to be a dimer...

## Biological Role

Catalyzes ISOCHORMAT-RXN (reaction.ecocyc.ISOCHORMAT-RXN). Component of enterobactin synthase (complex.ecocyc.ENTMULTI-CPLX).

## Annotation

The EntB protein is bifunctional, the N-terminal domain contains the isochorismate lyase (isochorismatase) activity and the C-terminus contains the aryl carrier protein (ArCP) domain. The isochorismatase activity of the entB gene product catalyzes the second step in both the overall enterobactin biosynthetic pathway (see pathway ENTBACSYN-PWY) and in the first part of the pathway, the conversion of chorismate to 2,3-dihydroxybenzoate (see pathway PWY-5901) . The ArCP domain of apo-EntB becomes phosphopantetheinylated in a reaction catalyzed by the entD gene product, ENTD-MONOMER. The ENTB-CPLX (holo-EntB) formed can now serve as a substrate for the entE product, a ENTE-CPLX that activates 2,3-dihydroxybenzoate as the acyl-AMP derivative and transfers the acyl moiety onto holo-EntB. The arylated holo-EntB product (CPLX0-7849) then serves as the aryl donor for the amide bond formation in enterobactin assembly . The crystal structure of this two domain protein has been determined at 2.3 Å resolution. Its two functionally independent domains are joined by a proline-rich linker. Functional analysis of EntB and EntE mutants probed the interaction between these two proteins . Based on gel filtration data, EntB was originally suggested to be a pentamer and later suggested to be a trimer . However subsequent gel filtration and crystallographic data showed it to be a dimer . Cell lysis and fractionation studies have led to the proposal that a large fraction of the Ent synthase proteins EntB, EntE and EntF is in contact with membranes, or in close proximity to membranes . A biophysical study of EntE substrate binding and the interaction between EntE and EntB showed that complex formation is most efficient in the presence of 2,3-dihydroxybenzoate . The thioesterase EntH has been pr

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ISOCHORMAT-RXN|reaction.ecocyc.ISOCHORMAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.ENTMULTI-CPLX|complex.ecocyc.ENTMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ADI4|protein.P0ADI4]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ENTB-CPLX`
- `QSPROTEOME:QS00147911`

## Notes

2*protein.P0ADI4
