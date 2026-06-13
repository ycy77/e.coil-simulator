---
entity_id: "complex.ecocyc.METHGLYSYN-CPLX"
entity_type: "complex"
name: "methylglyoxal synthase"
source_database: "EcoCyc"
source_id: "METHGLYSYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# methylglyoxal synthase

`complex.ecocyc.METHGLYSYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:METHGLYSYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A731|protein.P0A731]]

## Enriched Summary

Methylglyoxal synthase (MGS) catalyzes the apparently irreversible formation of methylglyoxal from dihydroxyacetone phosphate, an intermediate of GLYCOLYSIS. Methylglyoxal is extremely toxic to the cell, so the presence of methylglyoxal synthase in the organism seems at first paradoxical. The primary role of MGS appears to be the limitation of the accumulation of phosphorylated sugars, providing a bypass pathway for triose phosphate metabolism under conditions where levels of inorganic phosphate are inadequate. The enzyme is not present in abundance and the rate of methylglyoxal synthesis can be maintained at a relatively non-toxic level while still reducing the stress associated with the accumulation of sugar phosphates. A reaction mechanism involving initial deprotonation to the enol form of methylglyoxal has been proposed . Further studies on the reaction mechanism of the enzyme involved site-directed mutagenesis of predicted active site residues and kinetic characterization of the mutant enzymes as well as X-ray crystallography and NMR spectroscopy of wild type and mutant enzymes in complex with various inhibitors . Although gel filtration shows a molecular weight of 67 kDa for MGS , suggesting that the enzyme is a tetramer in solution, the crystal structure shows it to be a homohexamer...

## Biological Role

Catalyzes METHGLYSYN-RXN (reaction.ecocyc.METHGLYSYN-RXN).

## Annotation

Methylglyoxal synthase (MGS) catalyzes the apparently irreversible formation of methylglyoxal from dihydroxyacetone phosphate, an intermediate of GLYCOLYSIS. Methylglyoxal is extremely toxic to the cell, so the presence of methylglyoxal synthase in the organism seems at first paradoxical. The primary role of MGS appears to be the limitation of the accumulation of phosphorylated sugars, providing a bypass pathway for triose phosphate metabolism under conditions where levels of inorganic phosphate are inadequate. The enzyme is not present in abundance and the rate of methylglyoxal synthesis can be maintained at a relatively non-toxic level while still reducing the stress associated with the accumulation of sugar phosphates. A reaction mechanism involving initial deprotonation to the enol form of methylglyoxal has been proposed . Further studies on the reaction mechanism of the enzyme involved site-directed mutagenesis of predicted active site residues and kinetic characterization of the mutant enzymes as well as X-ray crystallography and NMR spectroscopy of wild type and mutant enzymes in complex with various inhibitors . Although gel filtration shows a molecular weight of 67 kDa for MGS , suggesting that the enzyme is a tetramer in solution, the crystal structure shows it to be a homohexamer . Artificially increased uptake and metabolism of ribose leads to an increase in glycolysis intermediates, which leads to production of methylglyoxal by MGS and to subsequent cell death . Deletion of mgsA accelerates co-metabolism of hexose and pentose sugars such as glucose and xylose , perhaps due to increased expression of crp . An mgsA null mutant has no obvious growth defect under most conditions; of the tested conditions, only growth on xylose in the presence of cAMP resulted i

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.METHGLYSYN-RXN|reaction.ecocyc.METHGLYSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A731|protein.P0A731]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:METHGLYSYN-CPLX`
- `QSPROTEOME:QS00195681`

## Notes

6*protein.P0A731
