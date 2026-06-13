---
entity_id: "complex.ecocyc.CPLX0-7688"
entity_type: "complex"
name: "succinate-semialdehyde dehydrogenase (NADP+) GabD"
source_database: "EcoCyc"
source_id: "CPLX0-7688"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# succinate-semialdehyde dehydrogenase (NADP+) GabD

`complex.ecocyc.CPLX0-7688`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7688`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P25526|protein.P25526]]

## Enriched Summary

E. coli K-12 encodes two succinate semialdehyde dehydrogenases, GabD and G6811-MONOMER Sad, which differ in their ability to utilize NAD+ and NADP+. The larger enzyme, GabD, was shown to utilize NADP+ . GabD also functions as a glutarate semialdehyde dehydrogenase during degradation of L-lysine . NMR experiments suggest that only the aldehyde form, but not the gem-diol form, of succinate semialdehyde binds to the enzyme . Crystal structures of GabD have been solved . Two domain-swapped dimers form a homotetramer in the crystal structure . It is unclear whether or not the E. coli enzyme, like its human ortholog ALDH5A1, undergoes structural changes in response to changes in environmental redox status. reported that oxidation of the catalytic Cys residue by treatment with hydrogen peroxide irreversibly inactivates the E. coli enzyme, while reported that hydrogen peroxide-inactivated GabD can be reactivated by addition of DDT. The positioning of the NADP+ cosubstrate in the active site and comparison to the structure of the NAD+-specific human enzyme revealed the basis for GabD's preference for NADP+ over NAD+...

## Biological Role

Catalyzes RXN-8182 (reaction.ecocyc.RXN-8182), SUCCSEMIALDDEHYDROG-RXN (reaction.ecocyc.SUCCSEMIALDDEHYDROG-RXN).

## Annotation

E. coli K-12 encodes two succinate semialdehyde dehydrogenases, GabD and G6811-MONOMER Sad, which differ in their ability to utilize NAD+ and NADP+. The larger enzyme, GabD, was shown to utilize NADP+ . GabD also functions as a glutarate semialdehyde dehydrogenase during degradation of L-lysine . NMR experiments suggest that only the aldehyde form, but not the gem-diol form, of succinate semialdehyde binds to the enzyme . Crystal structures of GabD have been solved . Two domain-swapped dimers form a homotetramer in the crystal structure . It is unclear whether or not the E. coli enzyme, like its human ortholog ALDH5A1, undergoes structural changes in response to changes in environmental redox status. reported that oxidation of the catalytic Cys residue by treatment with hydrogen peroxide irreversibly inactivates the E. coli enzyme, while reported that hydrogen peroxide-inactivated GabD can be reactivated by addition of DDT. The positioning of the NADP+ cosubstrate in the active site and comparison to the structure of the NAD+-specific human enzyme revealed the basis for GabD's preference for NADP+ over NAD+ . Inactivation of six genes encoding aldehyde dehydrogenases (EG12292, EG10036, EG10110, G6755, G7961, and EG11329) resulted in a strain with greatly reduced aromatic aldehyde oxidation activity (the strain was named ROAR for reduced oxidation and reduction of aromatic aldehydes) . The operon containing gabD appears to be regulated by catabolite repression and nitrogen source ; transcriptional regulation has been studied extensively . GabD activity is not induced by 4-AMINO-BUTYRATE (GABA) or PUTRESCINE . It was initially reported that wild-type E. coli K-12 strains do not grow on 4-AMINO-BUTYRATE (GABA) as the sole source of carbon or nitrogen, although mutants that

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-8182|reaction.ecocyc.RXN-8182]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SUCCSEMIALDDEHYDROG-RXN|reaction.ecocyc.SUCCSEMIALDDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P25526|protein.P25526]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7688`
- `QSPROTEOME:QS00181823`

## Notes

4*protein.P25526
