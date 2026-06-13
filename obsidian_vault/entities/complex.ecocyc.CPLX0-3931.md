---
entity_id: "complex.ecocyc.CPLX0-3931"
entity_type: "complex"
name: "ATP-dependent DNA helicase Rep"
source_database: "EcoCyc"
source_id: "CPLX0-3931"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ATP-dependent DNA helicase Rep

`complex.ecocyc.CPLX0-3931`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3931`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P09980|protein.P09980]]

## Enriched Summary

Rep is an ATP-dependent helicase belonging to the SF1 superfamily. It is a component of the replisome and is required for replication of some bacteriophages . Rep provides a replication fork-specific motor that facilitates replication through highly transcribed regions of the chromosome . By preventing replication fork stalling, Rep helicase prevents double-strand breaks and resultant illegitimate recombination between phage and bacterial genomes . Rep also acts with PriC in a replication fork restart pathway and in overcoming replication fork arrest due to UV damage . Rep helicase activity has been studied in great detail. Rep proceeds in the 3' to 5' direction relative to the bound strand and is stimulated by binding to single-stranded DNA (ssDNA) . Rep dimerizes after binding ssDNA or double-stranded DNA (dsDNA) . Dimerization is required for initiation, stimulation and processivity of helicase activity . This binding cycle is regulated by ATP, with hydrolysis of bound ATP to ADP promoting release of ssDNA by one subunit and binding of ssDNA rather than dsDNA by the other . Perhaps as a consequence of this mechanism, Rep is only processive at forks and not on ssDNA, and its two bound strands are kinetically distinct . The binding and hydrolysis of ATP by Rep have been studied in depth...

## Biological Role

Catalyzes RXN-11135 (reaction.ecocyc.RXN-11135).

## Annotation

Rep is an ATP-dependent helicase belonging to the SF1 superfamily. It is a component of the replisome and is required for replication of some bacteriophages . Rep provides a replication fork-specific motor that facilitates replication through highly transcribed regions of the chromosome . By preventing replication fork stalling, Rep helicase prevents double-strand breaks and resultant illegitimate recombination between phage and bacterial genomes . Rep also acts with PriC in a replication fork restart pathway and in overcoming replication fork arrest due to UV damage . Rep helicase activity has been studied in great detail. Rep proceeds in the 3' to 5' direction relative to the bound strand and is stimulated by binding to single-stranded DNA (ssDNA) . Rep dimerizes after binding ssDNA or double-stranded DNA (dsDNA) . Dimerization is required for initiation, stimulation and processivity of helicase activity . This binding cycle is regulated by ATP, with hydrolysis of bound ATP to ADP promoting release of ssDNA by one subunit and binding of ssDNA rather than dsDNA by the other . Perhaps as a consequence of this mechanism, Rep is only processive at forks and not on ssDNA, and its two bound strands are kinetically distinct . The binding and hydrolysis of ATP by Rep have been studied in depth . Other studies on Rep activity and kinetics indicate that Rep actively unwinds dsDNA rather than working through mass action, that it cycles back to its starting point when blocked by a lesion, that it is more effective on shorter test substrates, and that it uses two ATP molecules per base pair melted . As described above, on binding DNA, Rep dimerizes into a more active, functional form. This dimerization occurs even if the two Rep monomers do not bind the same piece of DNA . DNA bin

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11135|reaction.ecocyc.RXN-11135]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P09980|protein.P09980]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3931`
- `QSPROTEOME:QS00182757`

## Notes

2*protein.P09980
