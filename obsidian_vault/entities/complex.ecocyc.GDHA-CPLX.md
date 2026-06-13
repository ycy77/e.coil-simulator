---
entity_id: "complex.ecocyc.GDHA-CPLX"
entity_type: "complex"
name: "glutamate dehydrogenase"
source_database: "EcoCyc"
source_id: "GDHA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutamate dehydrogenase

`complex.ecocyc.GDHA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GDHA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P00370|protein.P00370]]

## Enriched Summary

Glutamate dehydrogenase catalyzes the amination step in the ATP-dependent glutamate synthase pathway. Glutamate dehydrogenase catalyzes the NADPH-dependent amination of α-ketoglutarate (2-oxoglutarate) to yield L-glutamate . GdhA has been crystallized on its own, or bound to α-ketoglutarate or NADP+ . Glutamate dehydrogenase has a single NADPH-binding site . Several residues are important for the proper functioning of glutamate dehydrogenase. Mutants in Lys-128 bind reactants quite poorly, and mutants in Lys-92 are inactive, although they still correctly form the hexameric holoenzyme . Asp-165 is involved in catalytic function as well . Glutamate dehydrogenase is induced by growth on glucose and ammonia, but conversely its activity levels drop during growth on L-glutamate, high-concentration ammonia, high-concentration urea, or low glucose . GdhA is subject to degradation by CPLX0-3104 and CPLX0-2881 during carbon or nitrogen starvation . Binding of NADPH alone destabilizes GdhA, leading to its degradation. The protein can be stabilized by allosteric binding of GTP and ppGpp, suggesting a possible mechanism by which phosphate concentration influences use of glutamate dehydrogenase by the cell . GdhA is also regulated at the mRNA level by repetitive extragenic palindromic (REP) sequences 3' to gdhA. Deletion of one of these sequences decreases the half-life of gdhA mRNA 2-fold...

## Biological Role

Catalyzes GLUTDEHYD-RXN (reaction.ecocyc.GLUTDEHYD-RXN).

## Annotation

Glutamate dehydrogenase catalyzes the amination step in the ATP-dependent glutamate synthase pathway. Glutamate dehydrogenase catalyzes the NADPH-dependent amination of α-ketoglutarate (2-oxoglutarate) to yield L-glutamate . GdhA has been crystallized on its own, or bound to α-ketoglutarate or NADP+ . Glutamate dehydrogenase has a single NADPH-binding site . Several residues are important for the proper functioning of glutamate dehydrogenase. Mutants in Lys-128 bind reactants quite poorly, and mutants in Lys-92 are inactive, although they still correctly form the hexameric holoenzyme . Asp-165 is involved in catalytic function as well . Glutamate dehydrogenase is induced by growth on glucose and ammonia, but conversely its activity levels drop during growth on L-glutamate, high-concentration ammonia, high-concentration urea, or low glucose . GdhA is subject to degradation by CPLX0-3104 and CPLX0-2881 during carbon or nitrogen starvation . Binding of NADPH alone destabilizes GdhA, leading to its degradation. The protein can be stabilized by allosteric binding of GTP and ppGpp, suggesting a possible mechanism by which phosphate concentration influences use of glutamate dehydrogenase by the cell . GdhA is also regulated at the mRNA level by repetitive extragenic palindromic (REP) sequences 3' to gdhA. Deletion of one of these sequences decreases the half-life of gdhA mRNA 2-fold . gdhA mutants grow more slowly during carbon-limited growth, as well as when grown in high phosphate and during nutrient stress . The effects of gdhA mutants on E. coli growth and metabolism were further studied under various conditions . Evidence has been presented that gdhA is one of the genes under ArgP control, and gdhA transcription is reduced under conditions of high osmolarity . Purified re

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTDEHYD-RXN|reaction.ecocyc.GLUTDEHYD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P00370|protein.P00370]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:GDHA-CPLX`
- `QSPROTEOME:QS00178315`

## Notes

6*protein.P00370
