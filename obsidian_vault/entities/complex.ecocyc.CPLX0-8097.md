---
entity_id: "complex.ecocyc.CPLX0-8097"
entity_type: "complex"
name: "peptide antibiotic transporter"
source_database: "EcoCyc"
source_id: "CPLX0-8097"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# peptide antibiotic transporter

`complex.ecocyc.CPLX0-8097`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8097`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AFY6|protein.P0AFY6]]

## Enriched Summary

Deletion, mutation and complementation studies indicate that sbmA encodes an inner-membrane transport protein which is responsible for the import of Microcin 25 (Mcc25) - a plasmid-encoded peptide antibiotic produced by Escherichia coli AY25 . SbmA transport is energised by the electrochemical gradient . SbmA belongs to the peptide uptake permease family (PUP) . SbmA is proposed to function subsequent to EG10302-MONOMER "FhuA", a multifunctional TonB dependent outer membrane receptor protein for Mcc25. After FhuA-dependent uptake across the outer membrane, SbmA facilitates the translocation of Mcc25 from the periplasmic space across the cytoplasmic membrane . Transposon insertion into sbmA results in resistance to Microcin B17 . sbmA is poorly expressed and overexpression of sbmA from a multicopy plasmid may be lethal . ΔsbmA strains show increased resistance to the antibiotic bleomycin and it has been suggested that thiazole rings constitute the key structural feature that is recognised by SbmA . SbmA transports antisense peptide nucleic acid (PNA) oligomers (antimicrobial compounds designed to target essential bacterial genes ). An E. coli K-12 ΔsbmA strain is resistant to antisense PNA oligomers targeting acpP or ftsZ . sbmA null mutants are resistant to proline-rich antimicrobial peptides of eukaryotic origin...

## Biological Role

Catalyzes TRANS-RXN-205A (reaction.ecocyc.TRANS-RXN-205A). Transports hν (molecule.ecocyc.Light), a peptide antibiotic (molecule.ecocyc.Peptide-Antibiotics).

## Annotation

Deletion, mutation and complementation studies indicate that sbmA encodes an inner-membrane transport protein which is responsible for the import of Microcin 25 (Mcc25) - a plasmid-encoded peptide antibiotic produced by Escherichia coli AY25 . SbmA transport is energised by the electrochemical gradient . SbmA belongs to the peptide uptake permease family (PUP) . SbmA is proposed to function subsequent to EG10302-MONOMER "FhuA", a multifunctional TonB dependent outer membrane receptor protein for Mcc25. After FhuA-dependent uptake across the outer membrane, SbmA facilitates the translocation of Mcc25 from the periplasmic space across the cytoplasmic membrane . Transposon insertion into sbmA results in resistance to Microcin B17 . sbmA is poorly expressed and overexpression of sbmA from a multicopy plasmid may be lethal . ΔsbmA strains show increased resistance to the antibiotic bleomycin and it has been suggested that thiazole rings constitute the key structural feature that is recognised by SbmA . SbmA transports antisense peptide nucleic acid (PNA) oligomers (antimicrobial compounds designed to target essential bacterial genes ). An E. coli K-12 ΔsbmA strain is resistant to antisense PNA oligomers targeting acpP or ftsZ . sbmA null mutants are resistant to proline-rich antimicrobial peptides of eukaryotic origin . Purified SbmA binds the eukaryotic proline-rich antimicrobial peptide Bac7 in vitro . SbmA transports the insect-derived proline-rich antimicrobial peptide pyrrhocoricin . SbmA is implicated in transport of the antimicrobial peptide, arasin . SbmA is a homodimeric inner membrane protein . Homology based protein modeling suggests that SbmA contains eight transmembrane domains with both the N terminus and C terminus located in the cytoplasm . Related reviews:

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-205A|reaction.ecocyc.TRANS-RXN-205A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Peptide-Antibiotics|molecule.ecocyc.Peptide-Antibiotics]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AFY6|protein.P0AFY6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-8097`
- `QSPROTEOME:QS00160625`

## Notes

2*protein.P0AFY6
