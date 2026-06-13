---
entity_id: "complex.ecocyc.CPLX0-8542"
entity_type: "complex"
name: "cupric reductase RclA"
source_database: "EcoCyc"
source_id: "CPLX0-8542"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cupric reductase RclA

`complex.ecocyc.CPLX0-8542`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8542`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77212|protein.P77212]]

## Enriched Summary

RclA plays a role in survival to oxidative stress through its NADH-dependent cupric reductase and hypothiocyanite reductase activities . RclA activity protects E. coli against the toxic effects of the combination of hypochlorous acid (HOCl) and intracellular copper as well as the antimicrobial oxidative effects of hypothiocyanous acid (HOSCN), released during inflammation by the human immune system . RclA shares part of a conserved active site with mercuric reductase . Crystal structures of the enzyme have been solved. Site-directed mutagenesis of predicted active site residues showed that C43 and C48 of the CXXXXC motif are involved in Cu2+ binding and catalysis . The two active site cysteine residues are also required for reduction of HOSCN, confirmed by RclAC43A and RclAC48A mutants being catalytically inactive. The reduction reaction rate of HOSCN with NAD(P)H was found to be more than 100 time faster than with Cu2+ . Reports disagree on whether RclA activity is oxygen-dependent or oxygen-independent . Purified RclA also shows some tellurite reductase activity with NADH as the electron donor . An rclA deletion mutant is more sensitive to HOCl treatment than wild type ; addition of extracellular CuCl2 decreases the sensitivity of both the wild-type and the ΔrclA mutant to sublethal HOCl...

## Biological Role

Catalyzes RXN-15119 (reaction.ecocyc.RXN-15119), hypothiocyanous acid reductase (reaction.ecocyc.RXN-24132), RXN0-7363 (reaction.ecocyc.RXN0-7363).

## Annotation

RclA plays a role in survival to oxidative stress through its NADH-dependent cupric reductase and hypothiocyanite reductase activities . RclA activity protects E. coli against the toxic effects of the combination of hypochlorous acid (HOCl) and intracellular copper as well as the antimicrobial oxidative effects of hypothiocyanous acid (HOSCN), released during inflammation by the human immune system . RclA shares part of a conserved active site with mercuric reductase . Crystal structures of the enzyme have been solved. Site-directed mutagenesis of predicted active site residues showed that C43 and C48 of the CXXXXC motif are involved in Cu2+ binding and catalysis . The two active site cysteine residues are also required for reduction of HOSCN, confirmed by RclAC43A and RclAC48A mutants being catalytically inactive. The reduction reaction rate of HOSCN with NAD(P)H was found to be more than 100 time faster than with Cu2+ . Reports disagree on whether RclA activity is oxygen-dependent or oxygen-independent . Purified RclA also shows some tellurite reductase activity with NADH as the electron donor . An rclA deletion mutant is more sensitive to HOCl treatment than wild type ; addition of extracellular CuCl2 decreases the sensitivity of both the wild-type and the ΔrclA mutant to sublethal HOCl . rclA expression is upregulated under RCS (reactive chlorine species) stress conditions . Insertion mutants show reduced growth in M9 glucose minimal medium compared to rich medium . RclA HOSCN reductase activity is sensitive to the presence of Cu2+, Zn2+ and Ni2+. The sensitization of HOSCN reductase activity by Ni2+ is not RclA-dependent but rather through inhibition of GLUTATHIONE-REDUCT-NADPH-CPLX (Gor) . RNAseq analysis in response to HOSCN exposure revealed the log-fold increas

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-15119|reaction.ecocyc.RXN-15119]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24132|reaction.ecocyc.RXN-24132]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7363|reaction.ecocyc.RXN0-7363]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77212|protein.P77212]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8542`
- `QSPROTEOME:QS00181919`

## Notes

2*protein.P77212
