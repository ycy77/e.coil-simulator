---
entity_id: "complex.ecocyc.GPT-CPLX"
entity_type: "complex"
name: "xanthine-guanine phosphoribosyltransferase"
source_database: "EcoCyc"
source_id: "GPT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# xanthine-guanine phosphoribosyltransferase

`complex.ecocyc.GPT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GPT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9M5|protein.P0A9M5]]

## Enriched Summary

Xanthine-guanine phosphoribosyltransferase is a purine salvage enzyme which catalyzes the transfer of the ribosyl-5-phosphate group from PRPP to the N9 position of guanine or xanthine to yield GMP and XANTHOSINE-5-PHOSPHATE, respectively. It can also act on hypoxanthine, although guanine appears to be the preferred substrate . The enzymatic activity is inhibited by GMP and ppGpp . Gpt shares only 23% amino acid sequence identity with E. coli Hpt, despite their common function . This enzyme is one of three E. coli phosphoribosyltransferases (PRTases) that participate in purine salvage, Gpt, Hpt and Apt . They are classified as type I PRTases based on a conserved 5-phospho-α-D-ribosyl-1-pyrophosphate binding-site motif . Based on the native molecular weight obtained by gel filtration, the enzyme was originally thought to be a trimer in solution , but was later found to be a homotetramer . Crystal structures of the free, substrate- and product-bound forms of the enzyme have been solved, and a reaction mechanism has been proposed . Nucleoside monophosphate product analogs that inhibit the enzyme have been identified, and crystal structures of two pyrrolidine phosphonate inhibitors bound to the enzyme have been solved. A 12-amino acid flexible loop that is important for inhibition of the enzyme covers the active site...

## Biological Role

Catalyzes GUANPRIBOSYLTRAN-RXN (reaction.ecocyc.GUANPRIBOSYLTRAN-RXN), HYPOXANPRIBOSYLTRAN-RXN (reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN), XANPRIBOSYLTRAN-RXN (reaction.ecocyc.XANPRIBOSYLTRAN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Xanthine-guanine phosphoribosyltransferase is a purine salvage enzyme which catalyzes the transfer of the ribosyl-5-phosphate group from PRPP to the N9 position of guanine or xanthine to yield GMP and XANTHOSINE-5-PHOSPHATE, respectively. It can also act on hypoxanthine, although guanine appears to be the preferred substrate . The enzymatic activity is inhibited by GMP and ppGpp . Gpt shares only 23% amino acid sequence identity with E. coli Hpt, despite their common function . This enzyme is one of three E. coli phosphoribosyltransferases (PRTases) that participate in purine salvage, Gpt, Hpt and Apt . They are classified as type I PRTases based on a conserved 5-phospho-α-D-ribosyl-1-pyrophosphate binding-site motif . Based on the native molecular weight obtained by gel filtration, the enzyme was originally thought to be a trimer in solution , but was later found to be a homotetramer . Crystal structures of the free, substrate- and product-bound forms of the enzyme have been solved, and a reaction mechanism has been proposed . Nucleoside monophosphate product analogs that inhibit the enzyme have been identified, and crystal structures of two pyrrolidine phosphonate inhibitors bound to the enzyme have been solved. A 12-amino acid flexible loop that is important for inhibition of the enzyme covers the active site . A gpt mutant is unable to grow on xanthine, but can still grow on guanine at a lower growth rate due to the presence of a second guanine phosphoribosyltransferase activity . An hpt gpt double mutant is extremely sensitive to inhibition by adenine due to the role of guanine phosphoribosyltransferase in converting free guanine to GMP when the cell is depleted for guanine nucleotides . A gpt mutant in combination with the optA1 allele of EG10225 dgt, which causes

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.GUANPRIBOSYLTRAN-RXN|reaction.ecocyc.GUANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN|reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.XANPRIBOSYLTRAN-RXN|reaction.ecocyc.XANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9M5|protein.P0A9M5]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:GPT-CPLX`
- `QSPROTEOME:QS00188679`

## Notes

4*protein.P0A9M5
