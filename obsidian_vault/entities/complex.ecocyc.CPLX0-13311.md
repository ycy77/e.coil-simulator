---
entity_id: "complex.ecocyc.CPLX0-13311"
entity_type: "complex"
name: "Mg2+ transporting P-type ATPase"
source_database: "EcoCyc"
source_id: "CPLX0-13311"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Mg2+ transporting P-type ATPase

`complex.ecocyc.CPLX0-13311`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-13311`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ABB8|protein.P0ABB8]]

## Enriched Summary

MgtA is a P-type ATPase that mediates the import of Mg2+ under Mg2+ limiting conditions. Exogenously expressed MgtA is able to support the growth of an Mg2+-auxotrophic E. coli K-12 strain . The well characterised homolog from Salmonella enterica (which has 90% amino acid identity with E. coli MgtA) mediates the influx of both Mg2+ and Ni2+ (see for example and reviews by ). mgtA expression is regulated by the PhoQP two component system; transcription is induced when external Mg2+ is low in a PhoP dependent manner . mgtA expression is also regulated by its leader peptide MgtL in response to Mg2+ levels; MgtL is subject to intrinsic ribosome destabilization - low intracellular Mg2+ levels enhance premature abortion of mgtL translation which enables formation of a secondary structure in the mgtA mRNA leader region that permits mgtA transcription; increasing Mg2+ concentration decreases translation abortion of MgtL and enables formation of a secondary structure that results in transcription termination and loss of mgtA expression . The MgtA leader region and MgtL leader peptide have been extensively characterized in Salmonella enterica (see ).When Mg2+ is limiting, the accumulation of MgtA requires the small membrane protein MONOMER0-766 "MgtS"; MgtA and MgtS copurify in a reciprocal manner...

## Biological Role

Catalyzes TRANS-RXN-250 (reaction.ecocyc.TRANS-RXN-250). Transports Magnesium cation (molecule.C00305), hν (molecule.ecocyc.Light).

## Annotation

MgtA is a P-type ATPase that mediates the import of Mg2+ under Mg2+ limiting conditions. Exogenously expressed MgtA is able to support the growth of an Mg2+-auxotrophic E. coli K-12 strain . The well characterised homolog from Salmonella enterica (which has 90% amino acid identity with E. coli MgtA) mediates the influx of both Mg2+ and Ni2+ (see for example and reviews by ). mgtA expression is regulated by the PhoQP two component system; transcription is induced when external Mg2+ is low in a PhoP dependent manner . mgtA expression is also regulated by its leader peptide MgtL in response to Mg2+ levels; MgtL is subject to intrinsic ribosome destabilization - low intracellular Mg2+ levels enhance premature abortion of mgtL translation which enables formation of a secondary structure in the mgtA mRNA leader region that permits mgtA transcription; increasing Mg2+ concentration decreases translation abortion of MgtL and enables formation of a secondary structure that results in transcription termination and loss of mgtA expression . The MgtA leader region and MgtL leader peptide have been extensively characterized in Salmonella enterica (see ).When Mg2+ is limiting, the accumulation of MgtA requires the small membrane protein MONOMER0-766 "MgtS"; MgtA and MgtS copurify in a reciprocal manner . MgtA interacts specifically with cardiolipin (species 18:1 and 16:0) and this interaction affects the transporter's activity, stability, and localization . MgtA is a type IIIB P-type ATPase . Proteins in the P-type ATPase family contain 4 principal domains: the membrane domain (M-domain); the phosphorylation domain (P-domain) containing the conserved aspartic acid residue (D373 in E. coli MgtA) which is the transient carrier of the ATP γ-phosphate; the nucleotide binding domain (N-dom

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-250|reaction.ecocyc.TRANS-RXN-250]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ABB8|protein.P0ABB8]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-13311`

## Notes

2*protein.P0ABB8
