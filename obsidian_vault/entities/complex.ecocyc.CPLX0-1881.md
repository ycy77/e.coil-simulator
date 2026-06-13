---
entity_id: "complex.ecocyc.CPLX0-1881"
entity_type: "complex"
name: "enamine/imine deaminase, redox-regulated chaperone"
source_database: "EcoCyc"
source_id: "CPLX0-1881"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# enamine/imine deaminase, redox-regulated chaperone

`complex.ecocyc.CPLX0-1881`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1881`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AF93|protein.P0AF93]]

## Enriched Summary

Under physiological conditions, the TAX-562 RidA acts as an EC-3.5.99.10. This activity promotes the release of ammonia from reactive enamine/imine intermediates that are formed by PLP-dependent enzymes such as EC-4.3.1.19. For example, purified RidA was shwn to accelerate the IlvA-dependent formation of 2-ketobutyrate from threonine in vitro . However, when modified by CPD-12799 (HOCl), RidA turns into a potent chaperone-like holdase that can effectively protect different proteins during oxidative stress. For example, HOCl- or CPD-26533- (a HOCl derivative) treated RidA prevent aggregation of denatured citrate synthase in vitro . Deletion of ridA in an E. coli BL21 strain results in increased sensitivity to HOCl; lack of ridA may be lethal in E. coli K-12 MC4100 . RidA activation is mediated by chlorination and is accompanied by loss of free amino groups and the resulting loss of positive charges on the protein surface, leading to an increased overall protein hydrophobicity. Two arginine residues (R105 and R128) as well as six lysine residues (K3, K38, K67, K79, K115, K118) have been shown to be N-chlorinated . Chlorination of RidA is reversible; N-chlorinated RidA is dechlorinated by exposure to ithiothreitol and ascorbic acid in vitro and to glutathione and thioredoxin in vivo . Purified, crystallized RidA is homotrimeric...

## Biological Role

Catalyzes RXN-15123 (reaction.ecocyc.RXN-15123), RXN-15127 (reaction.ecocyc.RXN-15127).

## Annotation

Under physiological conditions, the TAX-562 RidA acts as an EC-3.5.99.10. This activity promotes the release of ammonia from reactive enamine/imine intermediates that are formed by PLP-dependent enzymes such as EC-4.3.1.19. For example, purified RidA was shwn to accelerate the IlvA-dependent formation of 2-ketobutyrate from threonine in vitro . However, when modified by CPD-12799 (HOCl), RidA turns into a potent chaperone-like holdase that can effectively protect different proteins during oxidative stress. For example, HOCl- or CPD-26533- (a HOCl derivative) treated RidA prevent aggregation of denatured citrate synthase in vitro . Deletion of ridA in an E. coli BL21 strain results in increased sensitivity to HOCl; lack of ridA may be lethal in E. coli K-12 MC4100 . RidA activation is mediated by chlorination and is accompanied by loss of free amino groups and the resulting loss of positive charges on the protein surface, leading to an increased overall protein hydrophobicity. Two arginine residues (R105 and R128) as well as six lysine residues (K3, K38, K67, K79, K115, K118) have been shown to be N-chlorinated . Chlorination of RidA is reversible; N-chlorinated RidA is dechlorinated by exposure to ithiothreitol and ascorbic acid in vitro and to glutathione and thioredoxin in vivo . Purified, crystallized RidA is homotrimeric. The structure contains a covalent modification on the Sγ of Cys107 . Cys107 is oxidized by peroxynitrite treatment, and the oxidation abolishes the activity as EC-3.5.99.10. A RidA(C107S) substitution mutant retains the activating effect by HOCl and the resulting chaperone activity, but can no longer be inactivated by peroxynitrite treatment . RidA was shown to be modified with fatty acid metabolites in vitro; the modification may occur at C107 . R

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-15123|reaction.ecocyc.RXN-15123]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-15127|reaction.ecocyc.RXN-15127]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AF93|protein.P0AF93]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-1881`
- `QSPROTEOME:QS00199557`

## Notes

3*protein.P0AF93
