---
entity_id: "complex.ecocyc.CPLX-3946"
entity_type: "complex"
name: "exodeoxyribonuclease VII"
source_database: "EcoCyc"
source_id: "CPLX-3946"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ExoVII"
---

# exodeoxyribonuclease VII

`complex.ecocyc.CPLX-3946`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-3946`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P04994|protein.P04994]], [[protein.P0A8G9|protein.P0A8G9]]

## Enriched Summary

Exonuclease VII (ExoVII) is a single-strand DNA exonuclease implicated in various aspects of DNA repair. Purified ExoVII is an ATP-independent exonuclease which degrades single-stranded DNA (ssDNA) from both 3' and 5' termini; it can degrade 5' and 3' single strands extending from duplex DNA and it can excise thymine dimers (after incision by an appropriate endonuclease); in vitro the enzyme hydrolyzes DNA processively to yield oligonucleotides of varying length . Purified ExoVII cannot digest circular ssDNA or linear ssDNA with blocked ends; it can digest linear duplex DNA that contains a nick or ssDNA gap which is suggestive of the potential for endonuclease activity . ExoVII is directly involved in the repair of quinolone-induced, trapped CPLX0-2425 in vivo - denaturation of the trapped enzyme is required for efficient excision; ExoVII has tyrosyl-DNA phosphodiesterase activity - the purified enzyme excises tyrosine adducts on 5'-DNA and 3'-DNA ends (preferring a 4 or 5-base single-stranded overhang; ExoVII-deficient strains show hypersensitivity to CPD-12843 and accumulate trapped DNA gyrase upon ciprofloxacin treatment . ExoVII consists of large (XseA) and small (XseB) subunits; early work suggested assembly into an XseA1-XseB4 or XseA1-XseB6 complex...

## Biological Role

Catalyzes 3.1.11.6-RXN (reaction.ecocyc.3.1.11.6-RXN), RXN-24399 (reaction.ecocyc.RXN-24399).

## Annotation

Exonuclease VII (ExoVII) is a single-strand DNA exonuclease implicated in various aspects of DNA repair. Purified ExoVII is an ATP-independent exonuclease which degrades single-stranded DNA (ssDNA) from both 3' and 5' termini; it can degrade 5' and 3' single strands extending from duplex DNA and it can excise thymine dimers (after incision by an appropriate endonuclease); in vitro the enzyme hydrolyzes DNA processively to yield oligonucleotides of varying length . Purified ExoVII cannot digest circular ssDNA or linear ssDNA with blocked ends; it can digest linear duplex DNA that contains a nick or ssDNA gap which is suggestive of the potential for endonuclease activity . ExoVII is directly involved in the repair of quinolone-induced, trapped CPLX0-2425 in vivo - denaturation of the trapped enzyme is required for efficient excision; ExoVII has tyrosyl-DNA phosphodiesterase activity - the purified enzyme excises tyrosine adducts on 5'-DNA and 3'-DNA ends (preferring a 4 or 5-base single-stranded overhang; ExoVII-deficient strains show hypersensitivity to CPD-12843 and accumulate trapped DNA gyrase upon ciprofloxacin treatment . ExoVII consists of large (XseA) and small (XseB) subunits; early work suggested assembly into an XseA1-XseB4 or XseA1-XseB6 complex . Cryo-electron microscopy indicates that DNA-free ExoVII assembles into a large spindle-shaped complex that comprises 4 copies of XseA and 24 copies of XseB . ExoVII binds to linear ssDNA or linear duplex DNA and this interaction induces disassembly of the XseA4-XseB24 tetramer into an XseA2-XseB12 dimer . xse- mutant strains have reduced levels of exonuclease VII activity; xse- strains display increased sensitivity to the DNA synthesis inhibitor, CPD-21025, and are slightly more sensitive to UV irradiation than the p

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.3.1.11.6-RXN|reaction.ecocyc.3.1.11.6-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24399|reaction.ecocyc.RXN-24399]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P04994|protein.P04994]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `is_component_of` <-- [[protein.P0A8G9|protein.P0A8G9]] `EcoCyc` `database` - EcoCyc component coefficient=24 | EcoCyc protcplxs.col coefficient=24

## External IDs

- `EcoCyc:CPLX-3946`
- `QSPROTEOME:QS00196467`
- `PDB:8TXR`

## Notes

4*protein.P04994|24*protein.P0A8G9
