---
entity_id: "complex.ecocyc.CPLX-64"
entity_type: "complex"
name: "allantoinase"
source_database: "EcoCyc"
source_id: "CPLX-64"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# allantoinase

`complex.ecocyc.CPLX-64`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-64`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P77671|protein.P77671]]

## Enriched Summary

EC-3.5.2.5, catalyzes the hydrolytic ring cleavage of allantoin at the amide bond between N3 and C4, the first step in the assimilation of allantoin. The enzyme has a very narrow substrate specificity . The enzyme belongs to the cyclic amidohydrolase family, which also includes dihydropyrimidinase, dihydroorotase, hydantoinase, and imidase. Two dynamic loops in the active site are crucial for substrate entrance and product release. E. coli is able to utilize allantoin as a sole source of nitrogen under anaerobic conditions, but can not utilize it as a sole source of carbon . A crystal structure of allantoinase has been solved at 2.1 Å resolution, though the dynamic loops were not observed in that structure. Four monomers are present per asymmetric unit. Six essential residues, H59, H61, Kcx146 (Kcx is a posttranslational carbamylated lysine), H186, H242, and D315, participate in the assembly of a binuclear metal center within the active site. The active site residues N94 and S317 are important for enzymatic activity . A crystal structure of the enzyme from E. coli BL21, which differs by only two residues, was solved later at a resolution of 2.07 Å and resolved the structure of the two active site loops . Allantoinase activity is induced by growth on allantoin as the sole source of nitrogen...

## Biological Role

Catalyzes ALLANTOINASE-RXN (reaction.ecocyc.ALLANTOINASE-RXN). Bound by Zinc cation (molecule.C00038), Cobalt ion (molecule.C00175).

## Annotation

EC-3.5.2.5, catalyzes the hydrolytic ring cleavage of allantoin at the amide bond between N3 and C4, the first step in the assimilation of allantoin. The enzyme has a very narrow substrate specificity . The enzyme belongs to the cyclic amidohydrolase family, which also includes dihydropyrimidinase, dihydroorotase, hydantoinase, and imidase. Two dynamic loops in the active site are crucial for substrate entrance and product release. E. coli is able to utilize allantoin as a sole source of nitrogen under anaerobic conditions, but can not utilize it as a sole source of carbon . A crystal structure of allantoinase has been solved at 2.1 Å resolution, though the dynamic loops were not observed in that structure. Four monomers are present per asymmetric unit. Six essential residues, H59, H61, Kcx146 (Kcx is a posttranslational carbamylated lysine), H186, H242, and D315, participate in the assembly of a binuclear metal center within the active site. The active site residues N94 and S317 are important for enzymatic activity . A crystal structure of the enzyme from E. coli BL21, which differs by only two residues, was solved later at a resolution of 2.07 Å and resolved the structure of the two active site loops . Allantoinase activity is induced by growth on allantoin as the sole source of nitrogen . AllB has low affinity for allantoin, but is allosterically activated by direct binding of the allantoin catabolic enzyme GLY3KIN-MONOMER (G6283) in the presence of GLYOX. Activation by GlxK leads to increased affinity for allantoin, with a change in Km from more than 15 mM in the absence of glyoxylate to 2.8 mM in the presence of 1 mM glyoxylate . AllB binds to the B0511-MONOMER "allantoin transporter AllW", forming a functional 'membrane transport metabolon'. The binding is require

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ALLANTOINASE-RXN|reaction.ecocyc.ALLANTOINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P77671|protein.P77671]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX-64`
- `QSPROTEOME:QS00182705`

## Notes

4*protein.P77671
