---
entity_id: "complex.ecocyc.CPLX0-11183"
entity_type: "complex"
name: "tRNA (Gm18) 2'-O-methyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-11183"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tRNA (Gm18) 2'-O-methyltransferase

`complex.ecocyc.CPLX0-11183`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-11183`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AGJ2|protein.P0AGJ2]]

## Enriched Summary

TrmH is the methyltransferase responsible for 2'-O-methylation of ribose at position G18 in certain tRNAs . Unlike Type I enzymes (e.g. from Thermus thermophilus) that can modify all tRNA species, the E. coli enzyme is a Type II enzyme that only modifies a subset of tRNAs. The catalytic domain of TrmH is responsible for substrate selectivity . The subset of tRNA substrates that are most efficiently methylated by TrmH have longer variable regions and a shorter distance between the G18 and A14 nucleotides . TrmH belongs to the SPOUT superfamily of methyltransferases and was identified early as a member of a protein family predicted to include rRNA methylases . reported no growth defect of a trmH in LB or MOPS-glucose medium, while found a lower growth rate in rich-MOPS medium compared to wild type. The ΔspoU3 insertion-deletion allele of trmH causes phenotypes due to polar effects on recG gene expression . A trmH trmA truB triple mutant shows a defect in the tRNA modifications Gm18, m5U54, and Ψ55 as well as translation defects, heat sensitivity, and a growth defect . A crystal structure was obtained to a resolution of 1.95 Å when a single point mutation (E107G) was introduce and KCl concentration was high. The functional protein is a dimer with the characteristic trefoil knot structure of SPOUT methyltransferases in each subunit...

## Biological Role

Catalyzes 2.1.1.34-RXN (reaction.ecocyc.2.1.1.34-RXN).

## Annotation

TrmH is the methyltransferase responsible for 2'-O-methylation of ribose at position G18 in certain tRNAs . Unlike Type I enzymes (e.g. from Thermus thermophilus) that can modify all tRNA species, the E. coli enzyme is a Type II enzyme that only modifies a subset of tRNAs. The catalytic domain of TrmH is responsible for substrate selectivity . The subset of tRNA substrates that are most efficiently methylated by TrmH have longer variable regions and a shorter distance between the G18 and A14 nucleotides . TrmH belongs to the SPOUT superfamily of methyltransferases and was identified early as a member of a protein family predicted to include rRNA methylases . reported no growth defect of a trmH in LB or MOPS-glucose medium, while found a lower growth rate in rich-MOPS medium compared to wild type. The ΔspoU3 insertion-deletion allele of trmH causes phenotypes due to polar effects on recG gene expression . A trmH trmA truB triple mutant shows a defect in the tRNA modifications Gm18, m5U54, and Ψ55 as well as translation defects, heat sensitivity, and a growth defect . A crystal structure was obtained to a resolution of 1.95 Å when a single point mutation (E107G) was introduce and KCl concentration was high. The functional protein is a dimer with the characteristic trefoil knot structure of SPOUT methyltransferases in each subunit . Interestingly, tRNATyr lacking the Gm18 modification elicits release of interferon-α in human peripheral blood, while the modified tRNA does not . TrmH: "tRNA methylation"; H refers to the 8th identified gene for tRNA methylation Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.1.1.34-RXN|reaction.ecocyc.2.1.1.34-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AGJ2|protein.P0AGJ2]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-11183`
- `QSPROTEOME:QS00167441`

## Notes

2*protein.P0AGJ2
