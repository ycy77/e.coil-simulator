---
entity_id: "complex.ecocyc.CPLX0-7824"
entity_type: "complex"
name: "[Fe-S] cluster insertion protein SufA"
source_database: "EcoCyc"
source_id: "CPLX0-7824"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# [Fe-S] cluster insertion protein SufA

`complex.ecocyc.CPLX0-7824`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7824`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P77667|protein.P77667]]

## Enriched Summary

The assembly of iron-sulfur clusters requires complex biosynthetic machinery. E. coli encodes two sets of proteins, the Isc and the Suf system, to achieve this task. SufA is the type II A-type carrier (ATC-II) component of the Suf system for iron-sulfur cluster assembly that is utilized under iron starvation or oxidative stress conditions . SufA accepts Fe-S clusters formed by the SufBCD complex and transfers them to target proteins ; it was shown to carry a [2Fe-2S] cluster and to be able to transfer its cluster to target apoproteins such as ferredoxin (a [2Fe-2S]-containing protein) and aconitase A (a [4Fe-4S]-containing protein) . Contradictory results of earlier studies - some of which are reported below - were likely due to purification of apo-SufA and in vitro assays under conditions that may not have been physiologically relevant . SufA can accept sulfur atoms from the SufE component of the SufE-SufS cysteine desulfurase ; however, label transfer experiments don't show interactions between SufA and SufE/S . In vitro, purified apoSufA can chelate iron-sulfur clusters by treatment with iron and sulfide under anaerobic conditions. HoloSufA then can form a fast and tight association with the target apoprotein BIOTIN-SYN-CPLX (BioB) and transfers a [4Fe-4S] cluster to BioB in a slow reaction . Reports disagree on whether or not purified apoSufA binds iron...

## Annotation

The assembly of iron-sulfur clusters requires complex biosynthetic machinery. E. coli encodes two sets of proteins, the Isc and the Suf system, to achieve this task. SufA is the type II A-type carrier (ATC-II) component of the Suf system for iron-sulfur cluster assembly that is utilized under iron starvation or oxidative stress conditions . SufA accepts Fe-S clusters formed by the SufBCD complex and transfers them to target proteins ; it was shown to carry a [2Fe-2S] cluster and to be able to transfer its cluster to target apoproteins such as ferredoxin (a [2Fe-2S]-containing protein) and aconitase A (a [4Fe-4S]-containing protein) . Contradictory results of earlier studies - some of which are reported below - were likely due to purification of apo-SufA and in vitro assays under conditions that may not have been physiologically relevant . SufA can accept sulfur atoms from the SufE component of the SufE-SufS cysteine desulfurase ; however, label transfer experiments don't show interactions between SufA and SufE/S . In vitro, purified apoSufA can chelate iron-sulfur clusters by treatment with iron and sulfide under anaerobic conditions. HoloSufA then can form a fast and tight association with the target apoprotein BIOTIN-SYN-CPLX (BioB) and transfers a [4Fe-4S] cluster to BioB in a slow reaction . Reports disagree on whether or not purified apoSufA binds iron. A crystal structure of SufA has been solved at 2.7 Å resolution. SufA forms a homodimer in the crystal structure, and the arrangement of four cysteine residues at the dimer interface may allow the coordination of an Fe-S cluster or an iron atom . The sufABCDSE operon encodes components of a secondary pathway of iron-sulfur cluster assembly; the isc operon encodes the major assembly pathway . A sufABCDSE operon delet

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77667|protein.P77667]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7824`
- `QSPROTEOME:QS00184471`

## Notes

2*protein.P77667
