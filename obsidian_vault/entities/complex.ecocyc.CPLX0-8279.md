---
entity_id: "complex.ecocyc.CPLX0-8279"
entity_type: "complex"
name: "murein lipoprotein"
source_database: "EcoCyc"
source_id: "CPLX0-8279"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Braun lipoprotein"
---

# murein lipoprotein

`complex.ecocyc.CPLX0-8279`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8279`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P69776|protein.P69776]]

## Enriched Summary

lpp encodes murein lipoprotein, also known as Braun lipoprotein or Lpp for short. Lpp is initially translated as a 78 residue Prolipoproteins "prolipoprotein" (or more correctly pre-prolipoprotein) containing a 20 residue signal sequence at the amino terminus and a conserved 'lipobox' motif containing an invariant cysteine residue (Cys+1) that is the site of lipid attachment. The Lpp prolipoprotein is translocated across the inner membrane by the Sec complex (further ). Once transported to the outer face of the membrane the prolipoprotein is modified by the sequential action of three membrane-bound enzymes: EG12128-MONOMER (Lgt) that transfers an sn-1,2-diacylglyceryl group from phosphatidylglycerol to the sulfhydryl group of Cys+1 ; EG10548-MONOMER "signal peptidase II" (Lsp) that cleaves diacylglyceryl-prolipoprotein at the amino-terminal end of diacylated Cys+1 (see and references within), and EG10168-MONOMER (Lnt) that adds an acyl lipid chain from the sn-1 position of a phosphoglycerol lipid-donor to the free α-amino group of the now N-terminal Cys residue, resulting in mature triacylated lipoprotein (see PWY-7884). After post-translational modification murein lipoprotein is released from the outer face of the inner membrane and exported to the outer membrane via the 'lipoprotein outer membrane localization' pathway - the Lol pathway (reviewed in )...

## Annotation

lpp encodes murein lipoprotein, also known as Braun lipoprotein or Lpp for short. Lpp is initially translated as a 78 residue Prolipoproteins "prolipoprotein" (or more correctly pre-prolipoprotein) containing a 20 residue signal sequence at the amino terminus and a conserved 'lipobox' motif containing an invariant cysteine residue (Cys+1) that is the site of lipid attachment. The Lpp prolipoprotein is translocated across the inner membrane by the Sec complex (further ). Once transported to the outer face of the membrane the prolipoprotein is modified by the sequential action of three membrane-bound enzymes: EG12128-MONOMER (Lgt) that transfers an sn-1,2-diacylglyceryl group from phosphatidylglycerol to the sulfhydryl group of Cys+1 ; EG10548-MONOMER "signal peptidase II" (Lsp) that cleaves diacylglyceryl-prolipoprotein at the amino-terminal end of diacylated Cys+1 (see and references within), and EG10168-MONOMER (Lnt) that adds an acyl lipid chain from the sn-1 position of a phosphoglycerol lipid-donor to the free α-amino group of the now N-terminal Cys residue, resulting in mature triacylated lipoprotein (see PWY-7884). After post-translational modification murein lipoprotein is released from the outer face of the inner membrane and exported to the outer membrane via the 'lipoprotein outer membrane localization' pathway - the Lol pathway (reviewed in ). Lpp is considered to be the most abundant (lipo)protein in Escherichia coli; estimates suggest that it is present at approximately 750,000 copies per cell, comprises 2% of the dry weight of the cell and accounts for more than 40% of the peptidoglycan on a weight basis and see . Lpp physically tethers the outer membrane to the peptidoglycan layer; Lpp dictates the distance between the inner membrane (IM) and the outer me

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P69776|protein.P69776]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-8279`
- `QSPROTEOME:QS00049688`

## Notes

3*protein.P69776
