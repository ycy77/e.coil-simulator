---
entity_id: "complex.ecocyc.ABC-41-CPLX"
entity_type: "complex"
name: "putative oligopeptide ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-41-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# putative oligopeptide ABC transporter

`complex.ecocyc.ABC-41-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-41-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P33916|protein.P33916]], [[protein.P0AFU0|protein.P0AFU0]], [[protein.P33915|protein.P33915]], [[protein.P33913|protein.P33913]]

## Enriched Summary

yejA, yejB, yejE, and yejF encode the components of a predicted ATP-dependent oligopeptide permease. Sequence analysis suggests that YejA is the periplasmic binding protein, YejB and YejE are the inner membrane components, and YejF is the ATP-binding component of the transporter complex; yejA, yejB, yejE and yejF deletion mutants (in E. coli K-12 strain BW28357) are resistant to the toxic modified heptapeptide, CPD0-1129 due to a deficiency in uptake . Uptake of Microcin C is peptide length dependent and requires an N-terminal formyl-methionyl-arginyl sequence; in vivo competition assays (in which oligopeptide competition with Microcin C for Yej mediated transport will result in Microcin C resistance) suggests that the preferred peptide length is more than 7 but less than 13 amino acids . yejA, yejB, yejE, and yejF are transcribed in one direction and likely form an operon; operons similar to yejABEF occur in many bacterial species . Expression of yejABEF appears to be regulated by the RNA0-328; yejABEF is transcribed during growth in minimal media (but not in rich media); impairing rydC expression results in decreased yejABEF mRNA while overexpression of rydC results in degradation of yejABEF mRNA in vivo; a preformed RydC-Hfq complex binds to yejAB mRNA...

## Biological Role

Catalyzes 3.6.3.23-RXN (reaction.ecocyc.3.6.3.23-RXN). Transports Oligopeptide (molecule.C00098), hν (molecule.ecocyc.Light).

## Annotation

yejA, yejB, yejE, and yejF encode the components of a predicted ATP-dependent oligopeptide permease. Sequence analysis suggests that YejA is the periplasmic binding protein, YejB and YejE are the inner membrane components, and YejF is the ATP-binding component of the transporter complex; yejA, yejB, yejE and yejF deletion mutants (in E. coli K-12 strain BW28357) are resistant to the toxic modified heptapeptide, CPD0-1129 due to a deficiency in uptake . Uptake of Microcin C is peptide length dependent and requires an N-terminal formyl-methionyl-arginyl sequence; in vivo competition assays (in which oligopeptide competition with Microcin C for Yej mediated transport will result in Microcin C resistance) suggests that the preferred peptide length is more than 7 but less than 13 amino acids . yejA, yejB, yejE, and yejF are transcribed in one direction and likely form an operon; operons similar to yejABEF occur in many bacterial species . Expression of yejABEF appears to be regulated by the RNA0-328; yejABEF is transcribed during growth in minimal media (but not in rich media); impairing rydC expression results in decreased yejABEF mRNA while overexpression of rydC results in degradation of yejABEF mRNA in vivo; a preformed RydC-Hfq complex binds to yejAB mRNA . Expression of yejABEF is increased in minimal media supplemented with ribose as compared to glucose

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.3.6.3.23-RXN|reaction.ecocyc.3.6.3.23-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00098|molecule.C00098]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P0AFU0|protein.P0AFU0]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P33913|protein.P33913]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P33915|protein.P33915]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P33916|protein.P33916]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-41-CPLX`
- `QSPROTEOME:QS00049322`

## Notes

1*protein.P33916|1*protein.P0AFU0|1*protein.P33915|1*protein.P33913
