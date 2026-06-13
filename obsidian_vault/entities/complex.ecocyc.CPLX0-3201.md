---
entity_id: "complex.ecocyc.CPLX0-3201"
entity_type: "complex"
name: "peptidoglycan DD-endopeptidase/peptidoglycan LD-endopeptidase"
source_database: "EcoCyc"
source_id: "CPLX0-3201"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# peptidoglycan DD-endopeptidase/peptidoglycan LD-endopeptidase

`complex.ecocyc.CPLX0-3201`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3201`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PERI-BAC-GN
- Complex type: `structural`
- Components: [[protein.P0C0T5|protein.P0C0T5]]

## Enriched Summary

MepA is a penicillin-insensitive DD endopeptidase which hydrolyses DD (meso-A2pm-D-Ala) and LD (meso-A2pm-meso-A2pm) bonds within cell wall peptidoglycan peptide crosslinks. The structure of MepA has been determined to resolutions of 1.4 and 2.4 Å . MepA is a dimer that is localized in the periplasm by its amino-terminal signal peptide . MepA is similar to proteins in the LAS metallopeptidase family. Mutations in putative zinc-coordinating residues histidine-113, aspartate-120 and histidine-211 inactivate MepA, as do metal chelators . Mutation experiments reveal residue D120 is required for folding, while H113 and H211 are required for catalysis . Mutations of H206, H209, and H110 also reduce activity of the enzyme but are not required for folding . Residue W203 is important for substrate binding . MepA forms 3 intramolecular disulphide bonds catalyzed by DsbC . mepA mutants have reduced DD-endopeptidase activity, but grow normally . Purified MepA is able to hydrolyze D-alanyl-DAP and DAP-DAP amide bonds within peptidoglycan polymer . MepA does not appear to hydrolyse murein mDAP-mDAP cross-links under normal laboratory conditions . Overproduction of MepA results in increased amounts of tri- and tetra-peptides released into the medium in a peptide-uptake mutant...

## Biological Role

Catalyzes RXN0-3461 (reaction.ecocyc.RXN0-3461), RXN0-5407 (reaction.ecocyc.RXN0-5407).

## Annotation

MepA is a penicillin-insensitive DD endopeptidase which hydrolyses DD (meso-A2pm-D-Ala) and LD (meso-A2pm-meso-A2pm) bonds within cell wall peptidoglycan peptide crosslinks. The structure of MepA has been determined to resolutions of 1.4 and 2.4 Å . MepA is a dimer that is localized in the periplasm by its amino-terminal signal peptide . MepA is similar to proteins in the LAS metallopeptidase family. Mutations in putative zinc-coordinating residues histidine-113, aspartate-120 and histidine-211 inactivate MepA, as do metal chelators . Mutation experiments reveal residue D120 is required for folding, while H113 and H211 are required for catalysis . Mutations of H206, H209, and H110 also reduce activity of the enzyme but are not required for folding . Residue W203 is important for substrate binding . MepA forms 3 intramolecular disulphide bonds catalyzed by DsbC . mepA mutants have reduced DD-endopeptidase activity, but grow normally . Purified MepA is able to hydrolyze D-alanyl-DAP and DAP-DAP amide bonds within peptidoglycan polymer . MepA does not appear to hydrolyse murein mDAP-mDAP cross-links under normal laboratory conditions . Overproduction of MepA results in increased amounts of tri- and tetra-peptides released into the medium in a peptide-uptake mutant . Overproduction of MepA does not result in a reduced proportion of crosslinks in the peptidoglycan layer suggesting the enzyme acts in a progressive manner, possibly as part of a complex, rather than at random . MepA is able to digest thickened peptidoglycan septal rings that form due to the absence of AmiABC . The mepA gene is upregulated under basic, oxygen-limited conditions , and expression was lowest at neutral pH under aeration . Expression of mepA was also repressed by acivicin treatment . When cells were

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3461|reaction.ecocyc.RXN0-3461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5407|reaction.ecocyc.RXN0-5407]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0C0T5|protein.P0C0T5]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3201`
- `QSPROTEOME:QS00188901`
- `PDB:1tzp`
- `PDB:1u10`

## Notes

2*protein.P0C0T5
