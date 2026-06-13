---
entity_id: "complex.ecocyc.3-ISOPROPYLMALDEHYDROG-CPLX"
entity_type: "complex"
name: "3-isopropylmalate dehydrogenase"
source_database: "EcoCyc"
source_id: "3-ISOPROPYLMALDEHYDROG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "IPMDH"
---

# 3-isopropylmalate dehydrogenase

`complex.ecocyc.3-ISOPROPYLMALDEHYDROG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:3-ISOPROPYLMALDEHYDROG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P30125|protein.P30125]]

## Enriched Summary

3-isopropylmalate dehydrogenase (LeuB) carries out the third step in leucine biosynthesis, catalyzing the conversion of 3-isopropylmalate to 2-isopropyl-3-oxosuccinate. LeuB oxidizes 3-isopropylmalate with NAD+ to generate 2-isopropyl-3-oxosuccinate and NADH . The activity is dependent on divalent cations, Mg2+ and Mn2+, with Mn2+ being the preferred cation . A crystal structure of 3-isopropylmalate dehydrogenase to 2.1 Å resolution reveals that it is a dimer . The monomers are divided into two domains. The refolding mechanism of the homodimer was investigated by monitoring a complex time course of refolding . A single amino acid replacement at glutamine 200 increased thermostability by creating an intersubunit ion pair which can join existing ion clusters . Catalytic analyses of amino acid substitutions based on ancestral sequence reconstruction identified 3 key substitutions that contributed to the thermostability of E. coli's LeuB compared to its ancestors . The leucine operon consists of four structural genes (leuABCD) coding for the three enzymes which are specific for leucine biosynthesis. The leuB gene codes for 3'-isopropylmalate dehydrogenase . In auxotrophs, starvation for leucine triggers derepression of the leu operon and increased rates of leuB mRNA transcription...

## Biological Role

Catalyzes RXN-13158 (reaction.ecocyc.RXN-13158). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

3-isopropylmalate dehydrogenase (LeuB) carries out the third step in leucine biosynthesis, catalyzing the conversion of 3-isopropylmalate to 2-isopropyl-3-oxosuccinate. LeuB oxidizes 3-isopropylmalate with NAD+ to generate 2-isopropyl-3-oxosuccinate and NADH . The activity is dependent on divalent cations, Mg2+ and Mn2+, with Mn2+ being the preferred cation . A crystal structure of 3-isopropylmalate dehydrogenase to 2.1 Å resolution reveals that it is a dimer . The monomers are divided into two domains. The refolding mechanism of the homodimer was investigated by monitoring a complex time course of refolding . A single amino acid replacement at glutamine 200 increased thermostability by creating an intersubunit ion pair which can join existing ion clusters . Catalytic analyses of amino acid substitutions based on ancestral sequence reconstruction identified 3 key substitutions that contributed to the thermostability of E. coli's LeuB compared to its ancestors . The leucine operon consists of four structural genes (leuABCD) coding for the three enzymes which are specific for leucine biosynthesis. The leuB gene codes for 3'-isopropylmalate dehydrogenase . In auxotrophs, starvation for leucine triggers derepression of the leu operon and increased rates of leuB mRNA transcription . Overexpression of leuB, either from its chromosomal locus by leucine starvation or from a plasmid, it is able to rescue growth of a ΔdmlA mutant on D-malate as the sole source of carbon due to LeuB's promiscuous D-malate dehydrogenase activity .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-13158|reaction.ecocyc.RXN-13158]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P30125|protein.P30125]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:3-ISOPROPYLMALDEHYDROG-CPLX`
- `QSPROTEOME:QS00180889`

## Notes

2*protein.P30125
