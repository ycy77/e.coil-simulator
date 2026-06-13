---
entity_id: "complex.ecocyc.CPLX0-7838"
entity_type: "complex"
name: "cysteine sulfinate desulfinase"
source_database: "EcoCyc"
source_id: "CPLX0-7838"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cysteine sulfinate desulfinase

`complex.ecocyc.CPLX0-7838`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7838`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.Q46925|protein.Q46925]]

## Enriched Summary

CsdA is one of three members of the NifS protein family in E. coli, the other two being CPLX0-246 (G6906) and CPLX0-248 (G7325) . CsdA is a desulfinase that can utilize L-cysteine sulfinate, L-cysteine or L-selenocysteine as substrates . The mechanism of L-cysteine desulfurization is different from that of L-selenocysteine degradation . CsdA and CsdE combine to form the cysteine sulfinate desulfinase (CSD) sulfur transfer system. CsdA activity doubles in the presence of CsdE, which contains a cysteine residue (C61) that acts to accept sulfur liberated via the desulfinase activity of CsdA . CsdA can also transfer sulfur directly to CsdL in vitro . Utilizing L-cysteine, the enzyme can provide sulfur to molybdopterin synthase in vitro; the sulfur appears to be transferred as a protein-bound persulfide . It is also able to provide sulfur for the ferredoxin iron-sulfur cluster assembly in vitro . With L-selenocysteine as substrate , CsdA can provide selenide to selenophosphate synthetase . Unlike other cysteine desulfurases, none of the Cys residues of CsdA was reported to be essential for enzymatic activity . In a later report, a C358A mutant was shown to be catalytically inactive towards L-cysteine, but showed activity with L-cysteine sulfinate and L-selenocysteine...

## Biological Role

Catalyzes RXN0-279 (reaction.ecocyc.RXN0-279). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

CsdA is one of three members of the NifS protein family in E. coli, the other two being CPLX0-246 (G6906) and CPLX0-248 (G7325) . CsdA is a desulfinase that can utilize L-cysteine sulfinate, L-cysteine or L-selenocysteine as substrates . The mechanism of L-cysteine desulfurization is different from that of L-selenocysteine degradation . CsdA and CsdE combine to form the cysteine sulfinate desulfinase (CSD) sulfur transfer system. CsdA activity doubles in the presence of CsdE, which contains a cysteine residue (C61) that acts to accept sulfur liberated via the desulfinase activity of CsdA . CsdA can also transfer sulfur directly to CsdL in vitro . Utilizing L-cysteine, the enzyme can provide sulfur to molybdopterin synthase in vitro; the sulfur appears to be transferred as a protein-bound persulfide . It is also able to provide sulfur for the ferredoxin iron-sulfur cluster assembly in vitro . With L-selenocysteine as substrate , CsdA can provide selenide to selenophosphate synthetase . Unlike other cysteine desulfurases, none of the Cys residues of CsdA was reported to be essential for enzymatic activity . In a later report, a C358A mutant was shown to be catalytically inactive towards L-cysteine, but showed activity with L-cysteine sulfinate and L-selenocysteine . Overexpression of csdA suppresses the growth defect of an iscS sufS double mutant due to interaction of CsdA with the SufBCDE system . In growth competition experiments, a csdA mutant is outcompeted by wild type after 48 h of co-culture. A csdA mutant is unable to swim . CsdA: "cysteine sulfinate desulfinase" Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-279|reaction.ecocyc.RXN0-279]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.Q46925|protein.Q46925]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7838`
- `QSPROTEOME:QS00093654`

## Notes

2*protein.Q46925
