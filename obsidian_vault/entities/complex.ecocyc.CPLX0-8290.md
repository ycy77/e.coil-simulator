---
entity_id: "complex.ecocyc.CPLX0-8290"
entity_type: "complex"
name: "aminopeptidase YpdF"
source_database: "EcoCyc"
source_id: "CPLX0-8290"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# aminopeptidase YpdF

`complex.ecocyc.CPLX0-8290`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8290`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76524|protein.P76524]]

## Enriched Summary

YpdF is a metalloenzyme with aminopeptidase activity. YpdF can hydrolyze Xaa-Pro bonds when Xaa is Ala, Asn or Met and can hydrolyze amino-terminal Met-Xaa bonds when Xaa is Ala, Pro or Ser . Further investigation of the substrate specificity of YpdF showed higher activity with tripeptides than with dipeptides . It is unable to hydrolyze formylmethionine or acetylmethionine. The YpdF amino-terminus is required for its enzymatic activity . A crystal structure of YpdF has been solved at 2.6 Å resolution . YpdF is a metalloenzyme with aminopeptidase activity. YpdF can hydrolyze Xaa-Pro bonds when Xaa is Ala, Asn or Met and can hydrolyze amino-terminal Met-Xaa bonds when Xaa is Ala, Pro or Ser . Further investigation of the substrate specificity of YpdF showed higher activity with tripeptides than with dipeptides . It is unable to hydrolyze formylmethionine or acetylmethionine. The YpdF amino-terminus is required for its enzymatic activity . A crystal structure of YpdF has been solved at 2.6 Å resolution .

## Biological Role

Catalyzes RXN0-5052 (reaction.ecocyc.RXN0-5052). Bound by Cobalt ion (molecule.C00175), Nickel(2+) (molecule.C19609), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

YpdF is a metalloenzyme with aminopeptidase activity. YpdF can hydrolyze Xaa-Pro bonds when Xaa is Ala, Asn or Met and can hydrolyze amino-terminal Met-Xaa bonds when Xaa is Ala, Pro or Ser . Further investigation of the substrate specificity of YpdF showed higher activity with tripeptides than with dipeptides . It is unable to hydrolyze formylmethionine or acetylmethionine. The YpdF amino-terminus is required for its enzymatic activity . A crystal structure of YpdF has been solved at 2.6 Å resolution .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5052|reaction.ecocyc.RXN0-5052]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P76524|protein.P76524]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8290`
- `QSPROTEOME:QS00188899`

## Notes

2*protein.P76524
