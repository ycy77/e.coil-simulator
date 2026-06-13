---
entity_id: "complex.ecocyc.ORNDECARBOX-BIO-CPLX"
entity_type: "complex"
name: "constitutive ornithine decarboxylase"
source_database: "EcoCyc"
source_id: "ORNDECARBOX-BIO-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# constitutive ornithine decarboxylase

`complex.ecocyc.ORNDECARBOX-BIO-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ORNDECARBOX-BIO-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P21169|protein.P21169]]

## Enriched Summary

When ornithine is available, E. coli is able to synthesize putrescine via two pathways. One pathway yields putrescine directly from ornithine by a reaction catalyzed by ornithine decarboxylase. The other pathway involves two reactions using arginine . In addition, E. coli possesses two forms of ornithine decarboxylase, a biosynthetic (or constitutive) form apparently present in all strains, and a biodegradative (or inducible) form which is present in some strains of E. coli . These two types of ornithine decarboxylases have been characterized in E. coli K-12 . The biodegradative ornithine decarboxylase is induced by low pH and by the presence of omithine in the growth medium. The activity of the biosynthetic ornithine decarboxylases is modulated by a number of positive and negative effectors . The positive effectors include nucleotides, GTP being more effective in activating ornithine decarboxylase , while ppGpp reacts as a negative effector of ornithine decarboxylase . The accumulation of ppGpp leads to the cessation of stable RNA synthesis and appears to be related to the fidelity of protein synthesis . Ornithine decarboxylase regulation was reported to occur by a protein inhibitor named CPD0-1515 that binds to ornithine decarboxylase and non-competitively inhibits its activity. The antizyme is induced by polyamines . The gene encoding E...

## Biological Role

Catalyzes ORNDECARBOX-RXN (reaction.ecocyc.ORNDECARBOX-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

When ornithine is available, E. coli is able to synthesize putrescine via two pathways. One pathway yields putrescine directly from ornithine by a reaction catalyzed by ornithine decarboxylase. The other pathway involves two reactions using arginine . In addition, E. coli possesses two forms of ornithine decarboxylase, a biosynthetic (or constitutive) form apparently present in all strains, and a biodegradative (or inducible) form which is present in some strains of E. coli . These two types of ornithine decarboxylases have been characterized in E. coli K-12 . The biodegradative ornithine decarboxylase is induced by low pH and by the presence of omithine in the growth medium. The activity of the biosynthetic ornithine decarboxylases is modulated by a number of positive and negative effectors . The positive effectors include nucleotides, GTP being more effective in activating ornithine decarboxylase , while ppGpp reacts as a negative effector of ornithine decarboxylase . The accumulation of ppGpp leads to the cessation of stable RNA synthesis and appears to be related to the fidelity of protein synthesis . Ornithine decarboxylase regulation was reported to occur by a protein inhibitor named CPD0-1515 that binds to ornithine decarboxylase and non-competitively inhibits its activity. The antizyme is induced by polyamines . The gene encoding E. coli antizyme was cloned and identified as a bifunctional antizyme/transcriptional regulator . However another publication concluded that the E. coli antizyme is not a direct counterpart of mammalian antizyme genes . The product of E. coli gene atoC (see ATOC-MONOMER) was later identified as the bifunctional protein that has both antizyme activity (posttranslational inhibition of polyamine biosynthetic enzymes) and activity as a tran

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ORNDECARBOX-RXN|reaction.ecocyc.ORNDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P21169|protein.P21169]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ORNDECARBOX-BIO-CPLX`
- `QSPROTEOME:QS00049737`

## Notes

2*protein.P21169
