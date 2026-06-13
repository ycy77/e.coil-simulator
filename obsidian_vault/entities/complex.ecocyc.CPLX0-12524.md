---
entity_id: "complex.ecocyc.CPLX0-12524"
entity_type: "complex"
name: "phosphatidylserine synthase"
source_database: "EcoCyc"
source_id: "CPLX0-12524"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "CDP-diacylglycerol-serine O-phosphatidyltransferase"
---

# phosphatidylserine synthase

`complex.ecocyc.CPLX0-12524`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-12524`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P23830|protein.P23830]]

## Enriched Summary

Phosphatidylserine synthase (PssA) catalyzes the de novo synthesis of phosphatidylserine, the first committed step to phosphatidylethanolamine biosynthesis from precursors. When exposed to L-homoserine in minimal media both in vitro and in vivo, E. coli can accumulate phosphatidylhomoserine (PHS) and phosphatidylpropanolamine (PPA), a decarboxylated form of PHS, but not when pssA was deleted. The amounts of PHS and PPA were less than phosphatidylglycerol (PG) and phosphotidylethanolamine (PE) levels that occur in the presence of serine . Some of the enzymes involved in phospholipid biosynthesis interact and may form a functional complex in the membrane . The enzymatic activity of phosphatidylserine synthase is modulated by the membrane phospholipid composition and may constitute a regulatory mechanism . Catalysis by PssA appears to involve a two-step ping-pong mechanism that involves an enzyme-bound phosphatidyl intermediate . The enzyme is unique among the phospholipid biosynthetic enzymes in that it is tightly associated with ribosomes in crude extracts . Increased ionic strength or addition of the polyamine spermidine leads to dissociation from the ribosomal fraction , while addition of membranes containing either the substrate CDP-diacylglycerol or the product phosphatidylserine lead to membrane association...

## Biological Role

Catalyzes PHOSPHASERSYN-RXN (reaction.ecocyc.PHOSPHASERSYN-RXN), phosphotidylhomoserine synthase (reaction.ecocyc.RXN0-7499).

## Annotation

Phosphatidylserine synthase (PssA) catalyzes the de novo synthesis of phosphatidylserine, the first committed step to phosphatidylethanolamine biosynthesis from precursors. When exposed to L-homoserine in minimal media both in vitro and in vivo, E. coli can accumulate phosphatidylhomoserine (PHS) and phosphatidylpropanolamine (PPA), a decarboxylated form of PHS, but not when pssA was deleted. The amounts of PHS and PPA were less than phosphatidylglycerol (PG) and phosphotidylethanolamine (PE) levels that occur in the presence of serine . Some of the enzymes involved in phospholipid biosynthesis interact and may form a functional complex in the membrane . The enzymatic activity of phosphatidylserine synthase is modulated by the membrane phospholipid composition and may constitute a regulatory mechanism . Catalysis by PssA appears to involve a two-step ping-pong mechanism that involves an enzyme-bound phosphatidyl intermediate . The enzyme is unique among the phospholipid biosynthetic enzymes in that it is tightly associated with ribosomes in crude extracts . Increased ionic strength or addition of the polyamine spermidine leads to dissociation from the ribosomal fraction , while addition of membranes containing either the substrate CDP-diacylglycerol or the product phosphatidylserine lead to membrane association . The enzymatic activity is modulated by the structure of the lipid vesicles and the type of phospholipids present . Both of the major anionic membrane lipids stimulate phosphatidylserine synthase activity . Two monomeric crystal structures of PssA with and without its CDP-DG substrate (at resolutions of 2.44 and 2.83 Å, respectively) found that the non-substrate bound apo-enzyme is not associated with the membrane and can form a dimer in solution. The substrate-

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.PHOSPHASERSYN-RXN|reaction.ecocyc.PHOSPHASERSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7499|reaction.ecocyc.RXN0-7499]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P23830|protein.P23830]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-12524`
- `QSPROTEOME:QS00181691`

## Notes

2*protein.P23830
