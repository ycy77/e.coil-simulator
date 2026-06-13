---
entity_id: "complex.ecocyc.SIROHEMESYN-CPLX"
entity_type: "complex"
name: "siroheme synthase"
source_database: "EcoCyc"
source_id: "SIROHEMESYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# siroheme synthase

`complex.ecocyc.SIROHEMESYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SIROHEMESYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AEA8|protein.P0AEA8]]

## Enriched Summary

CysG is a multifunctional enzyme responsible for the complete transformation of uroporphyrinogen III into siroheme . The first two reactions catalyzed by CysG are S-adenosyl-L-methionine-dependent methylations of uroporphyrinogen III to yield dihydrosirohydrochlorin (precorrin-2), a key intermediate . The third reaction is a pyridine dinucleotide-dependent dehydrogenation converting dihydrosirohydrochlorin into sirohydrochlorin . The fourth and final reaction is the ferrochelation of sirohydrochlorin, which yields siroheme . The enzyme contains two separable domains. The C-terminal domain has uroporphyrinogen III methylase activity, but not dehydrogenase or ferrochelatase activity . Certain mutants in conserved amino acid residues in the C-terminal domain affect S-adenosyl-L-methionine (SAM) binding . SAM may be covalently linked to CysG and a multistep transmethylation mechanism has been proposed . Deletion of the N-terminal NAD+ binding site and mutation of certain amino acid residues affect the dehydrogenase and ferrochelatase activities, but not the methylase activity. The two domains can function independently . cysG shows differential codon adaptation, resulting in differential translation efficiency signatures, in halophilic microbes. It was therefore predicted to play a role in the osmotic stress response...

## Biological Role

Catalyzes DIMETHUROPORDEHYDROG-RXN (reaction.ecocyc.DIMETHUROPORDEHYDROG-RXN), RXN-13403 (reaction.ecocyc.RXN-13403), RXN-8675 (reaction.ecocyc.RXN-8675), SIROHEME-FERROCHELAT-RXN (reaction.ecocyc.SIROHEME-FERROCHELAT-RXN), UROPORIIIMETHYLTRANSA-RXN (reaction.ecocyc.UROPORIIIMETHYLTRANSA-RXN).

## Annotation

CysG is a multifunctional enzyme responsible for the complete transformation of uroporphyrinogen III into siroheme . The first two reactions catalyzed by CysG are S-adenosyl-L-methionine-dependent methylations of uroporphyrinogen III to yield dihydrosirohydrochlorin (precorrin-2), a key intermediate . The third reaction is a pyridine dinucleotide-dependent dehydrogenation converting dihydrosirohydrochlorin into sirohydrochlorin . The fourth and final reaction is the ferrochelation of sirohydrochlorin, which yields siroheme . The enzyme contains two separable domains. The C-terminal domain has uroporphyrinogen III methylase activity, but not dehydrogenase or ferrochelatase activity . Certain mutants in conserved amino acid residues in the C-terminal domain affect S-adenosyl-L-methionine (SAM) binding . SAM may be covalently linked to CysG and a multistep transmethylation mechanism has been proposed . Deletion of the N-terminal NAD+ binding site and mutation of certain amino acid residues affect the dehydrogenase and ferrochelatase activities, but not the methylase activity. The two domains can function independently . cysG shows differential codon adaptation, resulting in differential translation efficiency signatures, in halophilic microbes. It was therefore predicted to play a role in the osmotic stress response. A cysG deletion mutant was shown to be more sensitive than wild-type specifically to osmotic stress, but not other stresses . In biotechnology applications, cysG is useful as a stable reference gene for transcriptional analysis during recombinant protein production in some strains of E. coli , but is not useful for transcriptional analysis under salt and organic acid stress conditions . The red fluorescence emitted by products of CysG catalysis allowed develop

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.DIMETHUROPORDEHYDROG-RXN|reaction.ecocyc.DIMETHUROPORDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-13403|reaction.ecocyc.RXN-13403]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-8675|reaction.ecocyc.RXN-8675]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SIROHEME-FERROCHELAT-RXN|reaction.ecocyc.SIROHEME-FERROCHELAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.UROPORIIIMETHYLTRANSA-RXN|reaction.ecocyc.UROPORIIIMETHYLTRANSA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AEA8|protein.P0AEA8]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:SIROHEMESYN-CPLX`
- `QSPROTEOME:QS00155097`

## Notes

2*protein.P0AEA8
