---
entity_id: "complex.ecocyc.CPLX0-2081"
entity_type: "complex"
name: "dihydroxyacetone kinase"
source_database: "EcoCyc"
source_id: "CPLX0-2081"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "DHAK"
  - "DHA kinase"
---

# dihydroxyacetone kinase

`complex.ecocyc.CPLX0-2081`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2081`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P76015|protein.P76015]], [[protein.P76014|protein.P76014]], [[complex.ecocyc.CPLX0-8206|complex.ecocyc.CPLX0-8206]]

## Enriched Summary

Dihydroxyacetone (DHA) can serve as the sole source of carbon and energy for E. coli K-12, but only in a low phosphate environment (possibly due to the buildup of methylglyoxal) . Dihydroxyacetone kinase is an unusal enzyme that functions similarly to a phosphotransferase system (PTS) in that it utilizes phosphoenolpyruvate as a phosphate donor. However, the enzyme is cytoplasmic and is not involved in transmembrane transport . The phosphorylation reaction requires the presence of the PTSI-MONOMER EI and PTSH-MONOMER HPr proteins of the PTS system to phosphorylate the DhaM protein . DhaM then transfers the phosphate group to the ADP cofactor of DhaL, which in turn transfers it to dihydroxyacetone that is bound to the DhaK subunit . A mechanism for the phosphotransferase reaction has been proposed . DhaK and DhaL form a complex consisting of a central DhaK dimer and two subunits of DhaL, each interacting with only one DhaK subunit . The Km of the DhaK-DhaL complex for DhaM is 12 nM . The DhaK and DhaL subunits act antagonistically as corepressor and coactivator, respectively, of the G6628-MONOMER DhaR transcription factor that controls expression of the dhaKLM operon . A mutant lacking PTSI-MONOMER EI can not phosphorylate DHA . Review: Dihydroxyacetone (DHA) can serve as the sole source of carbon and energy for E...

## Biological Role

Catalyzes 2.7.1.121-RXN (reaction.ecocyc.2.7.1.121-RXN).

## Annotation

Dihydroxyacetone (DHA) can serve as the sole source of carbon and energy for E. coli K-12, but only in a low phosphate environment (possibly due to the buildup of methylglyoxal) . Dihydroxyacetone kinase is an unusal enzyme that functions similarly to a phosphotransferase system (PTS) in that it utilizes phosphoenolpyruvate as a phosphate donor. However, the enzyme is cytoplasmic and is not involved in transmembrane transport . The phosphorylation reaction requires the presence of the PTSI-MONOMER EI and PTSH-MONOMER HPr proteins of the PTS system to phosphorylate the DhaM protein . DhaM then transfers the phosphate group to the ADP cofactor of DhaL, which in turn transfers it to dihydroxyacetone that is bound to the DhaK subunit . A mechanism for the phosphotransferase reaction has been proposed . DhaK and DhaL form a complex consisting of a central DhaK dimer and two subunits of DhaL, each interacting with only one DhaK subunit . The Km of the DhaK-DhaL complex for DhaM is 12 nM . The DhaK and DhaL subunits act antagonistically as corepressor and coactivator, respectively, of the G6628-MONOMER DhaR transcription factor that controls expression of the dhaKLM operon . A mutant lacking PTSI-MONOMER EI can not phosphorylate DHA . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.1.121-RXN|reaction.ecocyc.2.7.1.121-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-8206|complex.ecocyc.CPLX0-8206]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P37349|protein.P37349]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P76014|protein.P76014]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P76015|protein.P76015]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-2081`
- `PDB:3PNL`
- `QSPROTEOME:QS00195673`

## Notes

2*protein.P76015|2*protein.P76014|complex.ecocyc.CPLX0-8206
