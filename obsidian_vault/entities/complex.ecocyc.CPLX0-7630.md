---
entity_id: "complex.ecocyc.CPLX0-7630"
entity_type: "complex"
name: "multifunctional acyl-CoA thioesterase I and protease I and lysophospholipase L1"
source_database: "EcoCyc"
source_id: "CPLX0-7630"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "TAP complex"
---

# multifunctional acyl-CoA thioesterase I and protease I and lysophospholipase L1

`complex.ecocyc.CPLX0-7630`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7630`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PERI-BAC-GN
- Complex type: `structural`
- Components: [[protein.P0ADA1|protein.P0ADA1]]

## Enriched Summary

The TAP complex (TesA) is a broad-specificity esterase that carries out thioesterase, arylesterase, lysophospholipase, and protease activities. Its exact function within the cell is unclear, and may potentially involve generating free fatty acids or salvaging compounds containing ester linkages. TesA is a multifunctional esterase that can act as a thioesterase, arylesterase, lysophospholipase, and limited protease. It acts as a thioesterase on a very wide range of acyl-CoA molecules, although it has been reported to be specific for fatty acyl thioesters of greater than ten carbons, with highest activity on palmityl, palmitoleyl, and cis-vaccenyl esters . The protease activity of TesA has a chymotrypsin-like specificity, but is mainly active on small peptide test substrates rather than larger polypeptides . In a competitive assay using both palmityl-CoA and peptide test substrates, TesA preferentially cleaves the fatty acid and has no activity on the peptides, suggesting that the peptides may be acting as acyl-CoA analogs in vitro . The actual in vivo role of TesA is unclear. Its location in the periplasm largely precludes access to fatty acyl-CoA molecules, although under conditions of TesA overexpression a certain amount of the enzyme remains in the cytoplasm and generates free fatty acids...

## Biological Role

Catalyzes LYSOPHOSPHOLIPASE-RXN (reaction.ecocyc.LYSOPHOSPHOLIPASE-RXN), RXN-9550 (reaction.ecocyc.RXN-9550), RXN-9555 (reaction.ecocyc.RXN-9555), THIOESTER-RXN (reaction.ecocyc.THIOESTER-RXN).

## Annotation

The TAP complex (TesA) is a broad-specificity esterase that carries out thioesterase, arylesterase, lysophospholipase, and protease activities. Its exact function within the cell is unclear, and may potentially involve generating free fatty acids or salvaging compounds containing ester linkages. TesA is a multifunctional esterase that can act as a thioesterase, arylesterase, lysophospholipase, and limited protease. It acts as a thioesterase on a very wide range of acyl-CoA molecules, although it has been reported to be specific for fatty acyl thioesters of greater than ten carbons, with highest activity on palmityl, palmitoleyl, and cis-vaccenyl esters . The protease activity of TesA has a chymotrypsin-like specificity, but is mainly active on small peptide test substrates rather than larger polypeptides . In a competitive assay using both palmityl-CoA and peptide test substrates, TesA preferentially cleaves the fatty acid and has no activity on the peptides, suggesting that the peptides may be acting as acyl-CoA analogs in vitro . The actual in vivo role of TesA is unclear. Its location in the periplasm largely precludes access to fatty acyl-CoA molecules, although under conditions of TesA overexpression a certain amount of the enzyme remains in the cytoplasm and generates free fatty acids . In contrast to the suggestion that peptide degradation by TesA is an in vitro artifact, it has been suggested that TesA acts as a scavenger, breaking down all the esters in its wide substrate range . TesA from E. coli B has been purified and characterized. It appears to be active as a tetramer . A number of crystal structures of TesA have been determined, both alone and in the presence of substrate analogs . Comparison between the unbound structure and TesA bound to octanoic acid s

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.LYSOPHOSPHOLIPASE-RXN|reaction.ecocyc.LYSOPHOSPHOLIPASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9550|reaction.ecocyc.RXN-9550]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9555|reaction.ecocyc.RXN-9555]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.THIOESTER-RXN|reaction.ecocyc.THIOESTER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ADA1|protein.P0ADA1]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7630`
- `QSPROTEOME:QS00049631`
- `PDB:1ivn`
- `PDB:1j00`
- `PDB:1jrl`
- `PDB:1u8u`
- `PDB:1v2g`

## Notes

4*protein.P0ADA1
