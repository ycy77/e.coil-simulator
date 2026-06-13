---
entity_id: "complex.ecocyc.CPLX0-8121"
entity_type: "complex"
name: "acrylyl-CoA reductase"
source_database: "EcoCyc"
source_id: "CPLX0-8121"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# acrylyl-CoA reductase

`complex.ecocyc.CPLX0-8121`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8121`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P26646|protein.P26646]]

## Enriched Summary

Like certain other members of the MDR012 medium-chain dehydrogenase/reductase protein family, purified YhdH has NADPH-dependent acrylyl-CoA reductase activity . The physiological role of YhdH in E. coli is unknown. Crystal structures of YhdH both alone and in complex with NADP were solved at 2.25 and 2.6 Å resolution, respectively. The structures do not indicate the presence of a Zn2+ ion, and thus YhdH may be a quinone oxidoreductase. In the crystal structure, YhdH is a homodimer, with each subunit consisting of a catalytic domain and an NADP-binding domain. NADP binding appears to cause large conformational changes. Potential conserved active site residues have been identified . Site-directed mutagenesis of several amino acid positions, in particular a Ser156Asp mutation, is able to shift the cofactor specificity of the enzyme from NADPH to NADH . A yhdH insertion mutant is hypersensitive to acrylate and 3-HYDROXY-PROPIONATE . AcuI: "acrylate utilization" Like certain other members of the MDR012 medium-chain dehydrogenase/reductase protein family, purified YhdH has NADPH-dependent acrylyl-CoA reductase activity . The physiological role of YhdH in E. coli is unknown. Crystal structures of YhdH both alone and in complex with NADP were solved at 2.25 and 2.6 Å resolution, respectively...

## Biological Role

Catalyzes RXN-9087 (reaction.ecocyc.RXN-9087).

## Annotation

Like certain other members of the MDR012 medium-chain dehydrogenase/reductase protein family, purified YhdH has NADPH-dependent acrylyl-CoA reductase activity . The physiological role of YhdH in E. coli is unknown. Crystal structures of YhdH both alone and in complex with NADP were solved at 2.25 and 2.6 Å resolution, respectively. The structures do not indicate the presence of a Zn2+ ion, and thus YhdH may be a quinone oxidoreductase. In the crystal structure, YhdH is a homodimer, with each subunit consisting of a catalytic domain and an NADP-binding domain. NADP binding appears to cause large conformational changes. Potential conserved active site residues have been identified . Site-directed mutagenesis of several amino acid positions, in particular a Ser156Asp mutation, is able to shift the cofactor specificity of the enzyme from NADPH to NADH . A yhdH insertion mutant is hypersensitive to acrylate and 3-HYDROXY-PROPIONATE . AcuI: "acrylate utilization"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-9087|reaction.ecocyc.RXN-9087]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P26646|protein.P26646]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8121`
- `QSPROTEOME:QS00203727`

## Notes

2*protein.P26646
