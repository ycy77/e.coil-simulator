---
entity_id: "complex.ecocyc.CPLX0-8190"
entity_type: "complex"
name: "tRNA U34 carboxymethyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-8190"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tRNA U34 carboxymethyltransferase

`complex.ecocyc.CPLX0-8190`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8190`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76291|protein.P76291]]

## Enriched Summary

CmoB catalyzes the transfer of the carboxymethyl group from carboxy-S-adenosyl-L-methionine (Cx-SAM) to ho5U34 in tRNA. This reaction is the final step in the biosynthesis of the 5-oxyacetyl uridine (cmo5U) modification at the U34 wobble base of certain tRNAs . Crystal structures of apo- and Cx-SAM-bound CmoB have been solved, providing insights into the specificity of the enzyme for Cx-SAM over SAM, one of the most abundant cofactors in nature. The K91 residue involved in Cx-SAM recognition is required for catalytic activity . The cmoB gene used by to overexpress and purify CmoB protein was amplified from E. coli BL21; the sequence is 99% identical to the sequence in E. coli K-12 MG1655. CmoB: "synthesis of cmo5U34" Comment: CmoB catalyzes the transfer of the carboxymethyl group from carboxy-S-adenosyl-L-methionine (Cx-SAM) to ho5U34 in tRNA. This reaction is the final step in the biosynthesis of the 5-oxyacetyl uridine (cmo5U) modification at the U34 wobble base of certain tRNAs . Crystal structures of apo- and Cx-SAM-bound CmoB have been solved, providing insights into the specificity of the enzyme for Cx-SAM over SAM, one of the most abundant cofactors in nature. The K91 residue involved in Cx-SAM recognition is required for catalytic activity . The cmoB gene used by to overexpress and purify CmoB protein was amplified from E...

## Biological Role

Catalyzes RXN0-7067 (reaction.ecocyc.RXN0-7067).

## Annotation

CmoB catalyzes the transfer of the carboxymethyl group from carboxy-S-adenosyl-L-methionine (Cx-SAM) to ho5U34 in tRNA. This reaction is the final step in the biosynthesis of the 5-oxyacetyl uridine (cmo5U) modification at the U34 wobble base of certain tRNAs . Crystal structures of apo- and Cx-SAM-bound CmoB have been solved, providing insights into the specificity of the enzyme for Cx-SAM over SAM, one of the most abundant cofactors in nature. The K91 residue involved in Cx-SAM recognition is required for catalytic activity . The cmoB gene used by to overexpress and purify CmoB protein was amplified from E. coli BL21; the sequence is 99% identical to the sequence in E. coli K-12 MG1655. CmoB: "synthesis of cmo5U34" Comment:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7067|reaction.ecocyc.RXN0-7067]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76291|protein.P76291]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8190`
- `QSPROTEOME:QS00233926`

## Notes

4*protein.P76291
