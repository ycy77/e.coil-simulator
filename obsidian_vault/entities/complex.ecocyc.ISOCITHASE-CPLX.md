---
entity_id: "complex.ecocyc.ISOCITHASE-CPLX"
entity_type: "complex"
name: "isocitrate dehydrogenase"
source_database: "EcoCyc"
source_id: "ISOCITHASE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# isocitrate dehydrogenase

`complex.ecocyc.ISOCITHASE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ISOCITHASE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P08200|protein.P08200]]

## Enriched Summary

Isocitrate dehydrogenase (ICDH) is the first bacterial enzyme shown to be regulated by phosphorylation/dephosphorylation . The modulation of this key enzyme activity enables E. coli to make rapid shifts between TCA and glyoxalate bypass pathways (see the TCA-GLYOX-BYPASS). Fluxes and intercellular concentrations for this junction have been determined. The state of phosphorylation of isocitrate dehydrogenase determines its activity. There are marked differences in the properties of enzymes from different sources. The E. coli enzyme is not an allosteric protein as isocitrate dehydrogenases from other sources are, and it is cold sensitive. IcdA is observed to have several distinct isoforms . Phosphorylation of the enzyme on a serine residue by isocitrate dehydrogenase kinase/phosphatase inactivates it, and dephosphorylation by the phosphatase reactivates it . Phosphorylation affects the binding of NADP . The enzyme shows allosteric inhibition by phosphoenolpyruvate . In some E. coli K-12 strains, including MG1655, a defective prophage, e14, is present. When present, it maps at the icd site and supplies the C terminal sequence of the gene, coding for 52 amino acid residues...

## Biological Role

Catalyzes ISOCITDEH-RXN (reaction.ecocyc.ISOCITDEH-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

Isocitrate dehydrogenase (ICDH) is the first bacterial enzyme shown to be regulated by phosphorylation/dephosphorylation . The modulation of this key enzyme activity enables E. coli to make rapid shifts between TCA and glyoxalate bypass pathways (see the TCA-GLYOX-BYPASS). Fluxes and intercellular concentrations for this junction have been determined. The state of phosphorylation of isocitrate dehydrogenase determines its activity. There are marked differences in the properties of enzymes from different sources. The E. coli enzyme is not an allosteric protein as isocitrate dehydrogenases from other sources are, and it is cold sensitive. IcdA is observed to have several distinct isoforms . Phosphorylation of the enzyme on a serine residue by isocitrate dehydrogenase kinase/phosphatase inactivates it, and dephosphorylation by the phosphatase reactivates it . Phosphorylation affects the binding of NADP . The enzyme shows allosteric inhibition by phosphoenolpyruvate . In some E. coli K-12 strains, including MG1655, a defective prophage, e14, is present. When present, it maps at the icd site and supplies the C terminal sequence of the gene, coding for 52 amino acid residues. Of the codon differences, most are synonymous, one is conservative; the properties of the enzyme seem not to be affected icd shows differential codon adaptation, resulting in differential translation efficiency signatures, in aerotolerant compared to obligate anaerobic microbes. It was therefore predicted to play a role in the oxidative stress response. An icd deletion mutant was shown to be more sensitive than wild-type specifically to hydrogen peroxide exposure, but not other stresses . The TCA-glyoxylate bypass junction and icd's role in glycolate biosynthesis, have also been studied through transcrip

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ISOCITDEH-RXN|reaction.ecocyc.ISOCITDEH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P08200|protein.P08200]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ISOCITHASE-CPLX`
- `QSPROTEOME:QS00181751`

## Notes

2*protein.P08200
