---
entity_id: "complex.ecocyc.HOMSUCTRAN-CPLX"
entity_type: "complex"
name: "homoserine O-succinyltransferase"
source_database: "EcoCyc"
source_id: "HOMSUCTRAN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# homoserine O-succinyltransferase

`complex.ecocyc.HOMSUCTRAN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:HOMSUCTRAN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P07623|protein.P07623]]

## Enriched Summary

Homoserine O-succinyltransferase (MetA) catalyzes the first unique step in the de novo HOMOSER-METSYN-PWY in Escherichia coli: transferring a succinyl group from succinyl-CoA to homoserine. It is regulated at several levels, and it appears to have a role in regulating bacterial growth. Its activity is regulated through allosteric feedback inhibition by the pathway end product methionine and also synergistically by the methionine derivative S-adenosylmethionine (see pathway PWY-6151). Expression of the enzyme is negatively regulated at the transcriptional level by the methionine regulon repressor EG10588 and positively regulated by the activator EG10591. MetA has been shown to be a heat shock protein . It was found to be very thermolabile, undergoing aggregation and proteolysis at elevated temperatures . It appears to be regulated by temperature-dependent proteolysis, thereby mediating a change in growth rate as a function of temperature . Using YFP-fused MetA as a representative protein, it was found to form polar aggregates in temperature upshift experiments to 45°C with chaperones EG10241-MONOMER DnaK, EG10240-MONOMER DnaJ and EG10157-MONOMER ClpB associating with the aggregates. Aggregation appears to be driven by nucleoid occlusion based on lack of aggregation in cells with EG10618 deleted...

## Biological Role

Catalyzes HOMSUCTRAN-RXN (reaction.ecocyc.HOMSUCTRAN-RXN).

## Annotation

Homoserine O-succinyltransferase (MetA) catalyzes the first unique step in the de novo HOMOSER-METSYN-PWY in Escherichia coli: transferring a succinyl group from succinyl-CoA to homoserine. It is regulated at several levels, and it appears to have a role in regulating bacterial growth. Its activity is regulated through allosteric feedback inhibition by the pathway end product methionine and also synergistically by the methionine derivative S-adenosylmethionine (see pathway PWY-6151). Expression of the enzyme is negatively regulated at the transcriptional level by the methionine regulon repressor EG10588 and positively regulated by the activator EG10591. MetA has been shown to be a heat shock protein . It was found to be very thermolabile, undergoing aggregation and proteolysis at elevated temperatures . It appears to be regulated by temperature-dependent proteolysis, thereby mediating a change in growth rate as a function of temperature . Using YFP-fused MetA as a representative protein, it was found to form polar aggregates in temperature upshift experiments to 45°C with chaperones EG10241-MONOMER DnaK, EG10240-MONOMER DnaJ and EG10157-MONOMER ClpB associating with the aggregates. Aggregation appears to be driven by nucleoid occlusion based on lack of aggregation in cells with EG10618 deleted . It has been suggested that MetA serves a role of a thermal "fuse", protecting the bacteria from dying at high temperatures. Degradation of MetA at high temperature cuts off methionine production, and as a result, biosynthesis and growth. The resulting growth arrest protects the bacteria in case the temperatures rise beyond the habitable range. It has been reported that the absence of functional MetA increases survival chances by more than 1,000-fold at temperatures exceeding 50°

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.HOMSUCTRAN-RXN|reaction.ecocyc.HOMSUCTRAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P07623|protein.P07623]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:HOMSUCTRAN-CPLX`
- `QSPROTEOME:QS00181845`

## Notes

2*protein.P07623
