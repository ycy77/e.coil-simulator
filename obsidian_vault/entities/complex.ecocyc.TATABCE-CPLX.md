---
entity_id: "complex.ecocyc.TATABCE-CPLX"
entity_type: "complex"
name: "twin arginine protein translocation system"
source_database: "EcoCyc"
source_id: "TATABCE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Tat system"
  - "Tat translocase"
  - "TatABCE"
  - "TatABC"
  - "twin-arginine translocase"
---

# twin arginine protein translocation system

`complex.ecocyc.TATABCE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TATABCE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P69425|protein.P69425]], [[protein.P69423|protein.P69423]], [[protein.P0A843|protein.P0A843]], [[protein.P69428|protein.P69428]]

## Enriched Summary

The twin-arginine translocation (Tat) system (TatABCE) transports folded proteins across the cytoplasmic membrane; Tat substrates include cofactor containing proteins that are critical for respiration . The Tat system functions in parallel to the Sec system which transports unfolded proteins across the cytoplasmic membrane; Tat pathway substrates are characterized by amino-terminal sequences which contain consecutive (twin) arginine residues. Cofactor-containing Tat substrates acquire their cofactors in the cytoplasm where they attain a folded conformation ( and reviewed by ). ΔtatA ΔtatE knockout mutants accumulate cofactor containing respiratory proteins (TMAO reductase, DMSO reductase, formate dehydrogenase N, hydrogenase I and II) in the cytoplasm . Deletion of tatC blocks the export of precursor proteins that contain twin-arginine signal sequences and are predicted to bind redox cofactors . The twin arginine signal peptide from TMAO reductase (TorA) is able to direct the Tat-dependent export of active (ie. folded) green fluorescent protein (GFP) in E. coli K-12 . Tat system proteins are encoded by genes in two loci - a tatABCD operon and a separate monocistronic unit containing tatE...

## Biological Role

Catalyzes protein translocation (reaction.ecocyc.TRANS-RXN0-181).

## Annotation

The twin-arginine translocation (Tat) system (TatABCE) transports folded proteins across the cytoplasmic membrane; Tat substrates include cofactor containing proteins that are critical for respiration . The Tat system functions in parallel to the Sec system which transports unfolded proteins across the cytoplasmic membrane; Tat pathway substrates are characterized by amino-terminal sequences which contain consecutive (twin) arginine residues. Cofactor-containing Tat substrates acquire their cofactors in the cytoplasm where they attain a folded conformation ( and reviewed by ). ΔtatA ΔtatE knockout mutants accumulate cofactor containing respiratory proteins (TMAO reductase, DMSO reductase, formate dehydrogenase N, hydrogenase I and II) in the cytoplasm . Deletion of tatC blocks the export of precursor proteins that contain twin-arginine signal sequences and are predicted to bind redox cofactors . The twin arginine signal peptide from TMAO reductase (TorA) is able to direct the Tat-dependent export of active (ie. folded) green fluorescent protein (GFP) in E. coli K-12 . Tat system proteins are encoded by genes in two loci - a tatABCD operon and a separate monocistronic unit containing tatE . TatA, TatB and TatE are similar in structure and predicted to comprise a membrane-spanning alpha helix at the amino terminus, followed by an amphipathic helix and a variable-length carboxy terminus in the cytoplasm . TatA, B and C are integral inner membrane proteins . Translocation of the Tat substrate protein, FtsP, in vivo and in vitro requires TatA, TatB and TatC; translocation is dependent on the presence of a twin-arginine containing signal sequence and the proton motive force . The Tat signal peptide targets precursor proteins to the Tat export machinery and triggers assembly o

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-181|reaction.ecocyc.TRANS-RXN0-181]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P0A843|protein.P0A843]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P69423|protein.P69423]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P69425|protein.P69425]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P69428|protein.P69428]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:TATABCE-CPLX`
- `QSPROTEOME:QS00173717`

## Notes

protein.P69425|protein.P69423|protein.P0A843|protein.P69428
