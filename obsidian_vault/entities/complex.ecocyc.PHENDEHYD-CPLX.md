---
entity_id: "complex.ecocyc.PHENDEHYD-CPLX"
entity_type: "complex"
name: "phenylacetaldehyde dehydrogenase"
source_database: "EcoCyc"
source_id: "PHENDEHYD-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phenylacetaldehyde dehydrogenase

`complex.ecocyc.PHENDEHYD-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PHENDEHYD-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P80668|protein.P80668]]

## Enriched Summary

Phenylacetaldehyde dehydrogenase (FeaB) is the second enzyme in the 2PHENDEG-PWY pathway. The enzyme prefers NAD+ as a cosubstrate and preferentially oxidizes aromatic or hydrophobic aldehydes . It appears to be able to oxidize 4-hydroxy-3-nitrophenylacetaldehyde, the predicted product of 3-nitrotyramine degradation by TynA, to 4-hydroxy-3-nitrophenylacetate . Phenylacetaldehyde dehydrogenase from E. coli W was originally shown to be a dimer in solution ; more recent experiments showed that it is in fact a homotetramer, consistent with the quarternary structure of other highly related enzymes . The hydride transfer step appears to be rate-limiting for FeaB . Expression of FeaB is induced by growth on 2-phenylethylamine as the sole carbon source and by growth on 3-nitrotyramine as the sole nitrogen source . Expression of feaB is activated by FeaR during carbon limitation . Chemotaxis of E. coli towards the neurotransmitter norepinephrine requires the expression of TynA and FeaB . Inactivation of six genes encoding aldehyde dehydrogenases (EG12292, EG10036, EG10110, G6755, G7961, and EG11329) resulted in a strain with greatly reduced aromatic aldehyde oxidation activity (the strain was named ROAR for reduced oxidation and reduction of aromatic aldehydes) . Based on sequence similarity, FeaB was predicted to act on 4-AMINO-BUTYRALDEHYDE and SUCC-S-ALD...

## Biological Role

Catalyzes PHENDEHYD-RXN (reaction.ecocyc.PHENDEHYD-RXN).

## Annotation

Phenylacetaldehyde dehydrogenase (FeaB) is the second enzyme in the 2PHENDEG-PWY pathway. The enzyme prefers NAD+ as a cosubstrate and preferentially oxidizes aromatic or hydrophobic aldehydes . It appears to be able to oxidize 4-hydroxy-3-nitrophenylacetaldehyde, the predicted product of 3-nitrotyramine degradation by TynA, to 4-hydroxy-3-nitrophenylacetate . Phenylacetaldehyde dehydrogenase from E. coli W was originally shown to be a dimer in solution ; more recent experiments showed that it is in fact a homotetramer, consistent with the quarternary structure of other highly related enzymes . The hydride transfer step appears to be rate-limiting for FeaB . Expression of FeaB is induced by growth on 2-phenylethylamine as the sole carbon source and by growth on 3-nitrotyramine as the sole nitrogen source . Expression of feaB is activated by FeaR during carbon limitation . Chemotaxis of E. coli towards the neurotransmitter norepinephrine requires the expression of TynA and FeaB . Inactivation of six genes encoding aldehyde dehydrogenases (EG12292, EG10036, EG10110, G6755, G7961, and EG11329) resulted in a strain with greatly reduced aromatic aldehyde oxidation activity (the strain was named ROAR for reduced oxidation and reduction of aromatic aldehydes) . Based on sequence similarity, FeaB was predicted to act on 4-AMINO-BUTYRALDEHYDE and SUCC-S-ALD . FeaB: 2-phenylethylamine catabolism

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PHENDEHYD-RXN|reaction.ecocyc.PHENDEHYD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P80668|protein.P80668]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:PHENDEHYD-CPLX`
- `QSPROTEOME:QS00196155`

## Notes

4*protein.P80668
