---
entity_id: "protein.P25397"
entity_type: "protein"
name: "tehB"
source_database: "UniProt"
source_id: "P25397"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:11053398}. Note=Probably a peripheral membrane protein that interacts with TehA."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tehB b1430 JW1426"
---

# tehB

`protein.P25397`

## Static

- Type: `protein`
- Source: `UniProt:P25397`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:11053398}. Note=Probably a peripheral membrane protein that interacts with TehA.

## Enriched Summary

FUNCTION: S-adenosyl-L-methionine dependent methyltransferase that catalyzes the methylation of tellurite and is responsible for tellurite resistance when present in high copy number. Can also methylate selenite and selenium dioxide. Is thus able to detoxify different chalcogens. Cannot methylate arsenic compounds. {ECO:0000269|PubMed:11053398, ECO:0000269|PubMed:21244361}.

## Biological Role

Component of tellurite methyltransferase (complex.ecocyc.CPLX0-7913).

## Annotation

FUNCTION: S-adenosyl-L-methionine dependent methyltransferase that catalyzes the methylation of tellurite and is responsible for tellurite resistance when present in high copy number. Can also methylate selenite and selenium dioxide. Is thus able to detoxify different chalcogens. Cannot methylate arsenic compounds. {ECO:0000269|PubMed:11053398, ECO:0000269|PubMed:21244361}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7913|complex.ecocyc.CPLX0-7913]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1430|gene.b1430]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25397`
- `KEGG:ecj:JW1426;eco:b1430;ecoc:C3026_08320;`
- `GeneID:93775571;945979;`
- `GO:GO:0005829; GO:0008168; GO:0008757; GO:0009636; GO:0032259; GO:0046677; GO:0046690`
- `EC:2.1.1.265`

## Notes

Tellurite methyltransferase (EC 2.1.1.265) (Chalcogen-detoxifying protein TehB) (Selenite methyltransferase) (Tellurite resistance protein TehB)
