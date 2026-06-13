---
entity_id: "complex.ecocyc.IMIDHISTID-CPLX"
entity_type: "complex"
name: "imidazoleglycerol-phosphate dehydratase / histidinol-phosphatase"
source_database: "EcoCyc"
source_id: "IMIDHISTID-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# imidazoleglycerol-phosphate dehydratase / histidinol-phosphatase

`complex.ecocyc.IMIDHISTID-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:IMIDHISTID-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P06987|protein.P06987]]

## Enriched Summary

The bifunctional imidazoleglycerol-phosphate dehydratase / histidinol-phosphatase (HisB) carries out the sixth and eighth step of histidine biosynthesis. HisB catalyzes two key reactions in histidine biosynthesis. The first is dehydration of D-ERYTHRO-IMIDAZOLE-GLYCEROL-P to yield IMIDAZOLE-ACETOL-P . The second is a phosphatase reaction that converts L-HISTIDINOL-P into HISTIDINOL . Much initial work was done on the gene and enzyme from Salmonella typhimurium. The two enzymatic activities were found to reside in distinct domains of the enzyme. The amino-terminal end was shown to have histidinol phosphate phosphatase activity, while the carboxy-terminal domain catalyzed the dehydration of imidazole glycerol-3-phosphate . A model for the evolution of the bifunctional hisB gene has been proposed . The amino-terminal domain of HisB (HisB-N) belongs to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. Using a variety of possible substrates (not including histidinol phosphate), no phosphatase activity was detected; thus, the enzyme may be highly substrate-specific. Crystal structures of HisB-N isolated from E. coli O157:H7 have been solved and the functional significance of its metal ion requirements elucidated. A catalytic mechanism differing from that of other HAD-like hydrolases has been proposed . A high-throughput study of protein complexes in E...

## Biological Role

Catalyzes HISTIDPHOS-RXN (reaction.ecocyc.HISTIDPHOS-RXN), IMIDPHOSDEHYD-RXN (reaction.ecocyc.IMIDPHOSDEHYD-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

The bifunctional imidazoleglycerol-phosphate dehydratase / histidinol-phosphatase (HisB) carries out the sixth and eighth step of histidine biosynthesis. HisB catalyzes two key reactions in histidine biosynthesis. The first is dehydration of D-ERYTHRO-IMIDAZOLE-GLYCEROL-P to yield IMIDAZOLE-ACETOL-P . The second is a phosphatase reaction that converts L-HISTIDINOL-P into HISTIDINOL . Much initial work was done on the gene and enzyme from Salmonella typhimurium. The two enzymatic activities were found to reside in distinct domains of the enzyme. The amino-terminal end was shown to have histidinol phosphate phosphatase activity, while the carboxy-terminal domain catalyzed the dehydration of imidazole glycerol-3-phosphate . A model for the evolution of the bifunctional hisB gene has been proposed . The amino-terminal domain of HisB (HisB-N) belongs to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. Using a variety of possible substrates (not including histidinol phosphate), no phosphatase activity was detected; thus, the enzyme may be highly substrate-specific. Crystal structures of HisB-N isolated from E. coli O157:H7 have been solved and the functional significance of its metal ion requirements elucidated. A catalytic mechanism differing from that of other HAD-like hydrolases has been proposed . A high-throughput study of protein complexes in E. coli has identified HisB as a homomultimeric protein . The E. coli O157:H7 HisB-N is a dimer both in solution and the crystal structure. The full-length HisB protein associates into large oligomers; the authors suggest that the basic unit of HisB is a hexamer . Overexpression of the EG10445 gene is able to rescue a mutation in the EG10945 gene .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.HISTIDPHOS-RXN|reaction.ecocyc.HISTIDPHOS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.IMIDPHOSDEHYD-RXN|reaction.ecocyc.IMIDPHOSDEHYD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P06987|protein.P06987]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:IMIDHISTID-CPLX`
- `QSPROTEOME:QS00049726`

## Notes

2*protein.P06987
