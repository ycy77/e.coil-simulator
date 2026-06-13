---
entity_id: "complex.ecocyc.CPLX0-7806"
entity_type: "complex"
name: "disulfide bond oxidoreductase YfcG"
source_database: "EcoCyc"
source_id: "CPLX0-7806"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "disulfide reductase"
---

# disulfide bond oxidoreductase YfcG

`complex.ecocyc.CPLX0-7806`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7806`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77526|protein.P77526]]

## Enriched Summary

YfcG has disulfide reductase activity using the model substrate 2-hydroxyethyldisulfide; the physiological substrate is unknown. No sulfhydryl groups within YfcG appear to be involved in the catalysis of this redox reaction; a non-covalently bound thiol-disulfide couple may perform the analogous function . YfcG has sequence similarity to glutathione S-transferase and has weak glutathione S-transferase activity with 1-chloro-2,4-dinitrobenzene and GSH-dependent peroxidase activity toward cumene hydroperoxide . A crystal structure of the enzyme has been determined at 2.3 Å resolution, showing a typical GSH transferase fold and dimeric quarternary structure. Surprisingly, a molecule of glutathione disulfide (GSSG) was found in the active site, between the two subunits of the dimer and exposing the disulfide bond of GSSG on the surface of the protein . Site-directed mutagenesis of the predicted active site residue Asn11 showed that it is important for catalytic activity . Expression of yfcG (o215) is dependent on RpoS . Deletion of yfcG decreases the resistance to hydrogen peroxide . YfcG has disulfide reductase activity using the model substrate 2-hydroxyethyldisulfide; the physiological substrate is unknown...

## Biological Role

Catalyzes RXN0-6256 (reaction.ecocyc.RXN0-6256).

## Annotation

YfcG has disulfide reductase activity using the model substrate 2-hydroxyethyldisulfide; the physiological substrate is unknown. No sulfhydryl groups within YfcG appear to be involved in the catalysis of this redox reaction; a non-covalently bound thiol-disulfide couple may perform the analogous function . YfcG has sequence similarity to glutathione S-transferase and has weak glutathione S-transferase activity with 1-chloro-2,4-dinitrobenzene and GSH-dependent peroxidase activity toward cumene hydroperoxide . A crystal structure of the enzyme has been determined at 2.3 Å resolution, showing a typical GSH transferase fold and dimeric quarternary structure. Surprisingly, a molecule of glutathione disulfide (GSSG) was found in the active site, between the two subunits of the dimer and exposing the disulfide bond of GSSG on the surface of the protein . Site-directed mutagenesis of the predicted active site residue Asn11 showed that it is important for catalytic activity . Expression of yfcG (o215) is dependent on RpoS . Deletion of yfcG decreases the resistance to hydrogen peroxide .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6256|reaction.ecocyc.RXN0-6256]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77526|protein.P77526]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7806`
- `QSPROTEOME:QS00182029`

## Notes

2*protein.P77526
