---
entity_id: "complex.ecocyc.ABC-12-CPLX"
entity_type: "complex"
name: "L-glutamine ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-12-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-glutamine ABC transporter

`complex.ecocyc.ABC-12-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-12-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P10346|protein.P10346]], [[protein.P0AEQ6|protein.P0AEQ6]], [[protein.P0AEQ3|protein.P0AEQ3]]

## Enriched Summary

glnH, glnP and glnQ encode proteins that constitute an L-glutamine uptake system in E. coli K-12. The transporter complex is a member of the ATP-Binding Cassette (ABC) superfamily of transporters; GlnH is the periplasmic L-glutamine-binding protein, GlnQ is the predicted ATP-binding subunit, and GlnP is the predicted integral membrane subunit of the transporter complex. Early studies using E. coli K-10 and K-12 derived strains strains characterised a high affinity, binding protein dependent L-glutamine uptake system . Further genetic analysis led to the identification of the glnP locus; glnP mutants were unable to transport L-glutamine and were unable to grow on L-glutamine (nor glutamate, nor proline) as a sole source of carbon; they were also resistant to toxic glutamine analogues . glnH, glnP and glnQ encode the components of the binding protein dependent L-glutamine uptake system, all of which are necessary for the utilization of L-glutamine as a sole carbon source; glnH is the stuctural gene of the periplasmic binding protein and glnP encodes a membrane bound component ; glnQ is the predicted ATP binding subunit . The regulation of glnHPQ expression is complex and is controlled by both global carbon and global nitrogen signal transduction pathways...

## Biological Role

Catalyzes ABC-12-RXN (reaction.ecocyc.ABC-12-RXN). Transports L-Glutamine (molecule.C00064), hν (molecule.ecocyc.Light).

## Annotation

glnH, glnP and glnQ encode proteins that constitute an L-glutamine uptake system in E. coli K-12. The transporter complex is a member of the ATP-Binding Cassette (ABC) superfamily of transporters; GlnH is the periplasmic L-glutamine-binding protein, GlnQ is the predicted ATP-binding subunit, and GlnP is the predicted integral membrane subunit of the transporter complex. Early studies using E. coli K-10 and K-12 derived strains strains characterised a high affinity, binding protein dependent L-glutamine uptake system . Further genetic analysis led to the identification of the glnP locus; glnP mutants were unable to transport L-glutamine and were unable to grow on L-glutamine (nor glutamate, nor proline) as a sole source of carbon; they were also resistant to toxic glutamine analogues . glnH, glnP and glnQ encode the components of the binding protein dependent L-glutamine uptake system, all of which are necessary for the utilization of L-glutamine as a sole carbon source; glnH is the stuctural gene of the periplasmic binding protein and glnP encodes a membrane bound component ; glnQ is the predicted ATP binding subunit . The regulation of glnHPQ expression is complex and is controlled by both global carbon and global nitrogen signal transduction pathways. Expression is controlled by tandem promoters (σ70, CRP-cAMP dependent glnHp1 and σ54, NtrC dependent glnHp2) in response to both nitrogen limitation and nitrogen source (see also related reviews by ) A low affinity system for L-glutamine transport can been detected when the high affinity transporter is repressed . The complex stoichiometry shown here - (GlnH)(GlnP)2(GlnH)2 - has not been experimentally confirmed

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-12-RXN|reaction.ecocyc.ABC-12-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0AEQ3|protein.P0AEQ3]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AEQ6|protein.P0AEQ6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P10346|protein.P10346]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:ABC-12-CPLX`
- `QSPROTEOME:QS00049300`

## Notes

2*protein.P10346|2*protein.P0AEQ6|1*protein.P0AEQ3
