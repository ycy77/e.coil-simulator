---
entity_id: "complex.ecocyc.CPLX0-2901"
entity_type: "complex"
name: "aspartate 1-decarboxylase"
source_database: "EcoCyc"
source_id: "CPLX0-2901"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# aspartate 1-decarboxylase

`complex.ecocyc.CPLX0-2901`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2901`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A790|protein.P0A790]], [[protein.P0A790|protein.P0A790]]

## Enriched Summary

Aspartate 1-decarboxylase catalyzes the oxidative decarboxylation of L-aspartate to yield B-ALANINE, which is needed in the biosynthesis of PANTOTHENATE. This enzyme is one of a small class of enzymes that use a covalently bound pyruvoyl prosthetic group. The pyruvoyl group is thought to act analogously to a pyridoxal phosphate cofactor by forming a Schiff base with the amino group of the substrate and then serving as an electron sink to facilitate the decarboxylation . Pyruvoyl-containing enzymes are expressed as a zymogen which is processed post-translationally by a self-maturation cleavage called serinolysis. E. coli contains two more such enzymes, PHOSPHASERDECARB-DIMER and SAMDECARB-CPLX. The PanD proenzyme (π protein) is processed at the serine residue at position 25, resulting in two subunits, α and β, which form a complex that is enzymatically active. Autocatalytic processing of purified enzyme preparations occurs slowly at room temperature or 37° C, and at a higher rate at elevated temperatures . An ester intermediate at Ser25, formed by an N->O acyl shift, facilitates autoproteolysis . β-elimination of the ester results in proteolysis and the formation of dehydroalanine, which undergoes hydrolysis to form the pyruvoyl group . Experiments in E...

## Biological Role

Catalyzes ASPDECARBOX-RXN (reaction.ecocyc.ASPDECARBOX-RXN).

## Annotation

Aspartate 1-decarboxylase catalyzes the oxidative decarboxylation of L-aspartate to yield B-ALANINE, which is needed in the biosynthesis of PANTOTHENATE. This enzyme is one of a small class of enzymes that use a covalently bound pyruvoyl prosthetic group. The pyruvoyl group is thought to act analogously to a pyridoxal phosphate cofactor by forming a Schiff base with the amino group of the substrate and then serving as an electron sink to facilitate the decarboxylation . Pyruvoyl-containing enzymes are expressed as a zymogen which is processed post-translationally by a self-maturation cleavage called serinolysis. E. coli contains two more such enzymes, PHOSPHASERDECARB-DIMER and SAMDECARB-CPLX. The PanD proenzyme (π protein) is processed at the serine residue at position 25, resulting in two subunits, α and β, which form a complex that is enzymatically active. Autocatalytic processing of purified enzyme preparations occurs slowly at room temperature or 37° C, and at a higher rate at elevated temperatures . An ester intermediate at Ser25, formed by an N->O acyl shift, facilitates autoproteolysis . β-elimination of the ester results in proteolysis and the formation of dehydroalanine, which undergoes hydrolysis to form the pyruvoyl group . Experiments in E. coli and Salmonella enterica have now shown that EG12211-MONOMER "PanZ" is a maturation factor that triggers cleavage of pro-PanD to its mature and active form. An S25A mutation eliminates self-cleavage of the π protein and eliminates enzymatic activity. A strain containing this mutant form of PanD absolutely requires exogenous β-alanine for growth . A crystal structure of aspartate 1-decarboxylase has been solved, identifying the ester intermediate of the autoproteolytic cleavage reaction. The active sites are located b

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ASPDECARBOX-RXN|reaction.ecocyc.ASPDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A790|protein.P0A790]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-2901`
- `QSPROTEOME:QS00158291`
- `PDB:1AW8`

## Notes

4*protein.P0A790|4*protein.P0A790
