---
entity_id: "protein.P46118"
entity_type: "protein"
name: "hexR"
source_database: "UniProt"
source_id: "P46118"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hexR yebK b1853 JW1842"
---

# hexR

`protein.P46118`

## Static

- Type: `protein`
- Source: `UniProt:P46118`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Represses the expression of the hex regulon (zwf, eda, glp and gap). {ECO:0000250}. YebK is a transcriptional regulator implicated in the adaptation to the transition from rich medium to cellobiose minimal medium, reducing the length of the lag phase . Expression of YebK is higher in cellobiose minimal medium than in glucose minimal medium. DNA binding of YebK is reversed by 2-keto-3-deoxygluconate-6-phosphate (KDPG) . A transposon insertion mutation in the yebK gene generates cellular susceptibility to the antibiotics trimethoprim and sulfamethoxazole . On the other hand, inhibition of yebK expression by CRISPRi reduced cellular fitness under treatment with the antibiotics carbonyl cyanide 3-chlorophenylhydrazone (CCCP), rifampicin or sulfamethizole . Genome-wide YebK binding sites were determined in vivo by chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . A transcription factor (TF)-based biosensor, YebK-GFP, sensing the 2-keto-3-deoxy-6-phosphogluconate (KDPG) intermediate of the Entner-Doudoroff pathway (EDP), has been constructed .

## Biological Role

Component of YebK-2-dehydro-3-deoxy-D-gluconate 6-phosphate (complex.ecocyc.CPLX0-8162).

## Annotation

FUNCTION: Represses the expression of the hex regulon (zwf, eda, glp and gap). {ECO:0000250}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8162|complex.ecocyc.CPLX0-8162]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b1853|gene.b1853]] `RegulonDB` `S` - regulator=YebK; target=yebK; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1853|gene.b1853]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46118`
- `KEGG:ecj:JW1842;eco:b1853;ecoc:C3026_10560;`
- `GeneID:93776120;946373;`
- `GO:GO:0003677; GO:0003700; GO:0006355; GO:0006974; GO:0097367; GO:1901135`

## Notes

HTH-type transcriptional regulator HexR (Hex regulon repressor)
