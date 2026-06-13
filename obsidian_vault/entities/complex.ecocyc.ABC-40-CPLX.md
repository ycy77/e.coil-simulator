---
entity_id: "complex.ecocyc.ABC-40-CPLX"
entity_type: "complex"
name: "glycine betaine ABC transporter, non-osmoregulatory"
source_database: "EcoCyc"
source_id: "ABC-40-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glycine betaine ABC transporter, non-osmoregulatory

`complex.ecocyc.ABC-40-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-40-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P33362|protein.P33362]], [[protein.P33361|protein.P33361]], [[protein.P33360|protein.P33360]], [[protein.P33359|protein.P33359]]

## Enriched Summary

YehY, YehX, YehW and OsmF belong to the ATP Binding Cassette (ABC) superfamily of transporters . YehX is a putative ATP binding component, YehW and YehY are putative integral membrane components, and OsmF is a periplasmic binding protein that binds the osmoprotectants glycine betaine, CPD-543 "choline-0-sulfate" and SS-DIMETHYL-BETA-PROPIOTHETIN "dimethylsulfopropionate" with low (mM) affinities . osmF, yehY, yehX and yehW are predicted to form an operon in E. coli K-12 . Transport assays in a strain expressing osmFyehYXW from a plasmid suggest that the protein complex is able to catalyse glycine betaine uptake; transport activity is low and decreases as the salinity of the assay medium increases . The physiological role of OsmFYehYXW is not clear. Osmotic shock and entry into stationary phase induces σs dependent transcription of the osmFyehYXW operon ; conversely osmFyehYXW expressed from a plasmid in a strain lacking all known osmolyte accumulation mechanisms does not mediate osmotic stress protection . YehY, YehX, YehW and OsmF belong to the ATP Binding Cassette (ABC) superfamily of transporters...

## Biological Role

Catalyzes TRANS-RXN-283 (reaction.ecocyc.TRANS-RXN-283). Transports Betaine (molecule.C00719), hν (molecule.ecocyc.Light).

## Annotation

YehY, YehX, YehW and OsmF belong to the ATP Binding Cassette (ABC) superfamily of transporters . YehX is a putative ATP binding component, YehW and YehY are putative integral membrane components, and OsmF is a periplasmic binding protein that binds the osmoprotectants glycine betaine, CPD-543 "choline-0-sulfate" and SS-DIMETHYL-BETA-PROPIOTHETIN "dimethylsulfopropionate" with low (mM) affinities . osmF, yehY, yehX and yehW are predicted to form an operon in E. coli K-12 . Transport assays in a strain expressing osmFyehYXW from a plasmid suggest that the protein complex is able to catalyse glycine betaine uptake; transport activity is low and decreases as the salinity of the assay medium increases . The physiological role of OsmFYehYXW is not clear. Osmotic shock and entry into stationary phase induces σs dependent transcription of the osmFyehYXW operon ; conversely osmFyehYXW expressed from a plasmid in a strain lacking all known osmolyte accumulation mechanisms does not mediate osmotic stress protection .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-283|reaction.ecocyc.TRANS-RXN-283]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P33359|protein.P33359]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P33360|protein.P33360]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P33361|protein.P33361]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P33362|protein.P33362]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-40-CPLX`
- `QSPROTEOME:QS00049321`

## Notes

protein.P33362|protein.P33361|protein.P33360|protein.P33359
