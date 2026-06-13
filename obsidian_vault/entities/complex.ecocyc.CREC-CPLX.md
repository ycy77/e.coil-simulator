---
entity_id: "complex.ecocyc.CREC-CPLX"
entity_type: "complex"
name: "sensor histidine kinase CreC"
source_database: "EcoCyc"
source_id: "CREC-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sensor histidine kinase CreC

`complex.ecocyc.CREC-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CREC-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P08401|protein.P08401]]

## Enriched Summary

CreC is the sensor histidine kinase of the CreCB two-component signal transduction system which is activated when E. coli is fermenting glucose and during aerobic growth in minimal media containing short chain carbon sources (formate, acetate, lactate, pyruvate and malate); the specific activating ligand is not known; CreCB is not activated during growth in complex media . CreC (formerly PhoM) and CreB (formerly PhoM-ORF2) constitute a 2 component regulatory system; a LacZ'-'PhoM fusion protein containing the C-terminal domain (residues 206-474) of PhoM autophosphorylates in the presence of ATP; phosphoPhoM transfers a phosphoryl group to CreB and to PHOB-MONOMER "PhoB" in vitro (see also ). Deletion of creC abolishes activation of a cre regulon reporter gene under aerobic growth with pyruvate as the sole carbon source or under anaerobic growth in glucose minimal media . creC mutations (ΔcreC and a constitutive allele - creC510 carrying an R77P amino acid substitution) confer phenotypes (yields of fermentation metabolites, NADH/NAD+ ratio) that vary with different aeration levels . The constitutive creC510 mutation (CreCR77P), also known as pho-510 or creC2, is present in many E. coli strains (but not in MG1655); it was originally present in HfrH strains and results in increased expression of CreBC-regulated genes...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Annotation

CreC is the sensor histidine kinase of the CreCB two-component signal transduction system which is activated when E. coli is fermenting glucose and during aerobic growth in minimal media containing short chain carbon sources (formate, acetate, lactate, pyruvate and malate); the specific activating ligand is not known; CreCB is not activated during growth in complex media . CreC (formerly PhoM) and CreB (formerly PhoM-ORF2) constitute a 2 component regulatory system; a LacZ'-'PhoM fusion protein containing the C-terminal domain (residues 206-474) of PhoM autophosphorylates in the presence of ATP; phosphoPhoM transfers a phosphoryl group to CreB and to PHOB-MONOMER "PhoB" in vitro (see also ). Deletion of creC abolishes activation of a cre regulon reporter gene under aerobic growth with pyruvate as the sole carbon source or under anaerobic growth in glucose minimal media . creC mutations (ΔcreC and a constitutive allele - creC510 carrying an R77P amino acid substitution) confer phenotypes (yields of fermentation metabolites, NADH/NAD+ ratio) that vary with different aeration levels . The constitutive creC510 mutation (CreCR77P), also known as pho-510 or creC2, is present in many E. coli strains (but not in MG1655); it was originally present in HfrH strains and results in increased expression of CreBC-regulated genes . The pho-510 mutation is also associated with the constitutive expression of bacterial alkaline phosphatase (BAP) in phoR null mutants; BAP synthesis shows "metastable clonal variation" in phoR null mutants containing 'wild-type' phoM (creC) (and see ). CreC dependent control of BAP expression in a phoR null mutant is subject to carbon control . phoM (creC) has no effect on BAP synthesis in phoR+ bacteria . Constitutive activation of CreC by mutation confers

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P08401|protein.P08401]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CREC-CPLX`
- `QSPROTEOME:QS00049696`

## Notes

2*protein.P08401
