---
entity_id: "complex.ecocyc.CPLX0-3925"
entity_type: "complex"
name: "DNA polymerase V"
source_database: "EcoCyc"
source_id: "CPLX0-3925"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Pol V"
---

# DNA polymerase V

`complex.ecocyc.CPLX0-3925`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3925`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P04152|protein.P04152]], [[protein.P0AG11|protein.P0AG11]]

## Enriched Summary

DNA Polymerase V (Pol V) is responsible for highly mutagenic bypass of DNA lesions that are not effectively passed through by the normal replicative DNA polymerase, Pol III . It also protects against the effects of nucleotide starvation . It is one of three SOS induced DNA polymerases that contribute to translesion DNA synthesis (TLS) in E. coli K-12. Various models for Pol V activity have been proposed; the active Pol V mutasome is currently thought to comprise EG11057-MONOMER UmuD'2-EG11056-MONOMER UmuC-EG10823-MONOMER RecA-ATP (PolV Mut) (and see review by ). PolV Mut is a DNA dependent ATPase; Pol V Mut requires ATP to bind template DNA and catalyse extension in vitro; ATP hydrolysis functions to release Pol V from DNA ensuring that error-prone DNA synthesis is limited Pol V carries out efficient synthesis through various DNA error sites, including thymine dimers, guanine oxidation products, abasic lesions and N-2-acetylaminofluorene (AAF) induced frame-shift mutations . It is required for repair of methyl methanesulfonate (MMS) induced lesions and can even carry out bypass synthesis over an artificial gap of methylene residues . PolV is responsible for replication readthrough following UV irradiation . Pol V bypasses abasic lesions 100-150 times more efficiently than the primary replicative DNA polymerase, Pol III...

## Biological Role

Catalyzes DNA-DIRECTED-DNA-POLYMERASE-RXN (reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN).

## Annotation

DNA Polymerase V (Pol V) is responsible for highly mutagenic bypass of DNA lesions that are not effectively passed through by the normal replicative DNA polymerase, Pol III . It also protects against the effects of nucleotide starvation . It is one of three SOS induced DNA polymerases that contribute to translesion DNA synthesis (TLS) in E. coli K-12. Various models for Pol V activity have been proposed; the active Pol V mutasome is currently thought to comprise EG11057-MONOMER UmuD'2-EG11056-MONOMER UmuC-EG10823-MONOMER RecA-ATP (PolV Mut) (and see review by ). PolV Mut is a DNA dependent ATPase; Pol V Mut requires ATP to bind template DNA and catalyse extension in vitro; ATP hydrolysis functions to release Pol V from DNA ensuring that error-prone DNA synthesis is limited Pol V carries out efficient synthesis through various DNA error sites, including thymine dimers, guanine oxidation products, abasic lesions and N-2-acetylaminofluorene (AAF) induced frame-shift mutations . It is required for repair of methyl methanesulfonate (MMS) induced lesions and can even carry out bypass synthesis over an artificial gap of methylene residues . PolV is responsible for replication readthrough following UV irradiation . Pol V bypasses abasic lesions 100-150 times more efficiently than the primary replicative DNA polymerase, Pol III . In the absence of Pol V function, DNA lesions are skipped, resulting in frameshifts rather than Pol V-catalyzed base substitutions . Purified, soluble UmuD'2C complex binds cooperatively to ssDNA and to RecA nucleoprotein filaments (known as RecA*) . Purified UmuD'2C requires RecA*, SSB and the β γ sliding clamp complex to catalyse lesion bypass in vitro ; the minimal requirements for lesion bypass in vitro are UmuC, UmuD', RecA* and SSB; the sliding cl

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN|reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P04152|protein.P04152]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AG11|protein.P0AG11]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3925`
- `QSPROTEOME:QS00049420`

## Notes

1*protein.P04152|2*protein.P0AG11
