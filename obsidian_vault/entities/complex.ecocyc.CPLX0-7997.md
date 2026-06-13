---
entity_id: "complex.ecocyc.CPLX0-7997"
entity_type: "complex"
name: "diaminopimelate epimerase"
source_database: "EcoCyc"
source_id: "CPLX0-7997"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# diaminopimelate epimerase

`complex.ecocyc.CPLX0-7997`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7997`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6K1|protein.P0A6K1]]

## Enriched Summary

Diaminopimelate epimerase (DapF) catalyzes the penultimate step in the biosynthesis of lysine, the stereoinversion of LL-diaminopimelate (LL-DAP) to meso-diaminopimelate (meso-DAP). DapF is a member of the family of pyridoxal phosphate-independent amino acid racemases . The reaction mechanism has been investigated with enzymes purified from other organisms; proton translocation is accomplished via a two-base mechanism involving a pair of cysteine residues. The AZIDAP inhibitor covalently modifies the Cys73 residue . Crystal structures of DapF has been solved . The protein is dimeric in solution and in the crystal structure; the monomeric mutant Y268A has ~1% of wild type activity . DapF directly interacts with G7459-MONOMER RppH and stimulates its activity . Crystal structures of the DapF-RppH complex have been solved . DapF and CMPKI-MONOMER Cmk appear to act together to stimulate RppH . A dapF mutant accumulates LL-DAP, but does not require meso-DAP for growth . It has a longer generation time, and its peptidoglycan contains LL-DAP . Diaminopimelate epimerase (DapF) catalyzes the penultimate step in the biosynthesis of lysine, the stereoinversion of LL-diaminopimelate (LL-DAP) to meso-diaminopimelate (meso-DAP). DapF is a member of the family of pyridoxal phosphate-independent amino acid racemases...

## Biological Role

Catalyzes DIAMINOPIMEPIM-RXN (reaction.ecocyc.DIAMINOPIMEPIM-RXN).

## Annotation

Diaminopimelate epimerase (DapF) catalyzes the penultimate step in the biosynthesis of lysine, the stereoinversion of LL-diaminopimelate (LL-DAP) to meso-diaminopimelate (meso-DAP). DapF is a member of the family of pyridoxal phosphate-independent amino acid racemases . The reaction mechanism has been investigated with enzymes purified from other organisms; proton translocation is accomplished via a two-base mechanism involving a pair of cysteine residues. The AZIDAP inhibitor covalently modifies the Cys73 residue . Crystal structures of DapF has been solved . The protein is dimeric in solution and in the crystal structure; the monomeric mutant Y268A has ~1% of wild type activity . DapF directly interacts with G7459-MONOMER RppH and stimulates its activity . Crystal structures of the DapF-RppH complex have been solved . DapF and CMPKI-MONOMER Cmk appear to act together to stimulate RppH . A dapF mutant accumulates LL-DAP, but does not require meso-DAP for growth . It has a longer generation time, and its peptidoglycan contains LL-DAP .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DIAMINOPIMEPIM-RXN|reaction.ecocyc.DIAMINOPIMEPIM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6K1|protein.P0A6K1]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7997`
- `QSPROTEOME:QS00166595`

## Notes

2*protein.P0A6K1
