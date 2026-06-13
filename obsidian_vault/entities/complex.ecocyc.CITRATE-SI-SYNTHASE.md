---
entity_id: "complex.ecocyc.CITRATE-SI-SYNTHASE"
entity_type: "complex"
name: "citrate synthase"
source_database: "EcoCyc"
source_id: "CITRATE-SI-SYNTHASE"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# citrate synthase

`complex.ecocyc.CITRATE-SI-SYNTHASE`

## Static

- Type: `complex`
- Source: `EcoCyc:CITRATE-SI-SYNTHASE`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ABH7|protein.P0ABH7]]

## Enriched Summary

The E. coli citrate synthase is a type II enzyme, which appears to be unique to the Gram-negative bacteria. It behaves like a trimer of dimeric subunits; the dimer appears to be the basic catalytic unit , but the hexameric form is required for allosteric inhibition by NADH. By contrast, citrate synthase from animals, plants and some bacteria is a simple dimer that is not allosterically regulated . Citrate synthase activity is allosterically inhibited by NADH . Acetyl-CoA appears to be able to bind to both the allosteric and active sites of the enzyme . Inhibition by 2-oxoglutarate was also thought to be allosteric , but was later shown to be competitive at the active site . Crystal structures of citrate synthase have been solved, providing insight into the allosteric regulatory mechanism of the enzyme . Using chemoproteomics analysis with a stable analogue of 3-pHis, GltA was identified as a putative phosphohistidine acceptor at 5 amino acids residues . A mutant enzyme that is dimeric and insensitive to regulation by NADH and 2-oxoglutarate has been characterized . Citrate synthase mutants require glutamate for growth . Enzyme synthesis is subject to catabolite repression , is repressed by glucose and anaerobiosis, and induced by acetate and oxygen. When acetate is the carbon source, citrate synthase is rate-limiting for the TCA cycle...

## Biological Role

Catalyzes CITSYN-RXN (reaction.ecocyc.CITSYN-RXN).

## Annotation

The E. coli citrate synthase is a type II enzyme, which appears to be unique to the Gram-negative bacteria. It behaves like a trimer of dimeric subunits; the dimer appears to be the basic catalytic unit , but the hexameric form is required for allosteric inhibition by NADH. By contrast, citrate synthase from animals, plants and some bacteria is a simple dimer that is not allosterically regulated . Citrate synthase activity is allosterically inhibited by NADH . Acetyl-CoA appears to be able to bind to both the allosteric and active sites of the enzyme . Inhibition by 2-oxoglutarate was also thought to be allosteric , but was later shown to be competitive at the active site . Crystal structures of citrate synthase have been solved, providing insight into the allosteric regulatory mechanism of the enzyme . Using chemoproteomics analysis with a stable analogue of 3-pHis, GltA was identified as a putative phosphohistidine acceptor at 5 amino acids residues . A mutant enzyme that is dimeric and insensitive to regulation by NADH and 2-oxoglutarate has been characterized . Citrate synthase mutants require glutamate for growth . Enzyme synthesis is subject to catabolite repression , is repressed by glucose and anaerobiosis, and induced by acetate and oxygen. When acetate is the carbon source, citrate synthase is rate-limiting for the TCA cycle . GltA is expressed with a 'slow' codon usage bias in E. coli; substitution of 'fast' codons (i.e. silent mutations) does not alter transcription rates (mRNA levels are the same) nor translation, protein folding and function. This is in contrast to other genes, such as EG10351 and EG10372, with conserved 'slow' codon usage .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CITSYN-RXN|reaction.ecocyc.CITSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ABH7|protein.P0ABH7]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CITRATE-SI-SYNTHASE`
- `QSPROTEOME:QS00183251`

## Notes

6*protein.P0ABH7
