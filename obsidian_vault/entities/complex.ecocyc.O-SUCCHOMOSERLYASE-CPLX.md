---
entity_id: "complex.ecocyc.O-SUCCHOMOSERLYASE-CPLX"
entity_type: "complex"
name: "O-succinylhomoserine(thiol)-lyase / O-succinylhomoserine lyase"
source_database: "EcoCyc"
source_id: "O-SUCCHOMOSERLYASE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# O-succinylhomoserine(thiol)-lyase / O-succinylhomoserine lyase

`complex.ecocyc.O-SUCCHOMOSERLYASE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:O-SUCCHOMOSERLYASE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00935|protein.P00935]]

## Enriched Summary

This pyridoxal 5'-phosphate (PLP) dependent enzyme catalyzes a γ-replacement reaction that produces L-cystathionine and succinate from the substrates O-succinylhomoserine and L-cysteine in the transsulfuration pathway for methionine biosynthesis (see pathway HOMOSER-METSYN-PWY). In the absence of L-cysteine it can catalyze a γ-elimination (deamination) reaction of O-succinylhomoserine to produce 2-oxobutanoate (α-ketobutyrate), ammonia and succinate, although this is considered to be a non-physiological reaction . The enzyme was first purified from Salmonella typhimurium . The native enzyme was later purified from Escherichia coli and characterized as a homotetramer, similar to the Salmonella enzyme . The recombinant enzyme was overproduced in E. coli, purified, and characterized both structurally and kinetically. It contained one PLP binding site per subunit and absorption spectra showed the PLP to be in a Schiff base form with lysine 198 . The PLP binding sites of purified, native E. coli cystathionine γ-synthase (MetB) and cystathionine β-lyase (MetC) were localized on phosphopyridoxal peptides. The amino acid sequences of these peptides were found to be homologous with the PLP binding site of rat liver cystathionine γ-lyase (γ-cystathionase) . MetB also shares 30% identity and 36% overall amino acid sequence homology with MetC, suggesting a common evolutionary origin...

## Biological Role

Catalyzes METBALT-RXN (reaction.ecocyc.METBALT-RXN), O-SUCCHOMOSERLYASE-RXN (reaction.ecocyc.O-SUCCHOMOSERLYASE-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

This pyridoxal 5'-phosphate (PLP) dependent enzyme catalyzes a γ-replacement reaction that produces L-cystathionine and succinate from the substrates O-succinylhomoserine and L-cysteine in the transsulfuration pathway for methionine biosynthesis (see pathway HOMOSER-METSYN-PWY). In the absence of L-cysteine it can catalyze a γ-elimination (deamination) reaction of O-succinylhomoserine to produce 2-oxobutanoate (α-ketobutyrate), ammonia and succinate, although this is considered to be a non-physiological reaction . The enzyme was first purified from Salmonella typhimurium . The native enzyme was later purified from Escherichia coli and characterized as a homotetramer, similar to the Salmonella enzyme . The recombinant enzyme was overproduced in E. coli, purified, and characterized both structurally and kinetically. It contained one PLP binding site per subunit and absorption spectra showed the PLP to be in a Schiff base form with lysine 198 . The PLP binding sites of purified, native E. coli cystathionine γ-synthase (MetB) and cystathionine β-lyase (MetC) were localized on phosphopyridoxal peptides. The amino acid sequences of these peptides were found to be homologous with the PLP binding site of rat liver cystathionine γ-lyase (γ-cystathionase) . MetB also shares 30% identity and 36% overall amino acid sequence homology with MetC, suggesting a common evolutionary origin . Steady-state kinetic analysis of the enzyme showed a ping-pong mechanism . However, later steady state kinetic analysis using continuous assays that employed coupling enzymes suggested that the enzyme has an ordered mechanism at L-cysteine concentrations greater than its Km and a ping-pong mechanism at L-cysteine concentrations lower that its Km . Spectroscopic analysis techniques showed that the γ-re

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.METBALT-RXN|reaction.ecocyc.METBALT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.O-SUCCHOMOSERLYASE-RXN|reaction.ecocyc.O-SUCCHOMOSERLYASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00935|protein.P00935]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:O-SUCCHOMOSERLYASE-CPLX`
- `QSPROTEOME:QS00181763`

## Notes

4*protein.P00935
