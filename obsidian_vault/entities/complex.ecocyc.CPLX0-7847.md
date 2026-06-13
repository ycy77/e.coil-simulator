---
entity_id: "complex.ecocyc.CPLX0-7847"
entity_type: "complex"
name: "4-hydroxythreonine-4-phosphate dehydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-7847"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 4-hydroxythreonine-4-phosphate dehydrogenase

`complex.ecocyc.CPLX0-7847`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7847`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P19624|protein.P19624]]

## Enriched Summary

4-Hydroxythreonine-4-phosphate dehydrogenase (PdxA) catalyzes the fourth step in the PYRIDOXSYN-PWY pathway. PdxA is an NAD+-dependent dehydrogenase responsible for the oxidation of 4-hydroxythreonine-4-phosphate to 3-amino-1-hydroxyacetone-1-phosphate. It was initially believed that formation of 3-amino-1-hydroxyacetone-1-phosphate involves an enzyme-catalyzed oxidation in which 2-amino-3-oxo-4-phosphonooxybutanoate is formed as an intermediate, which could undergo rapid, spontaneous decarboxylation once released from the enzyme . Subsequent work indicates that 3-amino-1-hydroxyacetone-1-phosphate is the only product of the PdxA-catalyzed reaction, and no intermediate 2-amino-3-oxo-4-phosphonooxybutanoate is released from the enzyme during catalysis. PdxA thus appears to catalyze the oxidative decarboxylation of the substrate 4-phospho-hydroxy-L-threonine . Crystal structures of PdxA show a homodimer with both active sites located at the dimer interface. Two zinc ions are each coordinated by three conserved histidine residues, again involving both monomers . pdxA mutants are able to grow on minimal medium supplemented with pyridoxine or pyridoxal . Under conditions when the C. elegans gut microbiota consists of a single E. coli ΔpdxA mutant strain, the life span of the nematode increases by 21% compared to colonization with wild-type E. coli...

## Biological Role

Catalyzes RXN-13179 (reaction.ecocyc.RXN-13179). Bound by Zinc cation (molecule.C00038).

## Annotation

4-Hydroxythreonine-4-phosphate dehydrogenase (PdxA) catalyzes the fourth step in the PYRIDOXSYN-PWY pathway. PdxA is an NAD+-dependent dehydrogenase responsible for the oxidation of 4-hydroxythreonine-4-phosphate to 3-amino-1-hydroxyacetone-1-phosphate. It was initially believed that formation of 3-amino-1-hydroxyacetone-1-phosphate involves an enzyme-catalyzed oxidation in which 2-amino-3-oxo-4-phosphonooxybutanoate is formed as an intermediate, which could undergo rapid, spontaneous decarboxylation once released from the enzyme . Subsequent work indicates that 3-amino-1-hydroxyacetone-1-phosphate is the only product of the PdxA-catalyzed reaction, and no intermediate 2-amino-3-oxo-4-phosphonooxybutanoate is released from the enzyme during catalysis. PdxA thus appears to catalyze the oxidative decarboxylation of the substrate 4-phospho-hydroxy-L-threonine . Crystal structures of PdxA show a homodimer with both active sites located at the dimer interface. Two zinc ions are each coordinated by three conserved histidine residues, again involving both monomers . pdxA mutants are able to grow on minimal medium supplemented with pyridoxine or pyridoxal . Under conditions when the C. elegans gut microbiota consists of a single E. coli ΔpdxA mutant strain, the life span of the nematode increases by 21% compared to colonization with wild-type E. coli . Transcription of pdxA is under growth rate regulation . Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-13179|reaction.ecocyc.RXN-13179]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P19624|protein.P19624]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7847`
- `QSPROTEOME:QS00183097`

## Notes

2*protein.P19624
