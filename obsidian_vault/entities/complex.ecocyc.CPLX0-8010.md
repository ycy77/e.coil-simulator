---
entity_id: "complex.ecocyc.CPLX0-8010"
entity_type: "complex"
name: "carboxy-S-adenosyl-L-methionine synthase"
source_database: "EcoCyc"
source_id: "CPLX0-8010"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# carboxy-S-adenosyl-L-methionine synthase

`complex.ecocyc.CPLX0-8010`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8010`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76290|protein.P76290]]

## Enriched Summary

CmoA catalyzes the conversion of S-adenosyl-L-methionine (SAM) to carboxy-S-adenosyl-L-methionine (Cx-SAM), utilizing prephenate as the carboxyl donor and involving a unique ylide intermediate as the carboxyl acceptor. This reaction is part of the pathway for biosynthesis of the 5-oxyacetyl uridine (cmo5U) modification at the U34 wobble base of certain tRNAs . A crystal structure of CmoA revealed the presence of Cx-SAM in the SAM binding site of the dimeric enzyme . A D89L mutant of CmoA is inactive and when provided on a plasmid, it does not complement the lack of cmo5U modification in RNAs of a cmoA null mutant . In Salmonella enterica serovar Typhimurium, a cmoA null mutation results in the accumulation of 5-methoxyuridine (mo5U34) and 5-hydroxyuridine (ho5U34) in tRNA . The cmoA gene used by to overexpress and purify CmoA was amplified from E. coli BL21; the sequence is 99% identical to the sequence in E. coli K-12 MG1655. The cmoA gene used by was amplified from E. coli OmniMax II cells and contains an R100H point mutation with respect to the sequence in E. coli K-12 MG1655. CmoA: "synthesis of cmo5U34" Comment: CmoA catalyzes the conversion of S-adenosyl-L-methionine (SAM) to carboxy-S-adenosyl-L-methionine (Cx-SAM), utilizing prephenate as the carboxyl donor and involving a unique ylide intermediate as the carboxyl acceptor...

## Biological Role

Catalyzes RXN0-7066 (reaction.ecocyc.RXN0-7066).

## Annotation

CmoA catalyzes the conversion of S-adenosyl-L-methionine (SAM) to carboxy-S-adenosyl-L-methionine (Cx-SAM), utilizing prephenate as the carboxyl donor and involving a unique ylide intermediate as the carboxyl acceptor. This reaction is part of the pathway for biosynthesis of the 5-oxyacetyl uridine (cmo5U) modification at the U34 wobble base of certain tRNAs . A crystal structure of CmoA revealed the presence of Cx-SAM in the SAM binding site of the dimeric enzyme . A D89L mutant of CmoA is inactive and when provided on a plasmid, it does not complement the lack of cmo5U modification in RNAs of a cmoA null mutant . In Salmonella enterica serovar Typhimurium, a cmoA null mutation results in the accumulation of 5-methoxyuridine (mo5U34) and 5-hydroxyuridine (ho5U34) in tRNA . The cmoA gene used by to overexpress and purify CmoA was amplified from E. coli BL21; the sequence is 99% identical to the sequence in E. coli K-12 MG1655. The cmoA gene used by was amplified from E. coli OmniMax II cells and contains an R100H point mutation with respect to the sequence in E. coli K-12 MG1655. CmoA: "synthesis of cmo5U34" Comment:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7066|reaction.ecocyc.RXN0-7066]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76290|protein.P76290]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8010`
- `QSPROTEOME:QS00196141`

## Notes

2*protein.P76290
