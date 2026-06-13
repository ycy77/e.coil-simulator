---
entity_id: "complex.ecocyc.CPLXECOLI-7943"
entity_type: "complex"
name: "NMN amidohydrolase"
source_database: "EcoCyc"
source_id: "CPLXECOLI-7943"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# NMN amidohydrolase

`complex.ecocyc.CPLXECOLI-7943`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLXECOLI-7943`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6G3|protein.P0A6G3]]

## Enriched Summary

NMN amidohydrolase takes part in the intracellular recycling of NAD, catalyzing the deamidation of NICOTINAMIDE_NUCLEOTIDE "NMN" to NICOTINATE_NUCLEOTIDE "NaMN" . The enzyme is in the most active path (PNC IV) for recycling NAD in E. coli . Until recently, the gene encoding NMN amidohydrolase was unknown. Aided by genomics-based reconstruction of NAD metabolism, the gene was finally identified by Galeazzi et al. . Site-directed mutagenesis of conserved residues and kinetic analysis of the resulting mutant enzymes enabled the identification of residues involved in catalysis; the enzyme may employ a Ser/Lys dyad active site configuration. A detailed reaction mechanism was proposed . PncC: "pyridine nucleotide cycle" NMN amidohydrolase takes part in the intracellular recycling of NAD, catalyzing the deamidation of NICOTINAMIDE_NUCLEOTIDE "NMN" to NICOTINATE_NUCLEOTIDE "NaMN" . The enzyme is in the most active path (PNC IV) for recycling NAD in E. coli . Until recently, the gene encoding NMN amidohydrolase was unknown. Aided by genomics-based reconstruction of NAD metabolism, the gene was finally identified by Galeazzi et al. . Site-directed mutagenesis of conserved residues and kinetic analysis of the resulting mutant enzymes enabled the identification of residues involved in catalysis; the enzyme may employ a Ser/Lys dyad active site configuration...

## Biological Role

Catalyzes NMNAMIDOHYDRO-RXN (reaction.ecocyc.NMNAMIDOHYDRO-RXN).

## Annotation

NMN amidohydrolase takes part in the intracellular recycling of NAD, catalyzing the deamidation of NICOTINAMIDE_NUCLEOTIDE "NMN" to NICOTINATE_NUCLEOTIDE "NaMN" . The enzyme is in the most active path (PNC IV) for recycling NAD in E. coli . Until recently, the gene encoding NMN amidohydrolase was unknown. Aided by genomics-based reconstruction of NAD metabolism, the gene was finally identified by Galeazzi et al. . Site-directed mutagenesis of conserved residues and kinetic analysis of the resulting mutant enzymes enabled the identification of residues involved in catalysis; the enzyme may employ a Ser/Lys dyad active site configuration. A detailed reaction mechanism was proposed . PncC: "pyridine nucleotide cycle"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.NMNAMIDOHYDRO-RXN|reaction.ecocyc.NMNAMIDOHYDRO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6G3|protein.P0A6G3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLXECOLI-7943`
- `QSPROTEOME:QS00049695`

## Notes

2*protein.P0A6G3
