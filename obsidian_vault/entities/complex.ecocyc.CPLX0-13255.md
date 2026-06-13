---
entity_id: "complex.ecocyc.CPLX0-13255"
entity_type: "complex"
name: "DNA replication protein DnaC"
source_database: "EcoCyc"
source_id: "CPLX0-13255"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA replication protein DnaC

`complex.ecocyc.CPLX0-13255`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-13255`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEF0|protein.P0AEF0]]

## Enriched Summary

DnaC is an accessory protein that loads the DnaB replicative helicase onto duplex DNA to initiate replication and onto single-stranded DNA to assist in primer formation by primase . As a consequence, DnaC is required for replication initiation, primer synthesis and restarting at stalled replication forks . Following binding of the replication initiator protein DnaA at the origin of replication oriC, DnaC loads DnaB onto the same site to yield an asymmetric prepriming complex consisting of DnaA and DnaB . Following loading by DnaC, DnaB unwinds DNA in both directions from oriC . The interaction between DnaC and DnaB is complex and has consequences for DnaB activation and subsequent function. DnaC and DnaB bind in an ATP-dependent manner . With DnaB and ATP engaged, DnaC is then able to bind single-stranded DNA (ssDNA) . Following binding, DnaC hydrolyzes its ATP, resulting in a fifty-fold drop in its affinity for ssDNA and thus release from both the DNA and DnaB . Even though ATP hydrolysis has no direct effect on binding of DnaC to DnaB, when it is blocked, DnaB helicase activity is severely curtailed due to the inhibitory effect of DnaC that remains bound to the DNA . DnaB helicase function has been shown both in vitro and in vivo to depend on the relative quantity of DnaB and DnaC, being inversely proportional to the amount of excess DnaC present...

## Biological Role

Component of DNA replication restart primosome (complex.ecocyc.CPLX0-3922).

## Annotation

DnaC is an accessory protein that loads the DnaB replicative helicase onto duplex DNA to initiate replication and onto single-stranded DNA to assist in primer formation by primase . As a consequence, DnaC is required for replication initiation, primer synthesis and restarting at stalled replication forks . Following binding of the replication initiator protein DnaA at the origin of replication oriC, DnaC loads DnaB onto the same site to yield an asymmetric prepriming complex consisting of DnaA and DnaB . Following loading by DnaC, DnaB unwinds DNA in both directions from oriC . The interaction between DnaC and DnaB is complex and has consequences for DnaB activation and subsequent function. DnaC and DnaB bind in an ATP-dependent manner . With DnaB and ATP engaged, DnaC is then able to bind single-stranded DNA (ssDNA) . Following binding, DnaC hydrolyzes its ATP, resulting in a fifty-fold drop in its affinity for ssDNA and thus release from both the DNA and DnaB . Even though ATP hydrolysis has no direct effect on binding of DnaC to DnaB, when it is blocked, DnaB helicase activity is severely curtailed due to the inhibitory effect of DnaC that remains bound to the DNA . DnaB helicase function has been shown both in vitro and in vivo to depend on the relative quantity of DnaB and DnaC, being inversely proportional to the amount of excess DnaC present . This may explain the lethality of DnaC overexpression . The temporary DnaC-DnaB complex consists of six DnaC monomers bound to the hexameric DnaB helicase . Thus, even though isolated DnaC is a monomer, it still experiences cooperativity in response to ATP binding when the DnaB hexamer is present . Based on cryo-EM studies of the DnaC-DnaB complex, the DnaC monomers arrange as three dimers that bind to the three-fold symmet

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3922|complex.ecocyc.CPLX0-3922]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AEF0|protein.P0AEF0]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-13255`

## Notes

6*protein.P0AEF0
